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
  Gets an asynchronous sequence of download-status updates for the asset pack with the specified ID.
- [AssetPackManager.DownloadStatusUpdate](assetpackmanager/downloadstatusupdate.md)
  Statuses of an asset-pack download.
- [func status(ofAssetPackWithID: String) async throws -> AssetPack.Status](assetpackmanager/status(ofassetpackwithid:).md)
  Returns an asynchronous sequence of download-status updates for the specified asset pack.
### Accessing asset packs
- [var allAssetPacks: Set<AssetPack>](assetpackmanager/allassetpacks.md)
  The asset packs that are available to download.
- [func assetPack(withID: String) async throws -> AssetPack](assetpackmanager/assetpack(withid:).md)
  Returns the asset pack with the given ID.
- [func contents(at: FilePath, searchingInAssetPackWithID: String?, options: Data.ReadingOptions) throws -> Data](assetpackmanager/contents(at:searchinginassetpackwithid:options:).md)
  Returns the contents of an asset file at the specified relative path.
- [func descriptor(for: FilePath, searchingInAssetPackWithID: String?) throws -> FileDescriptor](assetpackmanager/descriptor(for:searchinginassetpackwithid:).md)
  Opens and returns a file descriptor for an asset file at the specified relative path.
- [func url(for: FilePath) throws -> URL](assetpackmanager/url(for:).md)
  Returns a URL for the specified relative path.
### Managing asset packs
- [func checkForUpdates() async throws -> (updatingIDs: Set<String>, removedIDs: Set<String>)](assetpackmanager/checkforupdates.md)
  Gets the latest asset-pack information from the server, updates outdated asset packs, and removes obsolete asset packs.
- [func ensureLocalAvailability(of: AssetPack) async throws](assetpackmanager/ensurelocalavailability(of:).md)
  Ensures that the specified asset pack be available locally.
- [func remove(assetPackWithID: String) async throws](assetpackmanager/remove(assetpackwithid:).md)
  Removes the specified asset pack from the device.

## Relationships

### Conforms To
- [Actor](../Swift/Actor.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AssetPack](assetpack.md)
  An archive of assets that the system downloads together.
- [protocol ManagedDownloaderExtension](manageddownloaderextension.md)
  An app extension that uses the system implementation to schedule asset-pack downloads automatically.
- [BAAppGroupID](../BundleResources/Information-Property-List/BAAppGroupID.md)
  The app group identifier that you share between your app and the extension that uses asset packs.
- [BAHasManagedAssetPacks](../BundleResources/Information-Property-List/BAHasManagedAssetPacks.md)
  A Boolean value that indicates whether you let the system automatically manage your asset packs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager)*