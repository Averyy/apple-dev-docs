# urlSession(_:assetDownloadTask:didLoad:totalTimeRangesLoaded:timeRangeExpectedToLoad:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a download task loaded a new time range.

**Availability**:
- iOS 9.0+ - Deprecated in 27.0
- iPadOS 9.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use NSURLSessionTask.progress instead

## Declaration

```swift
optional func urlSession(_ session: URLSession, assetDownloadTask: AVAssetDownloadTask, didLoad timeRange: CMTimeRange, totalTimeRangesLoaded loadedTimeRanges: [NSValue], timeRangeExpectedToLoad: CMTimeRange)
```

```objc
- (void) URLSession:(NSURLSession *) session assetDownloadTask:(AVAssetDownloadTask *) assetDownloadTask didLoadTimeRange:(CMTimeRange) timeRange totalTimeRangesLoaded:(NSArray<NSValue *> *) loadedTimeRanges timeRangeExpectedToLoad:(CMTimeRange) timeRangeExpectedToLoad;
```

#### Discussion

Implement this method to track the download status of an asset. The following example shows how to calculate the percentage complete for the current download.

**Swift**:

```swift
func urlSession(_ session: URLSession, assetDownloadTask: AVAssetDownloadTask, didLoad timeRange: CMTimeRange, totalTimeRangesLoaded loadedTimeRanges: [NSValue], timeRangeExpectedToLoad: CMTimeRange) {
    var percentageComplete = 0.0
    // Iterate over loaded time ranges
    for value in loadedTimeRanges {
        // Unpack CMTimeRange value
        let loadedTimeRange = value.timeRangeValue
        percentageComplete += loadedTimeRange.duration.seconds / timeRangeExpectedToLoad.duration.seconds
    }
    percentageComplete *= 100
    // Updated interested observers of percentage change
}
```

**Objective-C**:

```objc
- (void)URLSession:(NSURLSession *)session assetDownloadTask:(AVAssetDownloadTask *)assetDownloadTask
                                            didLoadTimeRange:(CMTimeRange)timeRange
                                       totalTimeRangesLoaded:(NSArray<NSValue *> *)loadedTimeRanges
                                     timeRangeExpectedToLoad:(CMTimeRange)timeRangeExpectedToLoad {
    double percentageComplete = 0.0f;
    // Iterate over loaded time ranges
    for (NSValue *value in loadedTimeRanges) {
        // Unpack CMTimeRange value
        CMTimeRange loadedTimeRange = value.CMTimeRangeValue;
        percentageComplete +=
            CMTimeGetSeconds(loadedTimeRange.duration) / CMTimeGetSeconds(timeRangeExpectedToLoad.duration);
    }
    percentageComplete *= 100;
    // Updated interested observers of percentage change
}
```

## Parameters

- `session`: The session the asset download task is on.
- `assetDownloadTask`: The download task that loaded a new time range.
- `timeRange`: A [`CMTimeRange`](../../CoreMedia/cmtimerange.md) value that indicates the time range the task loaded since the last call to this method.
- `loadedTimeRanges`: An array of [`CMTimeRange`](../../CoreMedia/cmtimerange.md) values that indicate the time ranges the task has downloaded so far.
- `timeRangeExpectedToLoad`: A [`CMTimeRange`](../../CoreMedia/cmtimerange.md) value that indicates the expected duration of the downloaded asset.

## See Also

### Responding to download events
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didResolve: AVMediaSelection)](./urlsession%28_,assetdownloadtask,didresolve%29.md)
  Tells the delegate that a download task resolved the media selection to download, including any automatic selections.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didFinishDownloadingTo: URL)](./urlsession%28_,assetdownloadtask,didfinishdownloadingto%29.md)
  Tells the delegate that a download task finished downloading the requested asset.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, willDownloadVariants: [AVAssetVariant])](./urlsession%28_,assetdownloadtask,willdownloadvariants%29.md)
  Tells the delegate that a download task completed variant selection.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, willDownloadTo: URL)](./urlsession%28_,assetdownloadtask,willdownloadto%29.md)
  Tells the delegate when a download task determines its download location.
- [func urlSession(URLSession, assetDownloadTask: AVAssetDownloadTask, didReceive: AVMetricEvent)](./urlsession%28_,assetdownloadtask,didreceive%29.md)
  Sent when a download task receives an AVMetricEvent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/urlsession(_:assetdownloadtask:didload:totaltimerangesloaded:timerangeexpectedtoload:))*