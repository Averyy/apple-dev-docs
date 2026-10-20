# urlSession(_:assetDownloadTask:willDownloadVariants:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) URLSession:(NSURLSession *) session assetDownloadTask:(AVAssetDownloadTask *) assetDownloadTask willDownloadVariants:(NSArray<AVAssetVariant *> *) variants;
```

## Parameters

- `session`: The session the asset download task is on.
- `assetDownloadTask`: The task that finished selecting variant selection.
- `variants`: The asset variants to download.

## See Also

### Responding to download events
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didResolve: AVMediaSelection)](./urlsession%28_,assetdownloadtask,didresolve%29.md)
  Tells the delegate that a download task resolved the media selection to download, including any automatic selections.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didLoad: CMTimeRange, totalTimeRangesLoaded: [NSValue], timeRangeExpectedToLoad: CMTimeRange)](./urlsession%28_,assetdownloadtask,didload,totaltimerangesloaded,timerangeexpectedtoload%29.md)
  Tells the delegate that a download task loaded a new time range.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didFinishDownloadingTo: URL)](./urlsession%28_,assetdownloadtask,didfinishdownloadingto%29.md)
  Tells the delegate that a download task finished downloading the requested asset.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, willDownloadTo: URL)](./urlsession%28_,assetdownloadtask,willdownloadto%29.md)
  Tells the delegate when a download task determines its download location.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didReceive: AVMetricEvent)](./urlsession%28_,assetdownloadtask,didreceive%29.md)
  Sent when a download task receives an AVMetricEvent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:assetdownloadtask:willdownloadvariants:))*