# urlSession(_:assetDownloadTask:willDownloadTo:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) URLSession:(NSURLSession *) session assetDownloadTask:(AVAssetDownloadTask *) assetDownloadTask willDownloadToURL:(NSURL *) location;
```

#### Discussion

Save the returned URL to instantiate the asset in the future.

## Parameters

- `session`: The session the asset download task is on.
- `assetDownloadTask`: The download task.
- `location`: The URL the task downloads the asset to.

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
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didReceive: AVMetricEvent)](./urlsession%28_,assetdownloadtask,didreceive%29.md)
  Sent when a download task receives an AVMetricEvent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:assetdownloadtask:willdownloadto:))*