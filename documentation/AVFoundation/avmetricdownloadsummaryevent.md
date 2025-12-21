# AVMetricDownloadSummaryEvent

**Framework**: AVFoundation  
**Kind**: class

Represents a summary metric event with aggregated metrics for the entire download task.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
class AVMetricDownloadSummaryEvent
```

#### Overview

Subclasses of this type that are used from Swift must fulfill the requirements of a Sendable type.

## Topics

### Instance Properties
- [var bytesDownloadedCount: Int](avmetricdownloadsummaryevent/bytesdownloadedcount.md)
  Returns the total number of bytes downloaded by the download task.
- [var downloadDuration: TimeInterval](avmetricdownloadsummaryevent/downloadduration.md)
  Returns the total duration of the download in seconds.
- [var errorEvent: AVMetricErrorEvent?](avmetricdownloadsummaryevent/errorevent.md)
  Returns the error event if any. If no value is available, returns nil.
- [var mediaResourceRequestCount: Int](avmetricdownloadsummaryevent/mediaresourcerequestcount.md)
  Returns the total number of media requests performed by the download task. This includes playlist requests, media segment requests, and content key requests.
- [var recoverableErrorCount: Int](avmetricdownloadsummaryevent/recoverableerrorcount.md)
  Returns the total count of recoverable errors encountered during the download. If no errors were encountered, returns 0.
- [var variants: [AVAssetVariant]](avmetricdownloadsummaryevent/variants.md)
  Returns the variants that were downloaded.

## Relationships

### Inherits From
- [AVMetricEvent](avmetricevent.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AVMetricPlayerItemPlaybackSummaryEvent](avmetricplayeritemplaybacksummaryevent.md)
  An event that represents the combined metrics for the entire playback session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricdownloadsummaryevent)*