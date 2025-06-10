# AVAssetDownloadDelegate

**Framework**: AVFoundation  
**Kind**: protocol

A protocol that defines the methods to implement to respond to asset-download events.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
protocol AVAssetDownloadDelegate : URLSessionTaskDelegate
```

## Topics

### Responding to Download Events
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didResolve: AVMediaSelection)](avassetdownloaddelegate/urlsession(_:assetdownloadtask:didresolve:).md)
  Tells the delegate that a download task resolved the media selection to download, including any automatic selections.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didLoad: CMTimeRange, totalTimeRangesLoaded: [NSValue], timeRangeExpectedToLoad: CMTimeRange)](avassetdownloaddelegate/urlsession(_:assetdownloadtask:didload:totaltimerangesloaded:timerangeexpectedtoload:).md)
  Tells the delegate that a download task loaded a new time range.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didFinishDownloadingTo: URL)](avassetdownloaddelegate/urlsession(_:assetdownloadtask:didfinishdownloadingto:).md)
  Tells the delegate that a download task finished downloading the requested asset.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, willDownloadVariants: [AVAssetVariant])](avassetdownloaddelegate/urlsession(_:assetdownloadtask:willdownloadvariants:).md)
  Tells the delegate that a download task completed variant selection.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, willDownloadTo: URL)](avassetdownloaddelegate/urlsession(_:assetdownloadtask:willdownloadto:).md)
  Tells the delegate when a download task determines its download location.
### Responding to Aggregate Download Events
- [func urlSession(URLSession, aggregateAssetDownloadTask: AVAggregateAssetDownloadTask, willDownloadTo: URL)](avassetdownloaddelegate/urlsession(_:aggregateassetdownloadtask:willdownloadto:).md)
  Tells the delegate the final location of the asset when the download completes.
- [func urlSession(URLSession, aggregateAssetDownloadTask: AVAggregateAssetDownloadTask, didLoad: CMTimeRange, totalTimeRangesLoaded: [NSValue], timeRangeExpectedToLoad: CMTimeRange, for: AVMediaSelection)](avassetdownloaddelegate/urlsession(_:aggregateassetdownloadtask:didload:totaltimerangesloaded:timerangeexpectedtoload:for:).md)
  Tells the delegate that the aggregate download task loaded a new time range.
- [func urlSession(URLSession, aggregateAssetDownloadTask: AVAggregateAssetDownloadTask, didCompleteFor: AVMediaSelection)](avassetdownloaddelegate/urlsession(_:aggregateassetdownloadtask:didcompletefor:).md)
  Tells the delegate that a child task finished downloading a media selection.
### Instance Methods
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didReceive: AVMetricEvent)](avassetdownloaddelegate/urlsession(_:assetdownloadtask:didreceive:).md)
  Sent when a download task receives an AVMetricEvent.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [URLSessionDelegate](../Foundation/URLSessionDelegate.md)
- [URLSessionTaskDelegate](../Foundation/URLSessionTaskDelegate.md)

## See Also

- [init(configuration: URLSessionConfiguration, assetDownloadDelegate: (any AVAssetDownloadDelegate)?, delegateQueue: OperationQueue?)](avassetdownloadurlsession/init(configuration:assetdownloaddelegate:delegatequeue:).md)
  Creates a URL session to download assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate)*