# makeAssetDownloadTask(downloadConfiguration:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Creates a download task that uses the specified configuration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func makeAssetDownloadTask(downloadConfiguration: AVAssetDownloadConfiguration) -> AVAssetDownloadTask
```

```objc
- (AVAssetDownloadTask *) assetDownloadTaskWithConfiguration:(AVAssetDownloadConfiguration *) downloadConfiguration;
```

## Return Value

A new download task.

## Discussion

This method raises an exception if you call it on an invalidated session.

## Parameters

- `downloadConfiguration`: The configuration that the task uses.

## See Also

### Creating download tasks
- [class AVAssetDownloadConfiguration](../avassetdownloadconfiguration.md)
  An object that provides the configuration for a download task.
- [func makeAssetDownloadTask(asset: AVURLAsset, assetTitle: String, assetArtworkData: Data?, options: [String : Any]?) -> AVAssetDownloadTask?](./makeassetdownloadtask%28asset,assettitle,assetartworkdata,options%29.md)
  Creates a download task to download the asset.
- [func aggregateAssetDownloadTask(with: AVURLAsset, mediaSelections: [AVMediaSelection], assetTitle: String, assetArtworkData: Data?, options: [String : Any]?) -> AVAggregateAssetDownloadTask?](./aggregateassetdownloadtask%28with,mediaselections,assettitle,assetartworkdata,options%29.md)
  Creates a download task to download the asset and media selections.
- [func makeAssetDownloadTask(asset: AVURLAsset, destinationURL: URL, options: [String : Any]?) -> AVAssetDownloadTask?](./makeassetdownloadtask%28asset,destinationurl,options%29.md)
  Creates a download task to download the asset to the indicated location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadurlsession/makeassetdownloadtask(downloadconfiguration:))*