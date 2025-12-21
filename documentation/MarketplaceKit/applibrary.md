# AppLibrary

**Framework**: MarketplaceKit  
**Kind**: class

A class that represents a catalog of all installed apps, and offers various services for the apps that your marketplace distributes.

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
- [Providing age-rating appropriate content](providing-age-rating-appropriate-content.md)
- [Supplying an install verification token](supplying-an-install-verification-token.md)

#### Overview

Alternative app marketplaces call methods of this class to retrieve the set of currently installed apps, to request the installation of available apps, or to update the license for a specific app. Browser apps that use an alternative browser engine make a call to this class to install alternative app marketplaces from a webpage. You can also customize Spotlight search results and manage age-rating exception requests to install apps with an age rating beyond the maximum allowed for the device.

#### Observe Runtime Changes

The class is observable (through [`SwiftUI`](https://developer.apple.com/documentation/SwiftUI) or the [`Observation`](https://developer.apple.com/documentation/Observation) framework), so you can provide reactive updates when finishing, installing, updating, or loading (see [`isLoading`](applibrary/isloading.md)).

> ❗ **Important**: iOS ignores calls to this class for apps that lack one of the required entitlements: [`com.apple.developer.marketplace.app-installation`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.marketplace.app-installation), or [`com.apple.developer.browser.app-installation`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.browser.app-installation).

## Topics

### Accessing app library and account authorization information
- [static let current: AppLibrary](applibrary/current.md)
  A global accessor for the device’s app library instance.
- [func didAuthenticate(account: String) async](applibrary/didauthenticate(account:).md)
  Instructs iOS to reinstall an app after a required reuthorization completes.
### Managing app installation
- [AppLibrary.App](applibrary/app.md)
  Information about an app that someone installs from a marketplace, including its ID and installation status.
- [AppLibrary.InstallationRequest](applibrary/installationrequest.md)
  A request to install an app distribution package for a given account.
- [var installingApps: Set<AppLibrary.App>](applibrary/installingapps.md)
  The set of apps that are pending installation completion.
- [var isLoading: Bool](applibrary/isloading.md)
  A Boolean value that indicates whether the library is currently loading apps.
- [func requestAppInstallation(AppLibrary.InstallationRequest) async throws](applibrary/requestappinstallation(_:).md)
  Requests the installation of the given app distribution package for the given account.
- [func requestAppInstallationFromBrowser(for: URL, referrer: URL) async throws](applibrary/requestappinstallationfrombrowser(for:referrer:).md)
  Forwards an app installation request from the developer’s webpage.
### Accessing installed apps
- [func app(forAppleItemID: AppleItemID) -> AppLibrary.App](applibrary/app(forappleitemid:).md)
  Provides the app for the given app identifier.
- [var installedApps: Set<AppLibrary.App>](applibrary/installedapps.md)
  The set of apps installed by the alternative app marketplace.
### Checking for age-rating based content restrictions
- [var maximumAllowedAgeRating: Int](applibrary/maximumallowedagerating.md)
  An age rating that specifies the maximum rating set for content on the device.
- [AppLibrary.ExceptionRequest](applibrary/exceptionrequest.md)
  A structure that describes an app that a person requests permission to install.
- [func currentAgeExceptionRequests() async throws -> [AppLibrary.ExceptionRequest]](applibrary/currentageexceptionrequests.md)
  Returns a list of requests to install apps that exceed the maximum allowed age rating for the device.
### Filtering app searches
- [var searchTerritory: String?](applibrary/searchterritory.md)
  A country code that the framework uses to filter the search results of apps that aren’t available in that country.
- [func setSearchTerritory(String?) async](applibrary/setsearchterritory(_:).md)
  Defines a country code that iOS uses to filter the search results of apps that aren’t available in that country.
### Updating apps
- [func requestAppUpdate(AppLibrary.InstallationRequest) async throws](applibrary/requestappupdate(_:).md)
  Requests an app update for the given app distribution package and account information.
- [func requestLicenseRenewal(appleItemIDs: [UInt64]) async throws](applibrary/requestlicenserenewal(appleitemids:).md)
  Instructs iOS to request an updated app license from your marketplace server for the given app identifier.
### Determining device region
- [var catalogRegion: String?](applibrary/catalogregion.md)
  A country code for the device’s current region.
### Deprecated
- [func requestAppInstallation(for: URL, account: String, installVerificationToken: String) async throws](applibrary/requestappinstallation(for:account:installverificationtoken:).md)
- [func requestAppUpdate(for: URL, account: String, installVerificationToken: String) async throws](applibrary/requestappupdate(for:account:installverificationtoken:).md)

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