# customError

**Framework**: Combine  
**Kind**: property

A closure that executes if the publisher times out. The publisher sends the failure returned by this closure to the subscriber as the reason for termination.

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
let customError: (() -> Publishers.Timeout<Upstream, Context>.Failure)?
```

## See Also

- [let upstream: Upstream](publishers/timeout/upstream.md)
  The publisher from which this publisher receives elements.
- [let interval: Context.SchedulerTimeType.Stride](publishers/timeout/interval.md)
  The maximum time interval the publisher can go without emitting an element, expressed in the time system of the scheduler.
- [let scheduler: Context](publishers/timeout/scheduler.md)
  The scheduler on which to deliver events.
- [let options: Context.SchedulerOptions?](publishers/timeout/options.md)
  Scheduler options that customize the delivery of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/timeout/customerror)*