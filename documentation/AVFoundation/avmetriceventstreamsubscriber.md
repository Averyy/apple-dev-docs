# AVMetricEventStreamSubscriber

**Framework**: AVFoundation  
**Kind**: protocol  
**Role**: Protocol

A type for objects that receive metric events.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```objc
@protocol AVMetricEventStreamSubscriber
```

## Topics

### Receiving metric events
- [- publisher:didReceiveEvent:](./avmetriceventstreamsubscriber/publisher_didreceiveevent_.md)
  Tells the subscriber that the publisher produced a metric event.

## See Also

### Metrics
- [class AVVideoPerformanceMetrics](./avvideoperformancemetrics.md)
  An object that provides metrics related to video playback quality.
- [AVMetricEventStream](./avmetriceventstream.md)
  An object that allows clients to add publishers and then subscribe to specific metric event classes from those publishers.
- [protocol AVMetricEventStreamPublisher](./avmetriceventstreampublisher.md)
  A type for objects that publish metric events to the event stream.
- [class AVMetricEvent](./avmetricevent.md)
  A base class that represents a metric event.
- [class AVMetricErrorEvent](./avmetricerrorevent.md)
  An object that represents a metric event when an error occurs.
- [Metric event types](./metric-event-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetriceventstreamsubscriber)*