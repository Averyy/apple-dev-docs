# AssetPackManager

**Framework**: Background Assets  
**Kind**: class

An actor that manages asset packs.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
actor AssetPackManager
```

## Mentions

- [Reducing download and storage demands with localized asset packs](reducing-download-and-storage-demands-with-localized-asset-packs.md)

#### Overview

The first time that your code refers to the shared manager, Background Assets considers that your app is opting into automatic system management of your asset packs.

> ❗ **Important**: When using the asset-pack manager, make sure that you also adopt the corresponding managed extension protocol, [`ManagedDownloaderExtension`](manageddownloaderextension.md) (for self-hosted asset packs) or `StoreDownloaderExtension` from StoreKit (for Apple-hosted asset packs). Not doing so is a programmer error.

## Topics

### Getting the shared manager
- [static let shared: AssetPackManager](assetpackmanager/shared.md)
  The shared manager.
### Tracking downloads
- [let statusUpdates: some Sendable & AsyncSequence<AssetPackManager.DownloadStatusUpdate, Never>](assetpackmanager/statusupdates.md)
  An asynchronous sequence of download-status updates for all asset packs.
- [func statusUpdates(forAssetPackWithID: String) -> some Sendable & AsyncSequence<AssetPackManager.DownloadStatusUpdate, Never>
](assetpackmanager/statusupdates(forassetpackwithid:).md)
  Returns an asynchronous sequence of download-status updates for the asset pack with the specified ID.
- [AssetPackManager.DownloadStatusUpdate](assetpackmanager/downloadstatusupdate.md)
  Statuses of an asset-pack download.
### Accessing asset packs
- [var manifest: AssetPackManifest](assetpackmanager/manifest.md)
  The manifest of asset packs that are available to download.
- [struct AssetPackManifest](assetpackmanifest.md)
  A manifest of asset packs that are available to download.
- [var allAssetPacks: Set<AssetPack>](assetpackmanager/allassetpacks.md)
  The asset packs that are available to download.
- [func assetPack(withID: String) async throws -> AssetPack](assetpackmanager/assetpack(withid:).md)
  Returns the asset pack with the given ID.
### Accessing asset contents
- [func contents(at: FilePath, searchingInAssetPackWithID: String?, options: Data.ReadingOptions) throws -> Data](assetpackmanager/contents(at:searchinginassetpackwithid:options:).md)
  Returns the contents of an asset file at the specified relative path.
- [func contents(at: FilePath, asLocalizedFor: Locale.Language, options: Data.ReadingOptions) throws -> Data](assetpackmanager/contents(at:aslocalizedfor:options:).md)
  Returns the contents of a localized asset file at the specified relative path.
- [func descriptor(for: FilePath, searchingInAssetPackWithID: String?) throws -> FileDescriptor](assetpackmanager/descriptor(for:searchinginassetpackwithid:).md)
  Opens and returns a file descriptor for an asset file at the specified relative path.
- [func descriptor(for: FilePath, asLocalizedFor: Locale.Language) throws -> FileDescriptor](assetpackmanager/descriptor(for:aslocalizedfor:).md)
  Opens and returns a file descriptor for a localized asset file at the specified relative path.
- [func url(for: FilePath) throws -> URL](assetpackmanager/url(for:).md)
  Returns a URL for the specified relative path.
- [func url(for: FilePath, asLocalizedFor: Locale.Language) throws -> URL](assetpackmanager/url(for:aslocalizedfor:).md)
  Returns a URL for the specified relative path.
### Managing asset packs
- [func checkForUpdates() async throws -> (updatingIDs: Set<String>, removedIDs: Set<String>)](assetpackmanager/checkforupdates.md)
  Gets the latest asset-pack information from the server, updates outdated asset packs, and removes obsolete asset packs.
- [func ensureLocalAvailability(of: AssetPack, requireLatestVersion: Bool) async throws](assetpackmanager/ensurelocalavailability(of:requirelatestversion:).md)
  Ensures that an asset pack is available locally, performing a download if necessary.
- [func ensureLocalAvailability(of: Set<AssetPack>, requireLatestVersions: Bool) async throws](assetpackmanager/ensurelocalavailability(of:requirelatestversions:).md)
  Ensures the specified asset packs are available locally, performing a batch download if necessary.
- [func assetPackIsAvailableLocally(withID: String) -> Bool](assetpackmanager/assetpackisavailablelocally(withid:).md)
  Checks whether an asset pack is available locally.
- [func status(relativeTo: AssetPack) async throws -> AssetPack.Status](assetpackmanager/status(relativeto:).md)
  Checks the current status relative to a particular asset pack.
- [func localStatus(ofAssetPackWithID: String) async -> AssetPack.Status](assetpackmanager/localstatus(ofassetpackwithid:).md)
  Checks an asset pack’s local status.
- [AssetPack.Status](assetpack/status.md)
  The status of an asset pack.
- [func remove(assetPackWithID: String) async throws](assetpackmanager/remove(assetpackwithid:).md)
  Removes the specified asset pack from the device.
- [func status(ofAssetPackWithID: String) async throws -> AssetPack.Status](assetpackmanager/status(ofassetpackwithid:).md)
  Checks an asset pack’s status.
- [func ensureLocalAvailability(of: AssetPack) async throws](assetpackmanager/ensurelocalavailability(of:).md)
  Ensures that the specified asset pack is available locally, performing a download if necessary.
### Inspecting language support
- [var locallyAvailableLanguages: [Locale.Language]](assetpackmanager/locallyavailablelanguages.md)
  The languages used by asset packs that are localized and are available locally.
- [var resolvedLanguage: Locale.Language?](assetpackmanager/resolvedlanguage.md)
  The language that best matches current preferences and for which the system automatically makes localized asset packs available locally.
- [func reconcilePreferredLanguages() async throws](assetpackmanager/reconcilepreferredlanguages.md)
  Reconciles the set of locally available asset packs with the current preferred languages.
### Handling errors
- [AssetPackManager.LocalAvailabilityError](assetpackmanager/localavailabilityerror.md)
  An error that provides information about local asset pack availability, distinguishing between successes and failures.

## Relationships

### Conforms To
- [Actor](../swift/actor.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct AssetPack](assetpack.md)
  An archive of assets that the system downloads together.
- [struct AssetPackManifest](assetpackmanifest.md)
  A manifest of asset packs that are available to download.
- [protocol ManagedDownloaderExtension](manageddownloaderextension.md)
  An app extension that uses the system implementation to schedule asset-pack downloads automatically.
- [BAAppGroupID](../bundleresources/information-property-list/baappgroupid.md)
  The app group identifier that you share between your app and the extension that uses asset packs.
- [BAHasManagedAssetPacks](../bundleresources/information-property-list/bahasmanagedassetpacks.md)
  A Boolean value that indicates whether you let the system automatically manage your asset packs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager)*