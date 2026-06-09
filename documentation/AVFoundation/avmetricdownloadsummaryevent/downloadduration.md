# downloadDuration

**Framework**: AVFoundation  
**Kind**: property

Returns the total duration of the download in seconds.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var downloadDuration: TimeInterval { get }
```

## See Also

- [var bytesDownloadedCount: Int](avmetricdownloadsummaryevent/bytesdownloadedcount.md)
  Returns the total number of bytes downloaded by the download task.
- [var mediaResourceRequestCount: Int](avmetricdownloadsummaryevent/mediaresourcerequestcount.md)
  Returns the total number of media requests performed by the download task. This includes playlist requests, media segment requests, and content key requests.
- [var recoverableErrorCount: Int](avmetricdownloadsummaryevent/recoverableerrorcount.md)
  Returns the total count of recoverable errors encountered during the download. If no errors were encountered, returns 0.
- [var variants: [AVAssetVariant]](avmetricdownloadsummaryevent/variants.md)
  Returns the variants that were downloaded.
- [var errorEvent: AVMetricErrorEvent?](avmetricdownloadsummaryevent/errorevent.md)
  Returns the error event if any. If no value is available, returns nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricdownloadsummaryevent/downloadduration)*