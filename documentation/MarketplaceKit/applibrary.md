# AppLibrary

**Framework**: MarketplaceKit  
**Kind**: class

An object that manages search characteristics, licensing, and the installation of apps.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
final class AppLibrary
```

## Mentions

- [Installing apps from an alternative marketplace](installing-apps-from-an-alternative-marketplace.md)
- [Supplying an install verification token](supplying-an-install-verification-token.md)

#### Overview

Alternative app marketplaces call methods of this class to request the installation of iOS apps from within their app, or to update the license for a specific app that the marketplace distributes. In addition, web browsers that render with [`BrowserEngineKit`](https://developer.apple.com/documentation/BrowserEngineKit) rather than [`WebKit`](https://developer.apple.com/documentation/WebKit) call a method of this class to implement the installation of alternative app marketplaces from a webpage. You can also customize Spotlight search results for the detail using the [`setSearchTerritory(_:)`](applibrary/setsearchterritory(_:).md) method.

iOS ignores calls to this class for apps that lack one of the required entitlements:

- [`com.apple.developer.marketplace.app-installation`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.marketplace.app-installation)
- [`com.apple.developer.browser.app-installation`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.browser.app-installation)

## Topics

### Filtering app searches
- [var searchTerritory: String?](applibrary/searchterritory.md)
  A country code that iOS uses to filter the search results of apps that aren’t available in that country.
- [func setSearchTerritory(String?) async](applibrary/setsearchterritory(_:).md)
  Defines a country code that iOS uses to filter the search results of apps that aren’t available in that country.
### Classes
- [AppLibrary.App](applibrary/app.md)
  Information about an app that someone installs from a marketplace, including its ID and installation status.
### Structures
- [AppLibrary.InstallationRequest](applibrary/installationrequest.md)
### Instance Properties
- [var installedApps: Set<AppLibrary.App>](applibrary/installedapps.md)
- [var installingApps: Set<AppLibrary.App>](applibrary/installingapps.md)
- [var isLoading: Bool](applibrary/isloading.md)
### Instance Methods
- [func app(forAppleItemID: AppleItemID) -> AppLibrary.App](applibrary/app(forappleitemid:).md)
- [func didAuthenticate(account: String) async](applibrary/didauthenticate(account:).md)
  Instructs iOS to reinstall an app after a required reuthorization completes.
- [func requestAppInstallation(AppLibrary.InstallationRequest) async throws](applibrary/requestappinstallation(_:).md)
- [func requestAppInstallation(for: URL, account: String, installVerificationToken: String) async throws](applibrary/requestappinstallation(for:account:installverificationtoken:).md)
- [func requestAppInstallationFromBrowser(for: URL, referrer: URL) async throws](applibrary/requestappinstallationfrombrowser(for:referrer:).md)
  Forwards an app installation request from the developer’s webpage.
- [func requestAppUpdate(AppLibrary.InstallationRequest) async throws](applibrary/requestappupdate(_:).md)
- [func requestAppUpdate(for: URL, account: String, installVerificationToken: String) async throws](applibrary/requestappupdate(for:account:installverificationtoken:).md)
- [func requestLicenseRenewal(appleItemIDs: [UInt64]) async throws](applibrary/requestlicenserenewal(appleitemids:).md)
  Instructs iOS to request an updated app license from your marketplace server for the given app identifier.
### Type Properties
- [static let current: AppLibrary](applibrary/current.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary)*