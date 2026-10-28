# urlSession(_:assetDownloadTask:didResolve:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) URLSession:(NSURLSession *) session assetDownloadTask:(AVAssetDownloadTask *) assetDownloadTask didResolveMediaSelection:(AVMediaSelection *) resolvedMediaSelection;
```

## Discussion

For the best chance of playing back downloaded content without further network I/O, set this selection on the associated [`AVPlayerItem`](../avplayeritem.md).

## Parameters

- `session`: The session the asset download task is on.
- `assetDownloadTask`: The task that resolved the media selection.
- `resolvedMediaSelection`: The media selection the task resolved.

## See Also

### Responding to download events
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didLoad: CMTimeRange, totalTimeRangesLoaded: [NSValue], timeRangeExpectedToLoad: CMTimeRange)](./urlsession%28_,assetdownloadtask,didload,totaltimerangesloaded,timerangeexpectedtoload%29.md)
  Tells the delegate that a download task loaded a new time range.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didFinishDownloadingTo: URL)](./urlsession%28_,assetdownloadtask,didfinishdownloadingto%29.md)
  Tells the delegate that a download task finished downloading the requested asset.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, willDownloadVariants: [AVAssetVariant])](./urlsession%28_,assetdownloadtask,willdownloadvariants%29.md)
  Tells the delegate that a download task completed variant selection.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, willDownloadTo: URL)](./urlsession%28_,assetdownloadtask,willdownloadto%29.md)
  Tells the delegate when a download task determines its download location.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didReceive: AVMetricEvent)](./urlsession%28_,assetdownloadtask,didreceive%29.md)
  Sent when a download task receives an AVMetricEvent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:assetdownloadtask:didresolve:))*