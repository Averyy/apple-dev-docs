# urlSession(_:assetDownloadTask:didResolve:)

**Framework**: AVFoundation  
**Kind**: method

Tells the delegate that a download task resolved the media selection to download, including any automatic selections.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
optional func urlSession(_ session: URLSession, assetDownloadTask: AVAssetDownloadTask, didResolve resolvedMediaSelection: AVMediaSelection)
```

#### Discussion

For the best chance of playing back downloaded content without further network I/O, set this selection on the associated [`AVPlayerItem`](avplayeritem.md).

## Parameters

- `session`: The session the asset download task is on.
- `assetDownloadTask`: The task that resolved the media selection.
- `resolvedMediaSelection`: The media selection the task resolved.

## See Also

- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didLoad: CMTimeRange, totalTimeRangesLoaded: [NSValue], timeRangeExpectedToLoad: CMTimeRange)](avassetdownloaddelegate/urlsession(_:assetdownloadtask:didload:totaltimerangesloaded:timerangeexpectedtoload:).md)
  Tells the delegate that a download task loaded a new time range.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didFinishDownloadingTo: URL)](avassetdownloaddelegate/urlsession(_:assetdownloadtask:didfinishdownloadingto:).md)
  Tells the delegate that a download task finished downloading the requested asset.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, willDownloadVariants: [AVAssetVariant])](avassetdownloaddelegate/urlsession(_:assetdownloadtask:willdownloadvariants:).md)
  Tells the delegate that a download task completed variant selection.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, willDownloadTo: URL)](avassetdownloaddelegate/urlsession(_:assetdownloadtask:willdownloadto:).md)
  Tells the delegate when a download task determines its download location.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didReceive: AVMetricEvent)](avassetdownloaddelegate/urlsession(_:assetdownloadtask:didreceive:).md)
  Sent when a download task receives an AVMetricEvent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:assetdownloadtask:didresolve:))*