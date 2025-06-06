# MarketplaceKit

**Framework**: MarketplaceKit  
**Kind**: module

Create an alternative app marketplace, distribute your app on an alternative app marketplace, or distribute your app from your website.

**Availability**:
- iOS 17.4+
- iPadOS 18.0+

## Mentions

- [Enabling alternative distribution app installation in a browser](enabling-alternative-distribution-app-installation-in-a-browser.md)
- [Installing apps from an alternative marketplace](installing-apps-from-an-alternative-marketplace.md)
- [Installing your app from your website](installing-your-app-from-your-website.md)
- [Creating an alternative app marketplace](creating-an-alternative-app-marketplace.md)
- [Reauthenticating a person to manage apps](reauthenticating-a-person-to-manage-apps.md)

#### Overview

An  is an app from which someone can install apps from other developers, as an alternative to the App Store. MarketplaceKit enables alternative app marketplaces to install the apps they distribute to peoples’ devices. The framework also supports features that compose a quality browsing and installation experience, such as Spotlight Search and App Thinning. With the framework, you can manage existing app installations, convey download progress, update app licensing, and customize app search behavior.

In addition to alternative app marketplaces, this framework also serves:

- Web browsers, specifically by requesting app installation on a webpage.
- Apps that install from an alternative app marketplace or webpage, by determining the installation source at runtime. This allows an app to branch its functionality depending on the installation source.

![Three diagrams that describe the different use cases for MarketplaceKit. From left to right: installing an app from a webpage, installing an app from a alternative app marketplace, and determining an app’s installation source at runtime.](https://docs-assets.developer.apple.com/published/299f1a299648bff2fe696ad51c4bfd02/marketplacekit-hero%402x.png)

> ❗ **Important**: To request the marketplace entitlement, see [`Getting started as an alternative app marketplace in the European Union`](https://developer.apple.comhttps://developer.apple.com/support/alternative-app-marketplace-in-the-eu/). To apply to distribute your app from your website, see [`Getting started with Web Distribution in the EU`](https://developer.apple.comhttps://developer.apple.com/support/web-distribution-eu/).

To request the marketplace entitlement, see [`Getting started as an alternative app marketplace in the European Union`](https://developer.apple.comhttps://developer.apple.com/support/alternative-app-marketplace-in-the-eu/). To apply to distribute your app from your website, see [`Getting started with Web Distribution in the EU`](https://developer.apple.comhttps://developer.apple.com/support/web-distribution-eu/).

## Topics

### Essentials
- [Creating an alternative app marketplace](creating-an-alternative-app-marketplace.md)
  Enable the distribution of other third-party apps from within your marketplace app.
- [Distributing your app from your website](distributing-your-app-from-your-website.md)
  Configure your app and website to enable people to install your app on their devices from your website.
- [Distributing your app on an alternative app marketplace](distributing-your-app-on-an-alternative-marketplace.md)
  Design your app for alternative distribution from an alternative app marketplace.
### Web services
- [Processing alternative app marketplace notifications](processing-alternative-marketplace-notifications.md)
  Manage the addition and removal of apps available on your alternative marketplace.
- [Ingesting an alternative distribution package](ingesting-an-alternative-distribution-package.md)
  Process an available app version from App Store Connect and store it for download from your server.
- [Installing your app from your website](installing-your-app-from-your-website.md)
  Manage the installation of an app that you develop and distribute through your website.
- [Installing apps from an alternative marketplace](installing-apps-from-an-alternative-marketplace.md)
  Manage the installation of apps that developers distribute from your marketplace app.
- [Supplying an install verification token](supplying-an-install-verification-token.md)
  Support the installation of alternative distribution apps by creating signed JSON web tokens.
### Authorization
- [Reauthenticating a person to manage apps](reauthenticating-a-person-to-manage-apps.md)
  Renew your app’s authorization when an app needs updating or when a device restores from backup.
- [com.apple.developer.marketplace.app-installation](../BundleResources/Entitlements/com.apple.developer.marketplace.app-installation.md)
  The entitlement that enables an app to vend other apps as an alternative app marketplace.
- [com.apple.developer.browser.app-installation](../BundleResources/Entitlements/com.apple.developer.browser.app-installation.md)
  The entitlement that enables a browser to install alternative-distribution apps from a website.
- [App License Delivery SDK](../AppLicenseDeliverySDK/AppLicenseDeliverySDK.md)
  Secure the installation of alternative distribution apps on iOS or iPadOS devices by vending licenses from your web server.
### Browser support
- [Enabling alternative distribution app installation in a browser](enabling-alternative-distribution-app-installation-in-a-browser.md)
  Add support for browser apps to install alternative distribution apps from websites.
### App management
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
- [let MarketplaceKitURIScheme: String](marketplacekiturischeme.md)
  A URI scheme that defines an alternative distribution app installation link.
### Background services
- [protocol MarketplaceExtension](marketplaceextension.md)
  An extension that facilitates authentication, installation, and launching a marketplace with deep links.
- [protocol MarketplaceExtensionConfiguration](marketplaceextensionconfiguration.md)
  The type for a marketplace extension’s configuration object.
### App distribution UI
- [class ActionButton](actionbutton.md)
  A user-interface element that enables a person to install, update, or launch apps by tapping the element.
- [struct InstallMetadata](installmetadata.md)
  Information about a specific app to install or update and the person who initiates it.
- [struct InstallConfiguration](installconfiguration.md)
  Information that describes a requested app installation or app update.
- [enum InstallConfirmationResult](installconfirmationresult.md)
  Options that indicate whether the installation of an app proceeds when a person interacts with an app installation button.
- [struct BatchInstallConfiguration](batchinstallconfiguration.md)
  Information that describes multiple app installations or app updates.
- [enum BatchInstallConfirmationResult](batchinstallconfirmationresult.md)
  Options that indicate whether the installation of multiple apps proceeds when a person interacts with an app installation button.
- [enum MarketplaceDisplayOption](marketplacedisplayoption.md)
  The kinds of deep links that the operating system makes into your marketplace.
- [protocol MarketplaceSceneDelegate](marketplacescenedelegate.md)
  A delegate that handles deep link requests into your marketplace app.
### Installation sources
- [enum AppDistributor](appdistributor.md)
  Options that describe the marketplace from which the app installs.
### Errors
- [enum MarketplaceKitError](marketplacekiterror.md)
  Errors that can occur in the marketplace workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/MarketplaceKit)*