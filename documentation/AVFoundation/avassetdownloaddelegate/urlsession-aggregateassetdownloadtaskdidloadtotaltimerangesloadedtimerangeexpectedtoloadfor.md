# urlSession(_:aggregateAssetDownloadTask:didLoad:totalTimeRangesLoaded:timeRangeExpectedToLoad:for:)

**Framework**: AVFoundation  
**Kind**: method

Tells the delegate that the aggregate download task loaded a new time range.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
optional func urlSession(_ session: URLSession, aggregateAssetDownloadTask: AVAggregateAssetDownloadTask, didLoad timeRange: CMTimeRange, totalTimeRangesLoaded loadedTimeRanges: [NSValue], timeRangeExpectedToLoad: CMTimeRange, for mediaSelection: AVMediaSelection)
```

## Parameters

- `session`: The session the asset download task is on.
- `aggregateAssetDownloadTask`: The download task that loaded a new time range.
- `timeRange`: A   value that indicates the time range the task loaded since the last call to this method.
- `loadedTimeRanges`: An array of CMTimeRange values that indicate the time ranges the task has downloaded so far.
- `timeRangeExpectedToLoad`: A CMTimeRange value that indicates the expected duration of the downloaded asset.
- `mediaSelection`: The media selection the task is downloading.

## See Also

- [func urlSession(URLSession, aggregateAssetDownloadTask: AVAggregateAssetDownloadTask, willDownloadTo: URL)](avassetdownloaddelegate/urlsession(_:aggregateassetdownloadtask:willdownloadto:).md)
  Tells the delegate the final location of the asset when the download completes.
- [func urlSession(URLSession, aggregateAssetDownloadTask: AVAggregateAssetDownloadTask, didCompleteFor: AVMediaSelection)](avassetdownloaddelegate/urlsession(_:aggregateassetdownloadtask:didcompletefor:).md)
  Tells the delegate that a child task finished downloading a media selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:aggregateassetdownloadtask:didload:totaltimerangesloaded:timerangeexpectedtoload:for:))*