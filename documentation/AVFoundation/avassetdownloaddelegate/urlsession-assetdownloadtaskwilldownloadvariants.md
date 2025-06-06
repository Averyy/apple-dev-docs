# urlSession(_:assetDownloadTask:willDownloadVariants:)

**Framework**: AVFoundation  
**Kind**: method

Tells the delegate that a download task completed variant selection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
optional func urlSession(_ session: URLSession, assetDownloadTask: AVAssetDownloadTask, willDownloadVariants variants: [AVAssetVariant])
```

## Parameters

- `session`: The session the asset download task is on.
- `assetDownloadTask`: The task that finished selecting variant selection.
- `variants`: The asset variants to download.

## See Also

- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didResolve: AVMediaSelection)](avassetdownloaddelegate/urlsession(_:assetdownloadtask:didresolve:).md)
  Tells the delegate that a download task resolved the media selection to download, including any automatic selections.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didLoad: CMTimeRange, totalTimeRangesLoaded: [NSValue], timeRangeExpectedToLoad: CMTimeRange)](avassetdownloaddelegate/urlsession(_:assetdownloadtask:didload:totaltimerangesloaded:timerangeexpectedtoload:).md)
  Tells the delegate that a download task loaded a new time range.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didFinishDownloadingTo: URL)](avassetdownloaddelegate/urlsession(_:assetdownloadtask:didfinishdownloadingto:).md)
  Tells the delegate that a download task finished downloading the requested asset.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, willDownloadTo: URL)](avassetdownloaddelegate/urlsession(_:assetdownloadtask:willdownloadto:).md)
  Tells the delegate when a download task determines its download location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:assetdownloadtask:willdownloadvariants:))*