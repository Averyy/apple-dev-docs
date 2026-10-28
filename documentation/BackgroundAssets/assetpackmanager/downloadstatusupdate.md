# AssetPackManager.DownloadStatusUpdate

**Framework**: Background Assets  
**Kind**: enum  
**Role**: Enumeration

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

## Overview

An asset pack is available locally only after a [`AssetPackManager.DownloadStatusUpdate.finished(_:)`](./downloadstatusupdate/finished%28_%29.md) status update is posted.

## Topics

### Tracking downloads
- [AssetPackManager.DownloadStatusUpdate.began(_:)](./downloadstatusupdate/began%28_%29.md)
  A status update that indicates that the download began or resumed after being paused.
- [AssetPackManager.DownloadStatusUpdate.downloading(_:_:)](./downloadstatusupdate/downloading%28_,_%29.md)
  A status update that indicates that the download is in progress.
- [AssetPackManager.DownloadStatusUpdate.paused(_:)](./downloadstatusupdate/paused%28_%29.md)
  A status update that indicates that the download paused.
- [AssetPackManager.DownloadStatusUpdate.finished(_:)](./downloadstatusupdate/finished%28_%29.md)
  A status update that indicates that the download completed and that the asset pack is available locally.
- [AssetPackManager.DownloadStatusUpdate.failed(_:_:)](./downloadstatusupdate/failed%28_,_%29.md)
  A status update that indicates that the download failed.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Tracking downloads
- [let statusUpdates: some Sendable & AsyncSequence<AssetPackManager.DownloadStatusUpdate, Never>](./statusupdates.md)
  An asynchronous sequence of download-status updates for all asset packs.
- [func statusUpdates(forAssetPackWithID: String) -> some Sendable & AsyncSequence<AssetPackManager.DownloadStatusUpdate, Never>
](./statusupdates%28forassetpackwithid%29.md)
  Returns an asynchronous sequence of download-status updates for the asset pack with the specified ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/downloadstatusupdate)*