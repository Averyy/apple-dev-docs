# urlSession(_:assetDownloadTask:didFinishDownloadingTo:)

**Framework**: AVFoundation  
**Kind**: method

Tells the delegate that a download task finished downloading the requested asset.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
optional func urlSession(_ session: URLSession, assetDownloadTask: AVAssetDownloadTask, didFinishDownloadingTo location: URL)
```

#### Discussion

Don’t move the downloaded asset from this location. Downloaded assets must remain at the system-provided URL. Instead, save a persistent reference to this URL for future use.

## Parameters

- `session`: The session the asset download task is on.
- `assetDownloadTask`: The download task whose downloaded completed.
- `location`: The download location of the asset.

## See Also

- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didResolve: AVMediaSelection)](avassetdownloaddelegate/urlsession(_:assetdownloadtask:didresolve:).md)
  Tells the delegate that a download task resolved the media selection to download, including any automatic selections.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didLoad: CMTimeRange, totalTimeRangesLoaded: [NSValue], timeRangeExpectedToLoad: CMTimeRange)](avassetdownloaddelegate/urlsession(_:assetdownloadtask:didload:totaltimerangesloaded:timerangeexpectedtoload:).md)
  Tells the delegate that a download task loaded a new time range.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, willDownloadVariants: [AVAssetVariant])](avassetdownloaddelegate/urlsession(_:assetdownloadtask:willdownloadvariants:).md)
  Tells the delegate that a download task completed variant selection.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, willDownloadTo: URL)](avassetdownloaddelegate/urlsession(_:assetdownloadtask:willdownloadto:).md)
  Tells the delegate when a download task determines its download location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:assetdownloadtask:didfinishdownloadingto:))*