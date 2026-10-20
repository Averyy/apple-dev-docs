# AppLibrary.App

**Framework**: MarketplaceKit  
**Kind**: class  
**Role**: Class

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

- [Providing age-rating appropriate content](../providing-age-rating-appropriate-content.md)

## Topics

### Inspecting an app’s version and account
- [var installedMetadata: AppLibrary.App.Metadata?](./app/installedmetadata.md)
  The app version and the account that’s installing the app
- [AppLibrary.App.Metadata](./app/metadata.md)
  Information about an app’s version and account.
### Inspecting app installation and update status
- [var installation: AppLibrary.App.Installation?](./app/installation-swift.property.md)
  The progress of the app’s installation.
- [AppLibrary.App.Installation](./app/installation-swift.struct.md)
  A structure that provides progress information for a specific app installation.
- [var isInstalled: Bool](./app/isinstalled.md)
  A Boolean value that indicates whether the app’s installation is complete.
- [var isInstalling: Bool](./app/isinstalling.md)
  A Boolean value that indicates whether the app’s installation is in progress.
- [var isUpdating: Bool](./app/isupdating.md)
  A Boolean value that indicates whether an app’s update is in progress.
- [var installationError: MarketplaceKitError?](./app/installationerror.md)
  An error that occurs during the installation of an app that resides on a marketplace.
### Requesting installation approval
- [func presentAgeExceptionApproveInPersonSheet() async throws](./app/presentageexceptionapproveinpersonsheet%28%29.md)
  Presents a sheet that enables a parent or guardian to approve age-exception requests.
### Requesting app deletion
- [func requestDeletion(in: UIWindowScene) async throws](./app/requestdeletion%28in%29.md)
  Prompts the person to delete the app.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Identifiable](../../Swift/identifiable.md)
- [Observable](../../Observation/observable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Installing apps as a marketplace
- [AppLibrary.InstallationRequest](./installationrequest.md)
  A request to install an app distribution package for a given account.
- [var installingApps: Set<AppLibrary.App>](./installingapps.md)
  The set of apps that are pending installation completion.
- [var isLoading: Bool](./isloading.md)
  A Boolean value that indicates whether the library is currently loading apps.
- [func requestAppInstallation(AppLibrary.InstallationRequest) async throws](./requestappinstallation%28_%29.md)
  Requests the installation of the given app distribution package for the given account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/app)*