# Publishers.Timeout

**Framework**: Combine  
**Kind**: struct

A publisher that terminates publishing if the upstream publisher exceeds a specified time interval without producing an element.

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
struct Timeout<Upstream, Context> where Upstream : Publisher, Context : Scheduler
```

## Topics

### Creating a Timeout Publisher
- [init(upstream: Upstream, interval: Context.SchedulerTimeType.Stride, scheduler: Context, options: Context.SchedulerOptions?, customError: (() -> Publishers.Timeout<Upstream, Context>.Failure)?)](publishers/timeout/init(upstream:interval:scheduler:options:customerror:).md)
  Creates a publisher that terminates publishing if the upstream publisher exceeds the specified time interval without producing an element.
### Declaring Publisher Topography
- [Publishers.Timeout.Output](publishers/timeout/output.md)
  The kind of values published by this publisher.
- [Publishers.Timeout.Failure](publishers/timeout/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/timeout/upstream.md)
  The publisher from which this publisher receives elements.
- [let interval: Context.SchedulerTimeType.Stride](publishers/timeout/interval.md)
  The maximum time interval the publisher can go without emitting an element, expressed in the time system of the scheduler.
- [let scheduler: Context](publishers/timeout/scheduler.md)
  The scheduler on which to deliver events.
- [let options: Context.SchedulerOptions?](publishers/timeout/options.md)
  Scheduler options that customize the delivery of elements.
- [let customError: (() -> Publishers.Timeout<Upstream, Context>.Failure)?](publishers/timeout/customerror.md)
  A closure that executes if the publisher times out. The publisher sends the failure returned by this closure to the subscriber as the reason for termination.
### Applying Operators
- [Publisher Operators](publishers-timeout-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](publishers/timeout/publisher-implementations.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.MeasureInterval](publishers/measureinterval.md)
  A publisher that measures and emits the time interval between events received from an upstream publisher.
- [Publishers.Debounce](publishers/debounce.md)
  A publisher that publishes elements only after a specified time interval elapses between events.
- [Publishers.Delay](publishers/delay.md)
  A publisher that delays delivery of elements and completion to the downstream receiver.
- [Publishers.Throttle](publishers/throttle.md)
  A publisher that publishes either the most-recent or first element published by the upstream publisher in a specified time interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/timeout)*