# urlSession(_:assetDownloadTask:willDownloadTo:)

**Framework**: AVFoundation  
**Kind**: method

Tells the delegate when a download task determines its download location.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 14.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
optional func urlSession(_ session: URLSession, assetDownloadTask: AVAssetDownloadTask, willDownloadTo location: URL)
```

#### Discussion

Save the returned URL to instantiate the asset in the future.

## Parameters

- `session`: The session the asset download task is on.
- `assetDownloadTask`: The download task.
- `location`: The URL the task downloads the asset to.

## See Also

- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didResolve: AVMediaSelection)](avassetdownloaddelegate/urlsession(_:assetdownloadtask:didresolve:).md)
  Tells the delegate that a download task resolved the media selection to download, including any automatic selections.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didLoad: CMTimeRange, totalTimeRangesLoaded: [NSValue], timeRangeExpectedToLoad: CMTimeRange)](avassetdownloaddelegate/urlsession(_:assetdownloadtask:didload:totaltimerangesloaded:timerangeexpectedtoload:).md)
  Tells the delegate that a download task loaded a new time range.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didFinishDownloadingTo: URL)](avassetdownloaddelegate/urlsession(_:assetdownloadtask:didfinishdownloadingto:).md)
  Tells the delegate that a download task finished downloading the requested asset.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, willDownloadVariants: [AVAssetVariant])](avassetdownloaddelegate/urlsession(_:assetdownloadtask:willdownloadvariants:).md)
  Tells the delegate that a download task completed variant selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:assetdownloadtask:willdownloadto:))*