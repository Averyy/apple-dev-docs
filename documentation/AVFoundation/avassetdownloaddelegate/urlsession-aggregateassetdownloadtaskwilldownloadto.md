# urlSession(_:aggregateAssetDownloadTask:willDownloadTo:)

**Framework**: AVFoundation  
**Kind**: method

Tells the delegate the final location of the asset when the download completes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
optional func urlSession(_ session: URLSession, aggregateAssetDownloadTask: AVAggregateAssetDownloadTask, willDownloadTo location: URL)
```

## Parameters

- `session`: The session the asset download task is on.
- `aggregateAssetDownloadTask`: The task that downloads the asset.
- `location`: The file URL to which the task downloads media.

## See Also

- [func urlSession(URLSession, aggregateAssetDownloadTask: AVAggregateAssetDownloadTask, didLoad: CMTimeRange, totalTimeRangesLoaded: [NSValue], timeRangeExpectedToLoad: CMTimeRange, for: AVMediaSelection)](avassetdownloaddelegate/urlsession(_:aggregateassetdownloadtask:didload:totaltimerangesloaded:timerangeexpectedtoload:for:).md)
  Tells the delegate that the aggregate download task loaded a new time range.
- [func urlSession(URLSession, aggregateAssetDownloadTask: AVAggregateAssetDownloadTask, didCompleteFor: AVMediaSelection)](avassetdownloaddelegate/urlsession(_:aggregateassetdownloadtask:didcompletefor:).md)
  Tells the delegate that a child task finished downloading a media selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:aggregateassetdownloadtask:willdownloadto:))*