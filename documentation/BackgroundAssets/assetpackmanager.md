# AssetPackManager

**Framework**: Background Assets  
**Kind**: class

An actor that manages asset packs.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
actor AssetPackManager
```

#### Overview

The first time that your code refers to the shared manager, Background Assets considers that your app is opting into automatic system management of your asset packs.

> ❗ **Important**: When using the asset-pack manager, make sure that you also adopt the corresponding managed extension protocol, [`ManagedDownloaderExtension`](manageddownloaderextension.md). Not doing so is a programmer error.

## Topics

### Instance Properties
- [var allAssetPacks: Set<AssetPack>](assetpackmanager/allassetpacks.md)
  The asset packs that are available to download.
- [let statusUpdates: some Sendable & AsyncSequence<AssetPackManager.DownloadStatusUpdate, Never>](assetpackmanager/statusupdates.md)
  An asynchronous sequence of download-status updates for all asset packs.
### Instance Methods
- [func assetPack(withID: String) async throws -> AssetPack](assetpackmanager/assetpack(withid:).md)
  Gets a representation of an asset pack.
- [func checkForUpdates() async throws -> (updatingIDs: Set<String>, removedIDs: Set<String>)](assetpackmanager/checkforupdates.md)
  Gets the latest asset-pack information from the server, updates outdated asset packs, and removes obsolete asset packs.
- [func contents(at: FilePath, searchingInAssetPackWithID: String?, options: Data.ReadingOptions) throws -> Data](assetpackmanager/contents(at:searchinginassetpackwithid:options:).md)
  Gets the contents of an asset file at the specified relative path.
- [func descriptor(for: FilePath, searchingInAssetPackWithID: String?) throws -> FileDescriptor](assetpackmanager/descriptor(for:searchinginassetpackwithid:).md)
  Opens a file descriptor for the specified relative path.
- [func ensureLocalAvailability(of: AssetPack) async throws](assetpackmanager/ensurelocalavailability(of:).md)
  Ensures that the specified asset pack be available locally.
- [func remove(assetPackWithID: String) async throws](assetpackmanager/remove(assetpackwithid:).md)
  Removes the downloaded asset pack with the specified ID.
- [func status(ofAssetPackWithID: String) async throws -> AssetPack.Status](assetpackmanager/status(ofassetpackwithid:).md)
  Gets the status of the asset pack with the specified ID.
- [func statusUpdates(forAssetPackWithID: String) -> some Sendable & AsyncSequence<AssetPackManager.DownloadStatusUpdate, Never>
](assetpackmanager/statusupdates(forassetpackwithid:).md)
  Gets an asynchronous sequence of download-status updates for the asset pack with the specified ID.
- [func url(for: FilePath) throws -> URL](assetpackmanager/url(for:).md)
  Gets the URL for the specified relative path.
### Type Properties
- [static let shared: AssetPackManager](assetpackmanager/shared.md)
  The shared manager.
### Enumerations
- [AssetPackManager.DownloadStatusUpdate](assetpackmanager/downloadstatusupdate.md)
  A status update for an ongoing asset-pack download.

## Relationships

### Conforms To
- [Actor](../Swift/Actor.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager)*