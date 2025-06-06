# Publishers.MeasureInterval

**Framework**: Combine  
**Kind**: struct

A publisher that measures and emits the time interval between events received from an upstream publisher.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct MeasureInterval<Upstream, Context> where Upstream : Publisher, Context : Scheduler
```

## Topics

### Creating a Measure Interval Publisher
- [init(upstream: Upstream, scheduler: Context)](publishers/measureinterval/init(upstream:scheduler:).md)
  Creates a publisher that measures and emits the time interval between events received from an upstream publisher.
### Declaring Publisher Topography
- [Publishers.MeasureInterval.Output](publishers/measureinterval/output.md)
  The kind of values published by this publisher.
- [Publishers.MeasureInterval.Failure](publishers/measureinterval/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/measureinterval/upstream.md)
  The publisher from which this publisher receives elements.
- [let scheduler: Context](publishers/measureinterval/scheduler.md)
  The scheduler used for tracking the timing of events.
### Applying Operators
- [Publisher Operators](publishers-measureinterval-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](publishers/measureinterval/publisher-implementations.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.Debounce](publishers/debounce.md)
  A publisher that publishes elements only after a specified time interval elapses between events.
- [Publishers.Delay](publishers/delay.md)
  A publisher that delays delivery of elements and completion to the downstream receiver.
- [Publishers.Throttle](publishers/throttle.md)
  A publisher that publishes either the most-recent or first element published by the upstream publisher in a specified time interval.
- [Publishers.Timeout](publishers/timeout.md)
  A publisher that terminates publishing if the upstream publisher exceeds a specified time interval without producing an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/measureinterval)*