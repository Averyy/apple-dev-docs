# urlSession(_:assetDownloadTask:didReceive:)

**Framework**: AVFoundation  
**Kind**: method

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

## Parameters

- `session`: The NSURLSession corresponding to this AVAssetDownloadTask.
- `assetDownloadTask`: The asset download task.
- `metricEvent`: The metric event received.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:assetdownloadtask:didreceive:))*