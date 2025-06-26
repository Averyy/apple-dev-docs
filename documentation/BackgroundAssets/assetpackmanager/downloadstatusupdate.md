# AssetPackManager.DownloadStatusUpdate

**Framework**: Background Assets  
**Kind**: enum

A status update for an ongoing asset-pack download.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum DownloadStatusUpdate
```

#### Overview

An asset pack is available locally only after a [`AssetPackManager.DownloadStatusUpdate.finished(_:)`](assetpackmanager/downloadstatusupdate/finished(_:).md) status update is posted.

## Topics

### Enumeration Cases
- [AssetPackManager.DownloadStatusUpdate.began(_:)](assetpackmanager/downloadstatusupdate/began(_:).md)
  An indication that an asset pack began being downloaded.
- [AssetPackManager.DownloadStatusUpdate.downloading(_:_:)](assetpackmanager/downloadstatusupdate/downloading(_:_:).md)
  An indication that an asset pack is currently being downloaded.
- [AssetPackManager.DownloadStatusUpdate.failed(_:_:)](assetpackmanager/downloadstatusupdate/failed(_:_:).md)
  An indication that an asset pack failed to be downloaded.
- [AssetPackManager.DownloadStatusUpdate.finished(_:)](assetpackmanager/downloadstatusupdate/finished(_:).md)
  An indication that an asset pack finished being downloaded and is now available locally.
- [AssetPackManager.DownloadStatusUpdate.paused(_:)](assetpackmanager/downloadstatusupdate/paused(_:).md)
  An indication that an asset pack paused being downloaded.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/downloadstatusupdate)*