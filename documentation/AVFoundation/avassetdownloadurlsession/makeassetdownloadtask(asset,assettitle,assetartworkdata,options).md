# makeAssetDownloadTask(asset:assetTitle:assetArtworkData:options:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Creates a download task to download the asset.

**Availability**:
- iOS 10.0+ - Deprecated in 27.0
- iPadOS 10.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use assetDownloadTaskWithConfiguration: instead

## Declaration

```swift
func makeAssetDownloadTask(asset URLAsset: AVURLAsset, assetTitle title: String, assetArtworkData artworkData: Data?, options: [String : Any]? = nil) -> AVAssetDownloadTask?
```

```objc
- (AVAssetDownloadTask *) assetDownloadTaskWithURLAsset:(AVURLAsset *) URLAsset assetTitle:(NSString *) title assetArtworkData:(NSData *) artworkData options:(NSDictionary<NSString *,id> *) options;
```

## Return Value

A new download task.

## Discussion

This method may return `nil` if you call it on an invalidated session.

## Parameters

- `URLAsset`: The HTTP Live Streaming asset to download.
- `title`: A human readable title for this asset in the user’s preferred language. The system displays this value in the usage pane of the Settings app.
- `artworkData`: Optional artwork data for this asset. The system displays the image in the usage pane of the Settings app.
- `options`: Configures custom behavior on the download task. You must provide an options dictionary to download nondefault media selections for HLS assets.

## Topics

### Download option keys
- [let AVAssetDownloadTaskMinimumRequiredMediaBitrateKey: String](../avassetdownloadtaskminimumrequiredmediabitratekey.md)
  A key that indicates the minimum bit rate of the variant to download.
- [let AVAssetDownloadTaskMinimumRequiredPresentationSizeKey: String](../avassetdownloadtaskminimumrequiredpresentationsizekey.md)
  A key that indicates the minimum presentation size of the variant to download.
- [let AVAssetDownloadTaskMediaSelectionKey: String](../avassetdownloadtaskmediaselectionkey.md)
  A key that indicates which media selection to download.
- [let AVAssetDownloadTaskMediaSelectionPrefersMultichannelKey: String](../avassetdownloadtaskmediaselectionprefersmultichannelkey.md)
  A key that indicates whether the task downloads media selections with support for multichannel playback, when available.
- [let AVAssetDownloadTaskPrefersHDRKey: String](../avassetdownloadtaskprefershdrkey.md)
  A key that indicates whether the task downloads HDR instead of SDR video, when available.
- [let AVAssetDownloadTaskPrefersLosslessAudioKey: String](../avassetdownloadtaskpreferslosslessaudiokey.md)
  A key that indicates whether the task downloads media selections in lossless audio format, when available.

## See Also

### Creating download tasks
- [func makeAssetDownloadTask(downloadConfiguration: AVAssetDownloadConfiguration) -> AVAssetDownloadTask](./makeassetdownloadtask%28downloadconfiguration%29.md)
  Creates a download task that uses the specified configuration.
- [class AVAssetDownloadConfiguration](../avassetdownloadconfiguration.md)
  An object that provides the configuration for a download task.
- [func aggregateAssetDownloadTask(with: AVURLAsset, mediaSelections: [AVMediaSelection], assetTitle: String, assetArtworkData: Data?, options: [String : Any]?) -> AVAggregateAssetDownloadTask?](./aggregateassetdownloadtask%28with,mediaselections,assettitle,assetartworkdata,options%29.md)
  Creates a download task to download the asset and media selections.
- [func makeAssetDownloadTask(asset: AVURLAsset, destinationURL: URL, options: [String : Any]?) -> AVAssetDownloadTask?](./makeassetdownloadtask%28asset,destinationurl,options%29.md)
  Creates a download task to download the asset to the indicated location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadurlsession/makeassetdownloadtask(asset:assettitle:assetartworkdata:options:))*