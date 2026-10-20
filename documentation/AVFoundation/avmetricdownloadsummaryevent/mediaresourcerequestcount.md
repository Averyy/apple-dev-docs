# mediaResourceRequestCount

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Returns the total number of media requests performed by the download task. This includes playlist requests, media segment requests, and content key requests.

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
var mediaResourceRequestCount: Int { get }
```

```objc
@property (readonly) NSInteger mediaResourceRequestCount;
```

## See Also

### Inspecting the download summary
- [var downloadDuration: TimeInterval](./downloadduration.md)
  Returns the total duration of the download in seconds.
- [var bytesDownloadedCount: Int](./bytesdownloadedcount.md)
  Returns the total number of bytes downloaded by the download task.
- [var recoverableErrorCount: Int](./recoverableerrorcount.md)
  Returns the total count of recoverable errors encountered during the download. If no errors were encountered, returns 0.
- [var variants: [AVAssetVariant]](./variants.md)
  Returns the variants that were downloaded.
- [var errorEvent: AVMetricErrorEvent?](./errorevent.md)
  Returns the error event if any. If no value is available, returns nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricdownloadsummaryevent/mediaresourcerequestcount)*