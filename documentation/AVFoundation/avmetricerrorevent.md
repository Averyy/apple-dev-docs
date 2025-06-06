# AVMetricErrorEvent

**Framework**: AVFoundation  
**Kind**: class

An object that represents a metric event when an error occurs.

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
class AVMetricErrorEvent
```

## Topics

### Getting the error
- [var error: any Error](avmetricerrorevent/error.md)
  Returns the error event.
- [var didRecover: Bool](avmetricerrorevent/didrecover.md)
  A Boolean value that indicates whether the error was recoverable.

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

## See Also

- [struct AVMetrics](avmetrics.md)
  An asynchronous stream of metric information.
- [struct AVMergedMetrics](avmergedmetrics.md)
  An asynchronous stream of metric information from different publishers.
- [class AVVideoPerformanceMetrics](avvideoperformancemetrics.md)
  An object that provides metrics related to video playback quality.
- [protocol AVMetricEventStreamPublisher](avmetriceventstreampublisher.md)
  A type for objects that publish metric events to the event stream.
- [class AVMetricEvent](avmetricevent.md)
  A base class that represents a metric event.
- [Metric event types](metric-event-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricerrorevent)*