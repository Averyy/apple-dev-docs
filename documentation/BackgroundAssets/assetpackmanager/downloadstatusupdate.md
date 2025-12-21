# AssetPackManager.DownloadStatusUpdate

**Framework**: Background Assets  
**Kind**: enum

Statuses of an asset-pack download.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum DownloadStatusUpdate
```

#### Overview

An asset pack is available locally only after a [`AssetPackManager.DownloadStatusUpdate.finished(_:)`](assetpackmanager/downloadstatusupdate/finished(_:).md) status update is posted.

## Topics

### Tracking downloads
- [AssetPackManager.DownloadStatusUpdate.began(_:)](assetpackmanager/downloadstatusupdate/began(_:).md)
  A status update that indicates that the download began or resumed after being paused.
- [AssetPackManager.DownloadStatusUpdate.downloading(_:_:)](assetpackmanager/downloadstatusupdate/downloading(_:_:).md)
  A status update that indicates that the download is in progress.
- [AssetPackManager.DownloadStatusUpdate.paused(_:)](assetpackmanager/downloadstatusupdate/paused(_:).md)
  A status update that indicates that the download paused.
- [AssetPackManager.DownloadStatusUpdate.finished(_:)](assetpackmanager/downloadstatusupdate/finished(_:).md)
  A status update that indicates that the download completed and that the asset pack is available locally.
- [AssetPackManager.DownloadStatusUpdate.failed(_:_:)](assetpackmanager/downloadstatusupdate/failed(_:_:).md)
  A status update that indicates that the download failed.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let statusUpdates: some Sendable & AsyncSequence<AssetPackManager.DownloadStatusUpdate, Never>](assetpackmanager/statusupdates.md)
  An asynchronous sequence of download-status updates for all asset packs.
- [func statusUpdates(forAssetPackWithID: String) -> some Sendable & AsyncSequence<AssetPackManager.DownloadStatusUpdate, Never>
](assetpackmanager/statusupdates(forassetpackwithid:).md)
  Gets an asynchronous sequence of download-status updates for the asset pack with the specified ID.
- [func status(ofAssetPackWithID: String) async throws -> AssetPack.Status](assetpackmanager/status(ofassetpackwithid:).md)
  Returns an asynchronous sequence of download-status updates for the specified asset pack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/downloadstatusupdate)*