# makeAssetDownloadTask(asset:destinationURL:options:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Creates a download task to download the asset to the indicated location.

**Availability**:
- iOS 9.0+ - Deprecated in 10.0
- iPadOS 9.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`makeAssetDownloadTask(asset:assetTitle:assetArtworkData:options:)`](./makeassetdownloadtask%28asset,assettitle,assetartworkdata,options%29.md) instead.

## Declaration

```swift
func makeAssetDownloadTask(asset URLAsset: AVURLAsset, destinationURL: URL, options: [String : Any]? = nil) -> AVAssetDownloadTask?
```

```objc
- (AVAssetDownloadTask *) assetDownloadTaskWithURLAsset:(AVURLAsset *) URLAsset destinationURL:(NSURL *) destinationURL options:(NSDictionary<NSString *,id> *) options;
```

## Return Value

A new download task.

## Parameters

- `URLAsset`: The asset to download to the local device.
- `destinationURL`: The local file URL to download the asset to.
- `options`: Configures non-default behavior for the download task. To download nondefault media selections, you must indicate download options.

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
- [func makeAssetDownloadTask(asset: AVURLAsset, assetTitle: String, assetArtworkData: Data?, options: [String : Any]?) -> AVAssetDownloadTask?](./makeassetdownloadtask%28asset,assettitle,assetartworkdata,options%29.md)
  Creates a download task to download the asset.
- [func aggregateAssetDownloadTask(with: AVURLAsset, mediaSelections: [AVMediaSelection], assetTitle: String, assetArtworkData: Data?, options: [String : Any]?) -> AVAggregateAssetDownloadTask?](./aggregateassetdownloadtask%28with,mediaselections,assettitle,assetartworkdata,options%29.md)
  Creates a download task to download the asset and media selections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadurlsession/makeassetdownloadtask(asset:destinationurl:options:))*