# AVAssetDownloadTask

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

A URL session task that downloads a remote asset to the device for offline playback.

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

```objc
@interface AVAssetDownloadTask : NSURLSessionTask
```

#### Overview

You create instances of this class by calling [`makeAssetDownloadTask(downloadConfiguration:)`](./avassetdownloadurlsession/makeassetdownloadtask%28downloadconfiguration%29.md) on the download session.

To play an asset while its download is in progress, reuse the [`AVURLAsset`](./avurlasset.md) you supplied to the [`AVAssetDownloadConfiguration`](./avassetdownloadconfiguration.md). The asset reads locally cached segments during concurrent playback when the streaming variant matches the downloading variant.

Adopt the [`AVAssetDownloadDelegate`](./avassetdownloaddelegate.md) protocol to receive progress and completion callbacks. Use the inherited [`progress`](../Foundation/urlsessiontask/progress.md) property for numeric download progress updates. The delegate method [`urlSession(_:assetDownloadTask:willDownloadTo:)`](./avassetdownloaddelegate/urlsession%28_,assetdownloadtask,willdownloadto%29.md) provides the local file URL where the system stores the asset.

> ❗ **Important**: Save the local file URL the delegate provides. You need it to reconstruct the offline [`AVURLAsset`](./avurlasset.md) on subsequent app launches.

To augment an existing download, initialize a new task with an [`AVURLAsset`](./avurlasset.md) whose URL references the downloaded asset on disk. For example, you can add media selections that you didn’t include in the original download.

##### Live Activity

To control how the system schedules downloads, set the [`isDiscretionary`](../Foundation/urlsessionconfiguration/isdiscretionary.md) property on the [`URLSessionConfiguration`](../Foundation/urlsessionconfiguration.md) you pass when creating the [`AVAssetDownloadURLSession`](./avassetdownloadurlsession.md). Non-discretionary downloads start as soon as possible. The system defers discretionary downloads until conditions like network and battery state are favorable, and runs them silently in the background.

On supported platforms, a non-discretionary download displays a Live Activity on the Lock Screen and in the Dynamic Island that shows real-time download progress. Discretionary downloads don’t display a Live Activity.

When your app has multiple active downloads, the system aggregates them into a single Live Activity that shows combined progress. For a single active download, the activity title displays the asset title.

If any downloads in the group fail, the Live Activity transitions to a failure state after all downloads finish. A person can also cancel all active and queued downloads for your app directly from the Live Activity, which causes the tasks to fail with an error in the [`NSCocoaErrorDomain`](../Foundation/nscocoaerrordomain.md) domain with code https://developer.apple.com/documentation/foundation/nsusercancellederror.

The Live Activity doesn’t reflect download tasks until you resume them. If you resume a task while your app runs in the background, the system might demote it to discretionary. The system queues downloads in the order you resume them.

Swift subclasses of this type must conform to [`Sendable`](../Swift/sendable.md).

## Topics

### Accessing task information
- [var urlAsset: AVURLAsset](./avassetdownloadtask/urlasset.md)
  The asset that this task downloads.
- [var loadedTimeRanges: [NSValue]](./avassetdownloadtask/loadedtimeranges.md)
  The time ranges of the downloaded media that are ready for playback.
- [var options: [String : Any]?](./avassetdownloadtask/options.md)
  The configuration options for the task.
- [var destinationURL: URL](./avassetdownloadtask/destinationurl.md)
  The local file URL to where the task downloads the asset.

## Relationships

### Inherits From
- [URLSessionTask](../Foundation/urlsessiontask.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [ProgressReporting](../Foundation/progressreporting.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Asset downloading
- [Using AVFoundation to play and persist HTTP live streams](./using-avfoundation-to-play-and-persist-http-live-streams.md)
  Play HTTP Live Streams and persist streams on disk for offline playback using AVFoundation.
- [class AVAssetDownloadURLSession](./avassetdownloadurlsession.md)
  A URL session that creates and manages asset download tasks.
- [class AVAggregateAssetDownloadTask](./avaggregateassetdownloadtask.md)
  A task that downloads multiple media selections for an asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadtask)*