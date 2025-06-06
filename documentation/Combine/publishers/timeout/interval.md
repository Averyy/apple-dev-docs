# interval

**Framework**: Combine  
**Kind**: property

The maximum time interval the publisher can go without emitting an element, expressed in the time system of the scheduler.

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
let interval: Context.SchedulerTimeType.Stride
```

## See Also

- [let upstream: Upstream](publishers/timeout/upstream.md)
  The publisher from which this publisher receives elements.
- [let scheduler: Context](publishers/timeout/scheduler.md)
  The scheduler on which to deliver events.
- [let options: Context.SchedulerOptions?](publishers/timeout/options.md)
  Scheduler options that customize the delivery of elements.
- [let customError: (() -> Publishers.Timeout<Upstream, Context>.Failure)?](publishers/timeout/customerror.md)
  A closure that executes if the publisher times out. The publisher sends the failure returned by this closure to the subscriber as the reason for termination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/timeout/interval)*