# Enabling alternative distribution app installation in a browser

**Framework**: Marketplacekit

Add support for browser apps to install alternative distribution apps from websites.

#### Overview

To enable the installation of an alternative distribution app from a webpage, your browser listens for installation requests from the website visitor’s interaction with the page and hands off the request to [`MarketplaceKit`](MarketplaceKit.md). The installation request uses a specific URL scheme ([`MarketplaceKitURIScheme`](marketplacekiturischeme.md)) that the marketplace page assigns to a button. [`MarketplaceKit`](MarketplaceKit.md) handles the request by presenting the app install sheet, in which the person can confirm and install the alternative distribution app on their device.

![Three screenshots of iPhone that show the stages of installing a fictional alternative app marketplace called Megabyte Mart from a website. The left screenshot has the caption App marketplace website and shows the app icon for Megabyte Mart, which is a representation of a shopping basket, below that is the app title Megabyte Mart, below that are lines that represent descriptive text, and below that is the button Install Megabyte Mart. The center screenshot has the caption Install sheet and shows a confirmation, the title of the sheet is megabytemart.com Would Like to Install an App Marketplace, followed by lines that represent descriptive text, followed by the Megabyte Mart app info, which includes the developer name Tapland, Inc. as well as screenshots, below the app info is the Install App Marketplace button, followed by a cancel button. The right screenshot has the caption Installed app marketplace and shows a representation of the homescreen with Megabyte Mart installed.](https://docs-assets.developer.apple.com/published/6480f09e557a4dc0b48881538c1f92b9/enabling-alternative-distribution-app-installation-in-a-browser-1%402x.png)

[`MarketplaceKit`](MarketplaceKit.md) requires a one-to-one mapping between an alternative distribution app and the domain of the website that distributes it. When a page visitor taps a button to install the app, your browser app passes the origin of the site’s main frame to [`MarketplaceKit`](MarketplaceKit.md), which confirms that the owner of the domain also owns the app.

> **Note**: The system requires that your browser app have a specific entitlement to call the [`MarketplaceKit`](MarketplaceKit.md) installation method. For more information and to request the entitlement, see [`com.apple.developer.browser.app-installation`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.browser.app-installation).

#### Respond to App Installation Requests Using Browserenginekit

Browsers that render using [`BrowserEngineKit`](https://developer.apple.com/documentation/BrowserEngineKit) hand off app installation requests to [`MarketplaceKit`](MarketplaceKit.md). Your browser listens for invocations to a URL with the scheme `MarketplaceKit/MarketplaceKitURIScheme`:

```None
marketplace-kit://install
    ?alternativeDistributionPackage=<url>
    &installVerificationToken=<install verification token>
    &token=<authentication token>
    &account=<user id>
    &appShareURL=<URL>;
```

The URL parameters are:

| URL parameter | Description |
| --- | --- |
| `alternativeDistributionPackage` | The app to install in the form of an alternative distribution package. |
| `installVerificationToken` | A required JSON web signature (JWS). |
| `token` | An optional authentication token. |
| `account` | An optional user ID for the page visitor. |
| `appShareURL` | An optional URL to a product landing page for the app on the marketplace website. |

For more information about the parameters, see [`MarketplaceKitURIScheme`](marketplacekiturischeme.md).

To forward the navigation request to [`MarketplaceKit`](MarketplaceKit.md), call the [`requestAppInstallationFromBrowser(for:referrer:)`](applibrary/requestappinstallationfrombrowser(for:referrer:).md) method to display the app install sheet and pass in the following parameters:

| URL parameter | Description |
| --- | --- |
| `url` | The unparsed [`MarketplaceKitURIScheme`](marketplacekiturischeme.md) URL that triggers the installation request. |
| `referrer` | The origin of the main frame that contains the alternative marketplace installation URL. |

> ❗ **Important**:  To comply with operation system requirements, ignore the `marketplace-kit://` URL invocation if the navigation doesn’t result from a user interaction, such as tapping a button, or if the navigation results from a redirect.

#### Respond to App Installation Requests Using Webkit

If your browser app uses [`WebKit`](https://developer.apple.com/documentation/WebKit), modify your app’s [`webView(_:decidePolicyFor:decisionHandler:)`](https://developer.apple.com/documentation/WebKit/WKNavigationDelegate/webView(_:decidePolicyFor:decisionHandler:)-2ni62) navigation delegate method. When the system calls the delegate method with a URL matching the  `MarketplaceKitURIScheme` scheme, call the `decisionHandler` with a value of `WKNavigationActionPolicyAllow`.

Don’t call the [`requestAppInstallationFromBrowser(for:referrer:)`](applibrary/requestappinstallationfrombrowser(for:referrer:).md) method directly. WebKit handles the interaction with [`MarketplaceKit`](MarketplaceKit.md) after you call the navigation delegate’s `decisionHandler` with a value of `WKNavigationActionPolicyAllow`.

Safari is an example of a browser app that uses [`WebKit`](https://developer.apple.com/documentation/WebKit). When a person taps on an `MarketplaceKitURIScheme` URL, it calls Safari’s [`webView(_:decidePolicyFor:decisionHandler:)`](https://developer.apple.com/documentation/WebKit/WKNavigationDelegate/webView(_:decidePolicyFor:decisionHandler:)-2ni62) navigation delegate method with a URL matching the `MarketplaceKitURIScheme`. Safari responds by calling `decisionHandler` with `WKNavigationActionPolicyAllow`, which then causes WebKit to pass the URL to MarketplaceKit and display an install sheet.

#### Test Web Distribution During Development

In iOS or iPadOS 18.2 and later, development builds of browser apps with the default browser entitlement ([`com.apple.developer.web-browser`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.web-browser)) can test the installation of app marketplaces and other apps that distribute over the web. A development build signed with a development or Ad Hoc provisioning profile can run on Simulator and all supported physical devices (iPhone and iPad).


---

*[View on Apple Developer](https://developer.apple.com/documentation/MarketplaceKit/enabling-alternative-distribution-app-installation-in-a-browser)*