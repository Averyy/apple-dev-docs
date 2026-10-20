# urlSession(_:aggregateAssetDownloadTask:didCompleteFor:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a child task finished downloading a media selection.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use the NSURLSessionDownloadDelegate method instead, URLSession:task:didCompleteWithError:

## Declaration

```swift
optional func urlSession(_ session: URLSession, aggregateAssetDownloadTask: AVAggregateAssetDownloadTask, didCompleteFor mediaSelection: AVMediaSelection)
```

```objc
- (void) URLSession:(NSURLSession *) session aggregateAssetDownloadTask:(AVAggregateAssetDownloadTask *) aggregateAssetDownloadTask didCompleteForMediaSelection:(AVMediaSelection *) mediaSelection;
```

## Parameters

- `session`: The session the asset download task is on.
- `aggregateAssetDownloadTask`: The download task that finished downloading the media selection.
- `mediaSelection`: The downloaded media selection.

## See Also

### Responding to aggregate download events
- [func urlSession(URLSession, aggregateAssetDownloadTask: AVAggregateAssetDownloadTask, willDownloadTo: URL)](./urlsession%28_,aggregateassetdownloadtask,willdownloadto%29.md)
  Tells the delegate the final location of the asset when the download completes.
- [func urlSession(URLSession, aggregateAssetDownloadTask: AVAggregateAssetDownloadTask, didLoad: CMTimeRange, totalTimeRangesLoaded: [NSValue], timeRangeExpectedToLoad: CMTimeRange, for: AVMediaSelection)](./urlsession%28_,aggregateassetdownloadtask,didload,totaltimerangesloaded,timerangeexpectedtoload,for%29.md)
  Tells the delegate that the aggregate download task loaded a new time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:aggregateassetdownloadtask:didcompletefor:))*