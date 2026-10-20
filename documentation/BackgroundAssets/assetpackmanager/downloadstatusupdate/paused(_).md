# AssetPackManager.DownloadStatusUpdate.paused(_:)

**Framework**: Background Assets  
**Kind**: case  
**Role**: Case

A status update that indicates that the download paused.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case paused(AssetPack)
```

## See Also

### Tracking downloads
- [AssetPackManager.DownloadStatusUpdate.began(_:)](./began%28_%29.md)
  A status update that indicates that the download began or resumed after being paused.
- [AssetPackManager.DownloadStatusUpdate.downloading(_:_:)](./downloading%28_,_%29.md)
  A status update that indicates that the download is in progress.
- [AssetPackManager.DownloadStatusUpdate.finished(_:)](./finished%28_%29.md)
  A status update that indicates that the download completed and that the asset pack is available locally.
- [AssetPackManager.DownloadStatusUpdate.failed(_:_:)](./failed%28_,_%29.md)
  A status update that indicates that the download failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/downloadstatusupdate/paused(_:))*