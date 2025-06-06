# Publishers.Debounce

**Framework**: Combine  
**Kind**: struct

A publisher that publishes elements only after a specified time interval elapses between events.

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
struct Debounce<Upstream, Context> where Upstream : Publisher, Context : Scheduler
```

## Topics

### Creating a Debounce Publisher
- [init(upstream: Upstream, dueTime: Context.SchedulerTimeType.Stride, scheduler: Context, options: Context.SchedulerOptions?)](publishers/debounce/init(upstream:duetime:scheduler:options:).md)
  Creates a publisher that publishes elements only after a specified time interval elapses between events.
### Declaring Publisher Topography
- [Publishers.Debounce.Output](publishers/debounce/output.md)
  The kind of values published by this publisher.
- [Publishers.Debounce.Failure](publishers/debounce/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/debounce/upstream.md)
  The publisher from which this publisher receives elements.
- [let dueTime: Context.SchedulerTimeType.Stride](publishers/debounce/duetime.md)
  The amount of time the publisher should wait before publishing an element.
- [let scheduler: Context](publishers/debounce/scheduler.md)
  The scheduler on which this publisher delivers elements.
- [let options: Context.SchedulerOptions?](publishers/debounce/options.md)
  Scheduler options that customize this publisher’s delivery of elements.
### Applying Operators
- [Publisher Operators](publishers-debounce-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](publishers/debounce/publisher-implementations.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.MeasureInterval](publishers/measureinterval.md)
  A publisher that measures and emits the time interval between events received from an upstream publisher.
- [Publishers.Delay](publishers/delay.md)
  A publisher that delays delivery of elements and completion to the downstream receiver.
- [Publishers.Throttle](publishers/throttle.md)
  A publisher that publishes either the most-recent or first element published by the upstream publisher in a specified time interval.
- [Publishers.Timeout](publishers/timeout.md)
  A publisher that terminates publishing if the upstream publisher exceeds a specified time interval without producing an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/debounce)*