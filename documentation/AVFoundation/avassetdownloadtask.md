# AVAssetDownloadTask

**Framework**: AVFoundation  
**Kind**: class

A session used to download HTTP Live Streaming assets.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
class AVAssetDownloadTask
```

#### Overview

This class is a subclass of [`URLSessionTask`](https://developer.apple.com/documentation/Foundation/URLSessionTask) that you use to download HTTP Live Streaming assets. You create instances of this class by calling [`makeAssetDownloadTask(downloadConfiguration:)`](avassetdownloadurlsession/makeassetdownloadtask(downloadconfiguration:).md) on the download session.

## Topics

### Accessing Task Information
- [var urlAsset: AVURLAsset](avassetdownloadtask/urlasset.md)
  The asset that this task downloads.
- [var loadedTimeRanges: [NSValue]](avassetdownloadtask/loadedtimeranges.md)
  The time ranges of the downloaded media that are ready for playback.
- [var options: [String : Any]?](avassetdownloadtask/options.md)
  The configuration options for the task.
- [var destinationURL: URL](avassetdownloadtask/destinationurl.md)
  The local file URL to where the task downloads the asset.

## Relationships

### Inherits From
- [URLSessionTask](../Foundation/URLSessionTask.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [ProgressReporting](../Foundation/ProgressReporting.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Using AVFoundation to play and persist HTTP Live Streams](using-avfoundation-to-play-and-persist-http-live-streams.md)
  Play HTTP Live Streams and persist streams on disk for offline playback using AVFoundation.
- [class AVAssetDownloadURLSession](avassetdownloadurlsession.md)
  A URL session that creates and executes asset download tasks.
- [class AVAggregateAssetDownloadTask](avaggregateassetdownloadtask.md)
  A task that downloads multiple media selections for an asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadtask)*