# AVAssetDownloadURLSession

**Framework**: AVFoundation  
**Kind**: class

A URL session that creates and executes asset download tasks.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
class AVAssetDownloadURLSession
```

## Topics

### Creating a download session
- [init(configuration: URLSessionConfiguration, assetDownloadDelegate: (any AVAssetDownloadDelegate)?, delegateQueue: OperationQueue?)](avassetdownloadurlsession/init(configuration:assetdownloaddelegate:delegatequeue:).md)
  Creates a URL session to download assets.
- [protocol AVAssetDownloadDelegate](avassetdownloaddelegate.md)
  A protocol that defines the methods to implement to respond to asset-download events.
### Creating download tasks
- [func makeAssetDownloadTask(downloadConfiguration: AVAssetDownloadConfiguration) -> AVAssetDownloadTask](avassetdownloadurlsession/makeassetdownloadtask(downloadconfiguration:).md)
  Creates a download task that uses the specified configuration.
- [class AVAssetDownloadConfiguration](avassetdownloadconfiguration.md)
  An object that provides the configuration for a download task.
- [func makeAssetDownloadTask(asset: AVURLAsset, assetTitle: String, assetArtworkData: Data?, options: [String : Any]?) -> AVAssetDownloadTask?](avassetdownloadurlsession/makeassetdownloadtask(asset:assettitle:assetartworkdata:options:).md)
  Creates a download task to download the asset.
- [func aggregateAssetDownloadTask(with: AVURLAsset, mediaSelections: [AVMediaSelection], assetTitle: String, assetArtworkData: Data?, options: [String : Any]?) -> AVAggregateAssetDownloadTask?](avassetdownloadurlsession/aggregateassetdownloadtask(with:mediaselections:assettitle:assetartworkdata:options:).md)
  Creates a download task to download the asset and media selections.
- [func makeAssetDownloadTask(asset: AVURLAsset, destinationURL: URL, options: [String : Any]?) -> AVAssetDownloadTask?](avassetdownloadurlsession/makeassetdownloadtask(asset:destinationurl:options:).md)
  Creates a download task to download the asset to the indicated location.
### Download option keys
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

## Relationships

### Inherits From
- [URLSession](../Foundation/URLSession.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Using AVFoundation to play and persist HTTP live streams](using-avfoundation-to-play-and-persist-http-live-streams.md)
  Play HTTP Live Streams and persist streams on disk for offline playback using AVFoundation.
- [class AVAssetDownloadTask](avassetdownloadtask.md)
  A session used to download HTTP Live Streaming assets.
- [class AVAggregateAssetDownloadTask](avaggregateassetdownloadtask.md)
  A task that downloads multiple media selections for an asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadurlsession)*