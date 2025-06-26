# MarketplaceKitURIScheme

**Framework**: MarketplaceKit  
**Kind**: var

A URI scheme that defines an alternative distribution app installation link.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
let MarketplaceKitURIScheme: String
```

## Mentions

- [Installing your app from your website](installing-your-app-from-your-website.md)
- [Enabling alternative distribution app installation in a browser](enabling-alternative-distribution-app-installation-in-a-browser.md)
- [Installing apps from an alternative marketplace](installing-apps-from-an-alternative-marketplace.md)
- [Distributing your app from your website](distributing-your-app-from-your-website.md)
- [Ingesting an alternative distribution package](ingesting-an-alternative-distribution-package.md)

#### Discussion

This installation scheme defines how your webpage requests the installation of your app. For example, assign a URL with the following scheme to a Download button on your page:

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
| `alternativeDistributionPackage` | Your app’s alternative distribution package in the assembled format described in [`Ingesting an alternative distribution package`](ingesting-an-alternative-distribution-package.md). |
| `installVerificationToken` | A required JSON web signature (JWS). For more information, see [`Supplying an install verification token`](supplying-an-install-verification-token.md). |
| `token` | An optional authentication token to include if downloads require authorization. iOS sends the token back to your token endpoint to reference this request. The value is free-form, and can contain any information at your discretion, such as an id that identifies the customer. |
| `account` | An optional user ID for the page visitor. iOS groups apps in restore requests based on `account`. iOS also provides the `account` as `login_hint` for the authorization call during interactive re-authentication; for more information, see [`Reauthenticating a person to manage apps`](reauthenticating-a-person-to-manage-apps.md). |
| `appShareURL` | An optional URL to a product landing page for the app on your marketplace website. The operating system populates the value in the Share Sheet when a person touches and holds the app’s icon on the Home Screen. |

Web browsers recognize the scheme and hand off the installation request to [`MarketplaceKit`](MarketplaceKit.md). For more information, see [`Installing your app from your website`](installing-your-app-from-your-website.md).

#### Setting the Alternative Distribution Package Parameter

The fully qualified domain in the `alternateDistributionPackage` value needs to match the fully qualified domain of the , that is, the page that contains the `marketplace-kit://` link. This domain also needs to match the domain you supply to App Store Connect. For more information, see [`Alternative Distribution Domains`](https://developer.apple.com/documentation/AppStoreConnectAPI/alternative-distribution-domains). For example:

> **Note**: To allow installation, the web browser also needs to support the app installation URL scheme. If you develop a browser app, see [`Enabling alternative distribution app installation in a browser`](enabling-alternative-distribution-app-installation-in-a-browser.md) for more information.

## See Also

- [class AppLibrary](applibrary.md)
  An object that manages search characteristics, licensing, and the installation of apps.
- [struct AppVersion](appversion.md)
  Information that describes an app, including its identifier and version number.
- [struct AutomaticUpdate](automaticupdate.md)
  Information that describes an app that’s available for update, including a download URL.
- [struct InstallRequirements](installrequirements.md)
  An app’s installation criteria for a device.
- [typealias AppleItemID](appleitemid.md)
  An identifier that represents an app.
- [typealias AppleVersionID](appleversionid.md)
  An identifier that represents a single app version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/marketplacekiturischeme)*