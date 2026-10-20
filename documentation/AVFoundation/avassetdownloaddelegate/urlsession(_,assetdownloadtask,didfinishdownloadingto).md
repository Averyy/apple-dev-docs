# urlSession(_:assetDownloadTask:didFinishDownloadingTo:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a download task finished downloading the requested asset.

**Availability**:
- iOS 10.0+ - Deprecated in 27.0
- iPadOS 10.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 10.0+ - Deprecated in 27.0

> **Deprecated**: Use URLSession:assetDownloadTask:willDownloadToURL: instead

## Declaration

```swift
optional func urlSession(_ session: URLSession, assetDownloadTask: AVAssetDownloadTask, didFinishDownloadingTo location: URL)
```

```objc
- (void) URLSession:(NSURLSession *) session assetDownloadTask:(AVAssetDownloadTask *) assetDownloadTask didFinishDownloadingToURL:(NSURL *) location;
```

#### Discussion

Don’t move the downloaded asset from this location. Downloaded assets must remain at the system-provided URL. Instead, save a persistent reference to this URL for future use.

## Parameters

- `session`: The session the asset download task is on.
- `assetDownloadTask`: The download task whose downloaded completed.
- `location`: The download location of the asset.

## See Also

### Responding to download events
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didResolve: AVMediaSelection)](./urlsession%28_,assetdownloadtask,didresolve%29.md)
  Tells the delegate that a download task resolved the media selection to download, including any automatic selections.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didLoad: CMTimeRange, totalTimeRangesLoaded: [NSValue], timeRangeExpectedToLoad: CMTimeRange)](./urlsession%28_,assetdownloadtask,didload,totaltimerangesloaded,timerangeexpectedtoload%29.md)
  Tells the delegate that a download task loaded a new time range.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, willDownloadVariants: [AVAssetVariant])](./urlsession%28_,assetdownloadtask,willdownloadvariants%29.md)
  Tells the delegate that a download task completed variant selection.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, willDownloadTo: URL)](./urlsession%28_,assetdownloadtask,willdownloadto%29.md)
  Tells the delegate when a download task determines its download location.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didReceive: AVMetricEvent)](./urlsession%28_,assetdownloadtask,didreceive%29.md)
  Sent when a download task receives an AVMetricEvent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:assetdownloadtask:didfinishdownloadingto:))*