# AVAssetDownloadURLSession

**Framework**: AVFoundation  
**Kind**: class

A URL session that creates and manages asset download tasks.

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

#### Overview

Create an [`AVAssetDownloadURLSession`](avassetdownloadurlsession.md) by calling [`init(configuration:assetDownloadDelegate:delegateQueue:)`](avassetdownloadurlsession/init(configuration:assetdownloaddelegate:delegatequeue:).md) with a background [`URLSessionConfiguration`](https://developer.apple.com/documentation/foundation/urlsessionconfiguration). The background configuration supports reliable downloading while the app is in a suspended state.

> ❗ **Important**: The standard `URLSession` initializers and task-creation methods are unavailable on this class. Use [`init(configuration:assetDownloadDelegate:delegateQueue:)`](avassetdownloadurlsession/init(configuration:assetdownloaddelegate:delegatequeue:).md) to create a session and [`makeAssetDownloadTask(downloadConfiguration:)`](avassetdownloadurlsession/makeassetdownloadtask(downloadconfiguration:).md) to create download tasks.

Background sessions persist across app launches. The system manages downloads out-of-process so they continue while your app is in a suspended state. If the system terminates your app while downloads are in progress, it relaunches the app and calls [`application(_:handleEventsForBackgroundURLSession:completionHandler:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:handleeventsforbackgroundurlsession:completionhandler:)) with the session identifier. Recreate the [`AVAssetDownloadURLSession`](avassetdownloadurlsession.md) using the same background configuration identifier to reconnect to the running session and receive pending delegate callbacks. Call the provided completion handler after all callbacks finish. If a person force-quits your app, the system cancels all active downloads and doesn’t relaunch the app.

Mark the background session configuration as discretionary to let the system defer downloads until network and battery conditions are favorable. You can only start a non-discretionary download task while your app is in the foreground. Reserve non-discretionary sessions for downloads that a person explicitly starts. Use a discretionary session for opportunistic downloads that happen without a person’s direct involvement.

Assign an [`AVAssetDownloadDelegate`](avassetdownloaddelegate.md) to the session to receive download progress, media-selection resolution, and completion callbacks for every download task the session creates.

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
- [URLSession](../foundation/urlsession.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Using AVFoundation to play and persist HTTP live streams](using-avfoundation-to-play-and-persist-http-live-streams.md)
  Play HTTP Live Streams and persist streams on disk for offline playback using AVFoundation.
- [class AVAssetDownloadTask](avassetdownloadtask.md)
  A URL session task that downloads a remote asset to the device for offline playback.
- [class AVAggregateAssetDownloadTask](avaggregateassetdownloadtask.md)
  A task that downloads multiple media selections for an asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadurlsession)*