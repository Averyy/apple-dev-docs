# urlSession(_:aggregateAssetDownloadTask:didLoad:totalTimeRangesLoaded:timeRangeExpectedToLoad:for:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the aggregate download task loaded a new time range.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use NSURLSessionTask.progress: instead

## Declaration

```swift
optional func urlSession(_ session: URLSession, aggregateAssetDownloadTask: AVAggregateAssetDownloadTask, didLoad timeRange: CMTimeRange, totalTimeRangesLoaded loadedTimeRanges: [NSValue], timeRangeExpectedToLoad: CMTimeRange, for mediaSelection: AVMediaSelection)
```

```objc
- (void) URLSession:(NSURLSession *) session aggregateAssetDownloadTask:(AVAggregateAssetDownloadTask *) aggregateAssetDownloadTask didLoadTimeRange:(CMTimeRange) timeRange totalTimeRangesLoaded:(NSArray<NSValue *> *) loadedTimeRanges timeRangeExpectedToLoad:(CMTimeRange) timeRangeExpectedToLoad forMediaSelection:(AVMediaSelection *) mediaSelection;
```

## Parameters

- `session`: The session the asset download task is on.
- `aggregateAssetDownloadTask`: The download task that loaded a new time range.
- `timeRange`: A [`CMTimeRange`](../../CoreMedia/cmtimerange.md) value that indicates the time range the task loaded since the last call to this method.
- `loadedTimeRanges`: An array of CMTimeRange values that indicate the time ranges the task has downloaded so far.
- `timeRangeExpectedToLoad`: A CMTimeRange value that indicates the expected duration of the downloaded asset.
- `mediaSelection`: The media selection the task is downloading.

## See Also

### Responding to aggregate download events
- [func urlSession(URLSession, aggregateAssetDownloadTask: AVAggregateAssetDownloadTask, willDownloadTo: URL)](./urlsession%28_,aggregateassetdownloadtask,willdownloadto%29.md)
  Tells the delegate the final location of the asset when the download completes.
- [func urlSession(URLSession, aggregateAssetDownloadTask: AVAggregateAssetDownloadTask, didCompleteFor: AVMediaSelection)](./urlsession%28_,aggregateassetdownloadtask,didcompletefor%29.md)
  Tells the delegate that a child task finished downloading a media selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:aggregateassetdownloadtask:didload:totaltimerangesloaded:timerangeexpectedtoload:for:))*