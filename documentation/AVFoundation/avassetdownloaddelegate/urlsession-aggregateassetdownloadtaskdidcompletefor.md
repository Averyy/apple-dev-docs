# urlSession(_:aggregateAssetDownloadTask:didCompleteFor:)

**Framework**: AVFoundation  
**Kind**: method

Tells the delegate that a child task finished downloading a media selection.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
optional func urlSession(_ session: URLSession, aggregateAssetDownloadTask: AVAggregateAssetDownloadTask, didCompleteFor mediaSelection: AVMediaSelection)
```

## Parameters

- `session`: The session the asset download task is on.
- `aggregateAssetDownloadTask`: The download task that finished downloading the media selection.
- `mediaSelection`: The downloaded media selection.

## See Also

- [func urlSession(URLSession, aggregateAssetDownloadTask: AVAggregateAssetDownloadTask, willDownloadTo: URL)](avassetdownloaddelegate/urlsession(_:aggregateassetdownloadtask:willdownloadto:).md)
  Tells the delegate the final location of the asset when the download completes.
- [func urlSession(URLSession, aggregateAssetDownloadTask: AVAggregateAssetDownloadTask, didLoad: CMTimeRange, totalTimeRangesLoaded: [NSValue], timeRangeExpectedToLoad: CMTimeRange, for: AVMediaSelection)](avassetdownloaddelegate/urlsession(_:aggregateassetdownloadtask:didload:totaltimerangesloaded:timerangeexpectedtoload:for:).md)
  Tells the delegate that the aggregate download task loaded a new time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:aggregateassetdownloadtask:didcompletefor:))*