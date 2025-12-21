# AppLibrary.App

**Framework**: MarketplaceKit  
**Kind**: class

Information about an app that someone installs from a marketplace, including its ID and installation status.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
final class App
```

## Mentions

- [Providing age-rating appropriate content](providing-age-rating-appropriate-content.md)

## Topics

### Inspecting an app’s version and account
- [var installedMetadata: AppLibrary.App.Metadata?](applibrary/app/installedmetadata.md)
  The app version and the account that’s installing the app
- [AppLibrary.App.Metadata](applibrary/app/metadata.md)
  Information about an app’s version and account.
### Inspecting app installation and update status
- [var installation: AppLibrary.App.Installation?](applibrary/app/installation-swift.property.md)
  The progress of the app’s installation.
- [AppLibrary.App.Installation](applibrary/app/installation-swift.struct.md)
  A structure that provides progress information for a specific app installation.
- [var isInstalled: Bool](applibrary/app/isinstalled.md)
  A Boolean value that indicates whether the app’s installation is complete.
- [var isInstalling: Bool](applibrary/app/isinstalling.md)
  A Boolean value that indicates whether the app’s installation is in progress.
- [var isUpdating: Bool](applibrary/app/isupdating.md)
  A Boolean value that indicates whether an app’s update is in progress.
- [var installationError: MarketplaceKitError?](applibrary/app/installationerror.md)
  An error that occurs during the installation of an app that resides on a marketplace.
### Requesting installation approval
- [func presentAgeExceptionApproveInPersonSheet() async throws](applibrary/app/presentageexceptionapproveinpersonsheet.md)
  Presents a sheet that enables a parent or guardian to approve age-exception requests.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/app)*