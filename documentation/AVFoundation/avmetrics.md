# AVMetrics

**Framework**: AVFoundation  
**Kind**: struct

An asynchronous stream of metric information.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct AVMetrics<MetricEvent> where MetricEvent : AVMetricEvent
```

## Topics

### Merging metrics
- [func chronologicalMerge<OtherSecondMetric, each MetricEventPack>(with: AVMetrics<OtherSecondMetric>, repeat AVMetrics<each MetricEventPack>) -> AVMergedMetrics<MetricEvent, OtherSecondMetric, repeat each MetricEventPack>](avmetrics/chronologicalmerge(with:_:).md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AVMergedMetrics](avmergedmetrics.md)
  An asynchronous stream of metric information from different publishers.
- [class AVVideoPerformanceMetrics](avvideoperformancemetrics.md)
  An object that provides metrics related to video playback quality.
- [protocol AVMetricEventStreamPublisher](avmetriceventstreampublisher.md)
  A type for objects that publish metric events to the event stream.
- [class AVMetricEvent](avmetricevent.md)
  A base class that represents a metric event.
- [class AVMetricErrorEvent](avmetricerrorevent.md)
  An object that represents a metric event when an error occurs.
- [Metric event types](metric-event-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetrics)*