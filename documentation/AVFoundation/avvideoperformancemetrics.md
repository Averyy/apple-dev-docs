# AVVideoPerformanceMetrics

**Framework**: AVFoundation  
**Kind**: class

An object that provides metrics related to video playback quality.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
class AVVideoPerformanceMetrics
```

## Topics

### Inspecting metrics
- [var numberOfCorruptedFrames: Int](avvideoperformancemetrics/numberofcorruptedframes.md)
  The total number of corrupted frames.
- [var numberOfDroppedFrames: Int](avvideoperformancemetrics/numberofdroppedframes.md)
  The total number of frames the system drops prior to decoding or from missing the display deadline.
- [var numberOfFramesDisplayedUsingOptimizedCompositing: Int](avvideoperformancemetrics/numberofframesdisplayedusingoptimizedcompositing.md)
  The total number of full screen frames rendered in a special power-efficient mode that didn’t require compositing with other UI elements.
- [var totalAccumulatedFrameDelay: TimeInterval](avvideoperformancemetrics/totalaccumulatedframedelay.md)
  The accumulated amount of time between the prescribed presentation times of displayed video frames and their actual time of display.
- [var totalNumberOfFrames: Int](avvideoperformancemetrics/totalnumberofframes.md)
  The total number of frames that display if no frames drop.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AVMetrics](avmetrics.md)
  An asynchronous stream of metric information.
- [struct AVMergedMetrics](avmergedmetrics.md)
  An asynchronous stream of metric information from different publishers.
- [protocol AVMetricEventStreamPublisher](avmetriceventstreampublisher.md)
  A type for objects that publish metric events to the event stream.
- [class AVMetricEvent](avmetricevent.md)
  A base class that represents a metric event.
- [class AVMetricErrorEvent](avmetricerrorevent.md)
  An object that represents a metric event when an error occurs.
- [Metric event types](metric-event-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideoperformancemetrics)*