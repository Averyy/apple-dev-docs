# Publishers.Throttle

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher that publishes either the most-recent or first element published by the upstream publisher in a specified time interval.

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
struct Throttle<Upstream, Context> where Upstream : Publisher, Context : Scheduler
```

## Topics

### Creating a throttle publisher
- [init(upstream: Upstream, interval: Context.SchedulerTimeType.Stride, scheduler: Context, latest: Bool)](./throttle/init%28upstream,interval,scheduler,latest%29.md)
  Creates a publisher that publishes either the most-recent or first element published by the upstream publisher in a specified time interval.
### Declaring supporting types
- [Publishers.Throttle.Output](./throttle/output.md)
  The kind of values published by this publisher.
- [Publishers.Throttle.Failure](./throttle/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](./throttle/upstream.md)
  The publisher from which this publisher receives elements.
- [let interval: Context.SchedulerTimeType.Stride](./throttle/interval.md)
  The interval in which to find and emit the most recent element.
- [let scheduler: Context](./throttle/scheduler.md)
  The scheduler on which to publish elements.
- [let latest: Bool](./throttle/latest.md)
  A Boolean value indicating whether to publish the most recent element.

## Relationships

### Conforms To
- [Publisher](../publisher.md)

## See Also

### Controlling timing
- [Publishers.MeasureInterval](./measureinterval.md)
  A publisher that measures and emits the time interval between events received from an upstream publisher.
- [Publishers.Debounce](./debounce.md)
  A publisher that publishes elements only after a specified time interval elapses between events.
- [Publishers.Delay](./delay.md)
  A publisher that delays delivery of elements and completion to the downstream receiver.
- [Publishers.Timeout](./timeout.md)
  A publisher that terminates publishing if the upstream publisher exceeds a specified time interval without producing an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/throttle)*