# aggregateAssetDownloadTask(with:mediaSelections:assetTitle:assetArtworkData:options:)

**Framework**: AVFoundation  
**Kind**: method

Creates a download task to download the asset and media selections.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func aggregateAssetDownloadTask(with URLAsset: AVURLAsset, mediaSelections: [AVMediaSelection], assetTitle title: String, assetArtworkData artworkData: Data?, options: [String : Any]? = nil) -> AVAggregateAssetDownloadTask?
```

#### Return Value

An aggregate asset download task.

#### Discussion

This method may return `nil` if you call it on an invalidated session.

## Parameters

- `URLAsset`: The asset to download to the local device.
- `mediaSelections`: An array of media selections to download.
- `title`: A human readable title for this asset in the user’s preferred language. The system displays this value in the usage pane of the Settings app.
- `artworkData`: Optional artwork data for this asset. The system displays the image in the usage pane of the Settings app.
- `options`: Configures custom behavior on the download task.

## Topics

### Download Option Keys
- [let AVAssetDownloadTaskMinimumRequiredMediaBitrateKey: String](avassetdownloadtaskminimumrequiredmediabitratekey.md)
  A key that indicates the minimum bit rate of the variant to download.
- [let AVAssetDownloadTaskMinimumRequiredPresentationSizeKey: String](avassetdownloadtaskminimumrequiredpresentationsizekey.md)
  A key that indicates the minimum presentation size of the variant to download.
- [let AVAssetDownloadTaskMediaSelectionKey: String](avassetdownloadtaskmediaselectionkey.md)
  A key that indicates which media selection to download.
- [let AVAssetDownloadTaskMediaSelectionPrefersMultichannelKey: String](avassetdownloadtaskmediaselectionprefersmultichannelkey.md)
  A key that indicates whether the task downloads media selections with support for multichannel playback, when available.
- [let AVAssetDownloadTaskPrefersHDRKey: String](avassetdownloadtaskprefershdrkey.md)
  A key that indicates whether the task downloads HDR instead of SDR video, when available.
- [let AVAssetDownloadTaskPrefersLosslessAudioKey: String](avassetdownloadtaskpreferslosslessaudiokey.md)
  A key that indicates whether the task downloads media selections in lossless audio format, when available.

## See Also

- [func makeAssetDownloadTask(downloadConfiguration: AVAssetDownloadConfiguration) -> AVAssetDownloadTask](avassetdownloadurlsession/makeassetdownloadtask(downloadconfiguration:).md)
  Creates a download task that uses the specified configuration.
- [class AVAssetDownloadConfiguration](avassetdownloadconfiguration.md)
  An object that provides the configuration for a download task.
- [func makeAssetDownloadTask(asset: AVURLAsset, assetTitle: String, assetArtworkData: Data?, options: [String : Any]?) -> AVAssetDownloadTask?](avassetdownloadurlsession/makeassetdownloadtask(asset:assettitle:assetartworkdata:options:).md)
  Creates a download task to download the asset.
- [func makeAssetDownloadTask(asset: AVURLAsset, destinationURL: URL, options: [String : Any]?) -> AVAssetDownloadTask?](avassetdownloadurlsession/makeassetdownloadtask(asset:destinationurl:options:).md)
  Creates a download task to download the asset to the indicated location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadurlsession/aggregateassetdownloadtask(with:mediaselections:assettitle:assetartworkdata:options:))*