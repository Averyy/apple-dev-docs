# urlSession(_:assetDownloadTask:didReceive:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Sent when a download task receives an AVMetricEvent.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
optional func urlSession(_ session: URLSession, assetDownloadTask: AVAssetDownloadTask, didReceive metricEvent: AVMetricEvent)
```

```objc
- (void) URLSession:(NSURLSession *) session assetDownloadTask:(AVAssetDownloadTask *) assetDownloadTask didReceiveMetricEvent:(AVMetricEvent *) metricEvent;
```

## Parameters

- `session`: The NSURLSession corresponding to this AVAssetDownloadTask.
- `assetDownloadTask`: The asset download task.
- `metricEvent`: The metric event received.

## See Also

### Responding to download events
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didResolve: AVMediaSelection)](./urlsession%28_,assetdownloadtask,didresolve%29.md)
  Tells the delegate that a download task resolved the media selection to download, including any automatic selections.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didLoad: CMTimeRange, totalTimeRangesLoaded: [NSValue], timeRangeExpectedToLoad: CMTimeRange)](./urlsession%28_,assetdownloadtask,didload,totaltimerangesloaded,timerangeexpectedtoload%29.md)
  Tells the delegate that a download task loaded a new time range.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didFinishDownloadingTo: URL)](./urlsession%28_,assetdownloadtask,didfinishdownloadingto%29.md)
  Tells the delegate that a download task finished downloading the requested asset.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, willDownloadVariants: [AVAssetVariant])](./urlsession%28_,assetdownloadtask,willdownloadvariants%29.md)
  Tells the delegate that a download task completed variant selection.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, willDownloadTo: URL)](./urlsession%28_,assetdownloadtask,willdownloadto%29.md)
  Tells the delegate when a download task determines its download location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:assetdownloadtask:didreceive:))*