# TN3155: Debugging universal links

**Framework**: Technotes

Investigate why your universal links are opening in a web browser instead of your app.

#### Overview

[`Universal links`](https://developer.apple.comhttps://developer.apple.com/ios/universal-links/) use [`applinks`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/applinks), an associated domains service, to link directly to content within your app without routing through a web browser or your website. When a user clicks on a universal link, the following occurs:

- The universal link opens directly within the app when the app is installed on the user’s device.
- Otherwise, the the link will open in the user’s default web browser.

If unfamiliar with universal links and how to support them in your code, see [`Supporting Associated Domains`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/supporting-associated-domains) and [`Allowing apps and websites to link to your content`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content). Please note that web browsers, and apps [`registered as browsers`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.web-browser), are not allowed to register universal links by using the `applinks` service.

This document outlines how to:

- [`Test universal links behavior`](tn3155-debugging-universal-links#Test-universal-links-behavior.md)
- [`Understand applinks configuration and rules`](tn3155-debugging-universal-links#Understand-applinks-configuration-and-rules.md)
- [`Use universal links on your site`](tn3155-debugging-universal-links#Use-universal-links-on-your-site.md)
- [`Host and verify your AASA`](tn3155-debugging-universal-links#Host-and-verify-your-AASA.md)
- [`Debug through sysdiagnose`](tn3155-debugging-universal-links#Debug-through-sysdiagnose.md)
- [`Understand Apple’s CDN`](tn3155-debugging-universal-links#Understand-Apples-CDN.md)

#### Test Universal Links Behavior

To test your universal links behavior, paste a link into your Notes app and long-press  it (iOS) or control-click it (macOS) to see your options for following the link. If universal links have been configured correctly, the option to open in your app and in the web browser will both show up. The option you choose will set the default behavior for your device when following universal links from this domain in the future. To change this default choice, repeat the same steps and choose a different option.

> **Note**: Entering the URL directly into the web browser’s address bar will never open the app, as this is direct navigation within the web browser. As long as the user is on your domain after navigating there directly, your site will show a banner to open your app.

On iOS, you can additionally test your universal links with the associated domains diagnostic tests in Developer settings through these steps:

1. Turn on Developer Mode in Settings. Read [`Enabling Developer Mode on a device`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/enabling-developer-mode-on-a-device) for more help.
2. In Settings > Developer, scroll to the section labeled Universal Links and turn on Associated Domains Development.
3. Open Diagnostics and type in your full URL. You will receive feedback on whether this link is valid for an installed app.

If your universal links are invalid, your `applinks` may be configured incorrectly.

#### Understand Applinks Configuration and Rules

Using the Signing and Capabilities tab in Xcode, verify the app has the Associated Domains capability which contains `applinks` in the form of:

```other
applinks:<fully qualified domain>
```

A common problem is caused by using a domain in your `applinks` that doesn’t have an AASA file hosted in the correct location.

Make sure your domains and AASA file paths match. To match a root domain and all subdomains with a wildcard, an AASA file should be hosted at:

```other
https://example.com/.well-known/apple-app-site-association
```

This will only work with the root domain of `applinks:example.com` and subdomains that are matched with the wildcard `applinks:*.example.com`. This will not work with specific subdomains like `applinks:www.example.com` or `applinks:foo.example.com`.

To match a specific subdomain, an AASA file should be hosted at:

```other
https://www.example.com/.well-known/apple-app-site-association
```

This will only work with `applinks:www.example.com`. Each specific subdomain in your `applinks` should have its own matching AASA file path.

> **Note**: Domains in your `applinks` can’t contain a port number. For example, `applinks:example.com:8080` will not open your app.

#### Use Universal Links on Your Site

To use a universal link to open your app while already browsing in the web browser, use a different subdomain. Reasons for this could be completing a questionnaire or choosing to sign in. If a universal link has the same domain as the previous navigation, the web browser will expect the user wants to continue navigating within the browser. Review [`Allowing apps and websites to link your content`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content#Support-universal-links) for more information.

For an example of when to use subdomains, consider an app with the root domain `applinks:example.com` and an AASA containing:

```other
 "components" : [
 {
 "/" : "/login/*",
 "comment" : "Matches any URL with a path that starts with /login/."
 }]
```

If a user is browsing your site in a web browser and chooses a login button with the link `https://example.com/login`, the link will not be opened in the app. The web browser will continue navigation even though the path matches the component above since the domain did not change.

To avoid this:

- Add a subdomain such as `applinks:foo.example.com` to your associated domains in the Signing and Capabilities tab in Xcode.
- Host an AASA at:

```other
https://foo.example.com/.well-known/apple-app-site-association
```

- Give the login button a link of:

```other
https://foo.example.com/login
```

Using a different subdomain prevents the web browser from treating the link as navigation, so it will open the link in your app.

> ❗ **Important**: It is up to third-party web browsers to enable universal links functionality. Universal links may not be enabled in every web browser. For information about other browsers, developers should check with the browser’s vendor. Safari implements all of the function described in this technote.

#### Host and Verify Your Aasa

If your universal links are still not opening in your app, inspect your HTTP response headers and AASA content. For example, log the HTTP response headers and AASA JSON contents in Terminal using the following command:

```zsh
% curl -v https://{domain}/.well-known/apple-app-site-association
```

If the response contains a 301 or 302 HTTP status code, your is doing an HTTP redirect, which is not supported when hosting the AASA file as redirects are not supported.

Instead of hosting your AASA at your root domain and redirecting to serve a subdomain, host your AASA at each domain and subdomain included in your `applinks`. For example, if you have a subdomain like `applinks:www.example.com` and the wildcard `applinks:*.example.com`, host one AASA file here for the subdomain:

```other
https://www.example.com/.well-known/apple-app-site-association
```

and one here for the wildcard:

```other
https://example.com/.well-known/apple-app-site-association
```

> **Note**: Redirection is allowed, although not preferred, when opening universal links from another app. If the link tapped on by the user is not a universal link but redirects to one, the user will be routed through the web browser to the app.

If you see a 403 or 404 HTTP error, your site denied access. Generally, this happens when the AASA file path is not publicly accessible from all IP addresses or your site is blocked for some other reason. Confirm your website’s configuration allows direct access to the AASA file in the `.well-known` directory, in all geographical locations, from any IP address. Specific IP addresses and ranges are not published as they cannot be guaranteed. Additionally, your server should accept all user agent requests. You can verify this by setting a random user agent and confirm if your server responds with the AASA file or an error message. For example:

```zsh
curl -A "MyAgent-Bot/*" https://example.com/.well-known/apple-app-site-association
```

Verify the format of your AASA file. It should contain either an `Array` of `appIDs` and an `Array` of `components`, as shown in [`Supporting Associated Domains`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/supporting-associated-domains), or fields `appID` of type `String` and `paths` of type `Array` (matching the legacy format). Please avoid mixing formats. Doing so may result in unexpected behavior for universal links. An example of the recommended format is below:

```other
 "appIDs": [ "ABCDE12345.com.example.app", "ABCDE12345.com.example.app2" ], 
 "components": [ { 
    "/": "/test/*", 
    "comment": "Matches any URL beginning with /test/" 
    },
    { 
    "/": "/path/1/*", 
    "exclude": true,
    "comment": "Matches any URL beginning with /path/1/ and instructs the system not to open it as a universal link" 
    }]
```

While this is the older format:

```other
"appID": "ABCDE12345.com.example.app",
 "paths": [ "/test/*", NOT "/path/1/*"]
```

To verify that your AASA is in a valid format and pattern matches correctly, use the built-in `swcutil` tool on a Mac. Running `sudo swcutil` in Terminal shows the available commands, including `swcutil dl` and `swcutil verify`.

You can use these commands in Terminal by:

- Running `sudo swcutil dl -d <domain>` to check that the AASA JSON can be downloaded successfully.
- Running `sudo swcutil verify -d <domain> -j <path-to-JSON> [-u <URL>]` to check the contents of a downloaded `.json` AASA file. Verify that your domains match with `-d` and your URL path pattern matches with the JSON with `-u`. If both are successful, you will get a confirmation message.

For an app containing `applinks:example.com` and the AASA shown above, here is an example of using `swcutil verify` where “s” is the service, “a” is the App ID, and “d” is the domain:

```zsh
% sudo swcutil verify -d example.com -j ./example.json -u https://example.com/test
{ s = applinks, a = ABCD123.com.example.app, d = example.com }:
Pattern "https://example.com/test" matched.
```

Since the pattern `/test` is included in the AASA, the JSON has successfully pattern matched and is verified. For the path  `/path/1`, since it is set to be excluded in the AASA, you would see a message confirming the exclusion:

```None
Pattern "https://example.com/path/1" blocked match.
```

If you see this message for a URL path that is not excluded, your AASA has not been matched. Take a look at the [`Debug through sysdiagnose`](tn3155-debugging-universal-links#Debug-through-sysdiagnose.md) section for more information.

#### Debug Through Sysdiagnose

If the output from `swcutil` in the section [`Host and verify your AASA`](tn3155-debugging-universal-links#Host-and-verify-your-AASA.md) is showing invalid universal links, take a sysdiagnose on a device with the app installed by following the linked instructions for each platform in [`Profiles and Logs`](https://developer.apple.comhttps://developer.apple.com/bug-reporting/profiles-and-logs/?name=sysdiagnose). After you have opened the sysdiagnose, open the `swcutil_show.txt` file. Search for your `App ID` to see the information for your `applinks` as shown in the following example.

```other
Service:              applinks
App ID:               1234abcd.com.example
Domain:               example.com
User Approval:        unspecified
Site/Fmwk Approval:   approved
Last Checked:         2023-08-24 10:09:00 +0000
Next Check:           2023-08-18 21:00:19 +0000
```

`User Approval`: Shows the user’s decision to open links in your app or in the web browser. Review [`Test universal links behavior`](tn3155-debugging-universal-links#Test-universal-links-behavior.md) for more information.

`Site/Fmwk Approval`: Specifies if the Apple-managed content delivery network (CDN) has approved your universal links and pattern matched successfully. If it is `approved`, your universal links are working correctly.

If it is `unspecified` or `denied`, please ensure you are allowing full access to all IP addresses and the domain is included in your associated domains. For more information, review [`Understand Apple’s CDN`](tn3155-debugging-universal-links#Understand-Apples-CDN.md).

`Last Check/Next Check`: Specifies the last time Apple’s CDN requested your site for your AASA and when it will check again.

#### Understand Apples Cdn

When your app is installed on a device, Apple’s CDN requests your AASA file. For the CDN to successfully cache the file, it must be hosted on a domain that is available to all IP addresses and ranges, does not redirect, and is not blocked by access policies.

When testing, if you’re running your app from Xcode, using a server that is unreachable from the public internet, or testing changes faster than Apple’s CDN can cache them, use an alternate `developer` mode as described in [`Associated Domains Entitlement`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/entitlements/com_apple_developer_associated-domains). This allows you to bypass Apple’s CDN and pulls your AASA directly from your domain.

> ❗ **Important**: On iOS 14 and later, Apple’s CDN retrieves and caches the AASA file. When your app is installed, devices download the file from the CDN immediately. Devices check for updates approximately once per week after app installation. To download a newer version of the AASA file, reinstall the app. There is no direct CDN invalidation option.

#### Revision History

-  Added User-Agent policies for the hosted AASA file.
-  Clarified how web browsers interact with universal links. Made other minor editorial changes.
-  Made minor changes, added note for port numbers.
-  First published.

## See Also

- [TN3190: USB audio device design considerations](tn3190-usb-audio-device-design-considerations.md)
  Learn the best techniques for designing devices that conform to the USB Audio Device Class specifications.
- [TN3194: Handling account deletions and revoking tokens for Sign in with Apple](tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple.md)
  Learn the best techniques for managing Sign in with Apple user sessions and responding to account deletion requests.
- [TN3193: Managing the on-device foundation model’s context window](tn3193-managing-the-on-device-foundation-model-s-context-window.md)
  Learn how to budget for the context window limit of Apple’s on-device foundation model and handle the error when reaching the limit.
- [TN3115: Bluetooth State Restoration app relaunch rules](tn3115-bluetooth-state-restoration-app-relaunch-rules.md)
  Learn about the conditions under which an iOS app will be relaunched by Bluetooth State Restoration.
- [TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key](tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md)
  Support iPad multitasking and dynamic resizing while updating your app to remove the deprecated full-screen compatibility mode.
- [TN3151: Choosing the right networking API](tn3151-choosing-the-right-networking-api.md)
  Learn which networking API is best for you.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3191: IMAP extensions supported by Mail for iOS, iPadOS, and visionOS](tn3191-imap-extensions-supported-by-mail.md)
  Learn which extensions to the RFC 3501 IMAP protocol are supported by Mail for iOS, iPadOS, and visionOS.
- [TN3134: Network Extension provider deployment](tn3134-network-extension-provider-deployment.md)
  Explore the platforms, packaging, OS versions, and device configurations for Network Extension provider deployment.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3155-debugging-universal-links)*