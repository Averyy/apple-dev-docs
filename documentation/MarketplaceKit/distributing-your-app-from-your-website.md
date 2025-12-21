# Distributing your app from your website

**Framework**: MarketplaceKit

Configure your app and website to enable people to install your app on their devices from your website.

#### Overview

Alternative app marketplaces install on a person’s device from your website. To distribute your marketplace app, fill out a webform that outlines the qualifications, and if it’s approved, Apple enables you to download a framework that facilitates the secure installation of your app from your website. Coordinate with App Store Connect by providing your web domain and a public key that the system uses to validate your app’s installations. When you submit your app and pass review, App Store Connect enables you to access your approved app’s alternative distribution package. For more information, see [`Submit for Notarization`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/distributing-apps-in-the-european-union/submit-for-notarization).

Deploy a web server and modify your website to link to your marketplace app, which you host on your server. To prepare your app for installation, download and assemble a complete alternative distribution package using the ID that App Store Connect provides; see [`Ingesting an alternative distribution package`](ingesting-an-alternative-distribution-package.md). Add a Download button on your webpage that links to the alternative distribution package. The URL you assign the button uses a custom scheme that browsers handle differently, instructing them to provide the system with your app’s alternative distribution pacakge for installation on the device.

![A diagram that depicts development requirements for an alternative app marketplace, which consists of a client marketplace app, an app webpage, and an app web server.](https://docs-assets.developer.apple.com/published/d83a5b8247180d38525173a57594996d/distributing-your-app-from-your-website-2%402x.png)

> ❗ **Important**: To distribute your app from your website, request approval from Apple. The request process varies by geographic region; see [`Participating in alternative distribution for specific regions`](participating-in-alternative-distribution-for-specific-regions.md). Only people in the European Union can install apps that aren’t marketplaces from a website.

#### Set Up Your App for Alternative Distribution

Distributing your app on the web requires one-time setup with App Store Connect. First, define the domain where you distribute the app by calling the `alternativeDistributionDomains` endpoint:

```None
POST https://api.appstoreconnect.apple.com/v1/alternativeDistributionDomains
```

For more information about the request’s parameters, see [`Add an alternative distribution domain`](https://developer.apple.com/documentation/AppStoreConnectAPI/POST-v1-alternativeDistributionDomains).

Then, supply a public key that App Store Connect uses to verify installation requests for your app by calling the `alternativeDistributionKeys` endpoint:

```None
POST https://api.appstoreconnect.apple.com/v1/alternativeDistributionKeys
```

For steps to create your distribution key, see [`Creating keys and establishing alternative marketplace connections`](https://developer.apple.com/documentation/AppStoreConnectAPI/creating-keys-and-establishing-alternative-marketplace-connections).

If you’re developing an alternative marketplace app, create one distribution key pair and reuse it across all your developer relationships and apps that install from your marketplace. Otherwise, create a distribution key pair for each app that you distribute from your website.

For more information about setting up a marketplace app in App Store Connect, see [`Create a marketplace app`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/distributing-apps-in-the-european-union/create-an-marketplace-app).

#### Submit Your App and Host It on Your Web Server

When you’re ready to distribute your app, submit it to App Store Connect for review. Choose the review type:

If Apple approves your app for distribution, download your app’s  from App Store Connect, this package contains everything that the system needs to install your app. For more information, see [`Get an alternative distribution package ID`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/distributing-apps-in-the-european-union/get-an-alternative-distribution-package-id).

Assemble and host the alternative distribution package on your web server in a location accessible to the device; see [`Ingesting an alternative distribution package`](ingesting-an-alternative-distribution-package.md). When you want to update your app, submit it to App Store Connect and repeat the process.

#### Add a Download Button on Your Webpage

People download your app by tapping a button on your webpage with a URL scheme reserved for app installations. The browser forwards the installation request to the system, which retrieves the right app variant or delta from the alternative distribution package for the app that you host on your server.

![A screenshot of and example download button, a button with the label Install Megabyte Mart.](https://docs-assets.developer.apple.com/published/b38fd2d3f4a9c46a5bcf72022f0772bf/distributing-your-app-from-your-website-3%402x.png)

The button URL is of the [`MarketplaceKitURIScheme`](marketplacekiturischeme.md) format, which provides the system with everything it needs to install the app:

```http
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
| `alternativeDistributionPackage` | Your app’s alternative distribution package. This value has unique domain-matching requirements; for more information, see [`MarketplaceKitURIScheme`](marketplacekiturischeme.md). |
| `installVerificationToken` | A required JSON web signature (JWS). For more information, see [`Supplying an install verification token`](supplying-an-install-verification-token.md). |
| `token` | An optional authentication token to include if downloads require authorization. The device sends the token back to your token endpoint to reference this request. The value is free-form, and can contain any information at your discretion, such as a customer identifier. |
| `account` | An optional user ID for the page visitor. The system groups apps in restore requests based on `account`. The system also provides the `account` as `login_hint` in the call to your authorization endpoint during re-authentication; for more information, see [`Reauthenticating a person to manage apps`](reauthenticating-a-person-to-manage-apps.md). |
| `appShareURL` | An optional URL to a product landing page for the app on your marketplace website. The operating system populates the value in the Share Sheet when a person touches and holds the app’s icon on the Home Screen. |

The system enforces the following criteria for a webpage that invokes an app download request:

- Your webpage initiates app installation only on a person’s express invocation; in other words, no automatic or indirect app installation. Your webpage can only install an app when a person requests it by tapping a button.
- The origin of the main frame on the webpage containing the installation link must match the domain passed to App Store Connect. The browser app records this information and sends it to MarketplaceKit as covered in [`Enabling alternative distribution app installation in a browser`](enabling-alternative-distribution-app-installation-in-a-browser.md).

> 💡 **Tip**: Some apps that Apple approves for web distribution can also install from the App Store or an alternative app marketplace. You can customize the user experience depending on the source from which a person downloads your app. For more information, see [`Customize your app depending on the installation source`](distributing-your-app-on-an-alternative-marketplace#Customize-your-app-depending-on-the-installation-source.md).

#### Coordinate with the Device From Your Web Server

When a page visitor taps the install button, the system communicates with your web server to validate the request and retrieve the data necessary to perform the installation. If you supply an authentication token in the installation request URL, the system checks if your authentication server authorizes the download. The system then requests an app license from your server, followed by the app itself. For more information, see [`Installing your app from your website`](installing-your-app-from-your-website.md).

#### Report Transactions for the Core Technology Commission

Track any eligible purchases that you offer a person that relate to your app and report them to Apple using tokens provided by MarketplaceKit. For more information, see [`Reporting transactions for the Core Technology Commission`](reporting-transactions-for-core-technology-commission.md).

#### Test Your App During Development

Your app can install over the web only after passing [`Notarization`](https://developer.apple.comhttps://developer.apple.com/support/dma-and-apps-in-the-eu/#notarization-for-ios-apps). To test your app beforehand, set the installation source for development builds. Setting the installation source enables you to simulate a web distribution in production.

Set your target’s Alternative Distribution - Web build setting to `Yes`:

![A screenshot of Xcode with the project AltDistTesting selected in the project navigation sidebar, and the build settings tab open. Under targets, AltDistTesting Tests is selected, under Deployment the setting Alternative Distribution - Web is set to Yes.](https://docs-assets.developer.apple.com/published/b8dd32218b5eb0e36fb1d30bd4873430/distributing-your-app-from-your-website-4%402x.png)

> **Note**: The build setting is `ALTERNATIVE_DISTRIBUTION_WEB`. Open your Xcode project in Xcode 15.4 or later and add the setting manually if it isn’t present.

This build setting overrides the [`current`](appdistributor/current.md) property for development builds to return [`AppDistributor.web`](appdistributor/web.md), which enables you to test any custom code branching your app might do, such as displaying a different image or offering different menu items depending on whether your app installs from the web or a marketplace.

In your scheme’s Run task Options tab, Distribution selection menu, choose Website to simulate installation over the web for runs on device through Xcode.

![A screenshot of Xcode Scheme settings window with Run selected in the sidebar and the options tab open. The Distribution pop-up menu shows the Website option selected.](https://docs-assets.developer.apple.com/published/a556a3fd8a8658b99037065151c288f6/distributing-your-app-from-your-website-5%402x.png)

Similarly, to return [`AppDistributor.web`](appdistributor/web.md) for the [`current`](appdistributor/current.md) distributor in a test plan, choose Website in the Distribution selection menu of your test plan’s configuration.

![A screenshot of Xcode with TestPlan selected in the project navigation sidebar and the Configurations tab open. The Distribution pop-up menu has Website selected.](https://docs-assets.developer.apple.com/published/11323ebc7189f8d8af0a183c8e2d177b/distributing-your-app-from-your-website-6%402x.png)

## See Also

- [Creating an alternative app marketplace](creating-an-alternative-app-marketplace.md)
  Enable the distribution of other third-party apps from within your marketplace app.
- [Distributing your app on an alternative app marketplace](distributing-your-app-on-an-alternative-marketplace.md)
  Design your app for alternative distribution from an alternative app marketplace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/distributing-your-app-from-your-website)*