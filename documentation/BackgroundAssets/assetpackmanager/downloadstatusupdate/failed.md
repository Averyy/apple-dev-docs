# AssetPackManager.DownloadStatusUpdate.failed(_:_:)

**Framework**: Background Assets  
**Kind**: case

A status update that indicates that the download failed.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case failed(AssetPack, any Error)
```

## See Also

- [AssetPackManager.DownloadStatusUpdate.began(_:)](assetpackmanager/downloadstatusupdate/began(_:).md)
  A status update that indicates that the download began or resumed after being paused.
- [AssetPackManager.DownloadStatusUpdate.downloading(_:_:)](assetpackmanager/downloadstatusupdate/downloading(_:_:).md)
  A status update that indicates that the download is in progress.
- [AssetPackManager.DownloadStatusUpdate.paused(_:)](assetpackmanager/downloadstatusupdate/paused(_:).md)
  A status update that indicates that the download paused.
- [AssetPackManager.DownloadStatusUpdate.finished(_:)](assetpackmanager/downloadstatusupdate/finished(_:).md)
  A status update that indicates that the download completed and that the asset pack is available locally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/downloadstatusupdate/failed(_:_:))*