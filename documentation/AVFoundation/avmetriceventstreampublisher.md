# AVMetricEventStreamPublisher

**Framework**: AVFoundation  
**Kind**: protocol

A type for objects that publish metric events to the event stream.

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
protocol AVMetricEventStreamPublisher
```

## Topics

### Getting the metrics
- [func allMetrics() -> AVMetrics<AVMetricEvent>](avmetriceventstreampublisher/allmetrics.md)
- [func metrics<MetricEvent>(forType: MetricEvent.Type) -> AVMetrics<MetricEvent>](avmetriceventstreampublisher/metrics(fortype:).md)

## Relationships

### Conforming Types
- [AVPlayerItem](avplayeritem.md)

## See Also

- [struct AVMetrics](avmetrics.md)
  An asynchronous stream of metric information.
- [struct AVMergedMetrics](avmergedmetrics.md)
  An asynchronous stream of metric information from different publishers.
- [class AVVideoPerformanceMetrics](avvideoperformancemetrics.md)
  An object that provides metrics related to video playback quality.
- [class AVMetricEvent](avmetricevent.md)
  A base class that represents a metric event.
- [class AVMetricErrorEvent](avmetricerrorevent.md)
  An object that represents a metric event when an error occurs.
- [Metric event types](metric-event-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetriceventstreampublisher)*