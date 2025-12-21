# Publishers.Delay

**Framework**: Combine  
**Kind**: struct

A publisher that delays delivery of elements and completion to the downstream receiver.

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
struct Delay<Upstream, Context> where Upstream : Publisher, Context : Scheduler
```

## Topics

### Creating a delay publisher
- [init(upstream: Upstream, interval: Context.SchedulerTimeType.Stride, tolerance: Context.SchedulerTimeType.Stride, scheduler: Context, options: Context.SchedulerOptions?)](publishers/delay/init(upstream:interval:tolerance:scheduler:options:).md)
  Creates a publisher that delays delivery of elements and completion to the downstream receiver.
### Declaring supporting types
- [Publishers.Delay.Output](publishers/delay/output.md)
  The kind of values published by this publisher.
- [Publishers.Delay.Failure](publishers/delay/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](publishers/delay/upstream.md)
  The publisher from which this publisher receives its elements.
- [let interval: Context.SchedulerTimeType.Stride](publishers/delay/interval.md)
  The amount of time to delay.
- [let tolerance: Context.SchedulerTimeType.Stride](publishers/delay/tolerance.md)
  The allowed tolerance in firing delayed events.
- [let scheduler: Context](publishers/delay/scheduler.md)
  The scheduler to deliver the delayed events.
- [let options: Context.SchedulerOptions?](publishers/delay/options.md)
  Options relevant to the scheduler’s behavior.

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.MeasureInterval](publishers/measureinterval.md)
  A publisher that measures and emits the time interval between events received from an upstream publisher.
- [Publishers.Debounce](publishers/debounce.md)
  A publisher that publishes elements only after a specified time interval elapses between events.
- [Publishers.Throttle](publishers/throttle.md)
  A publisher that publishes either the most-recent or first element published by the upstream publisher in a specified time interval.
- [Publishers.Timeout](publishers/timeout.md)
  A publisher that terminates publishing if the upstream publisher exceeds a specified time interval without producing an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/delay)*