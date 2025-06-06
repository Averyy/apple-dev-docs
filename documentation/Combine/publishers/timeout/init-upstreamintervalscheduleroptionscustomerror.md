# init(upstream:interval:scheduler:options:customError:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that terminates publishing if the upstream publisher exceeds the specified time interval without producing an element.

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
init(upstream: Upstream, interval: Context.SchedulerTimeType.Stride, scheduler: Context, options: Context.SchedulerOptions?, customError: (() -> Publishers.Timeout<Upstream, Context>.Failure)?)
```

## Parameters

- `upstream`: The publisher from which this publisher receives elements.
- `interval`: The maximum time interval the publisher can go without emitting an element, expressed in the time system of the scheduler.
- `scheduler`: The scheduler on which to deliver events.
- `options`: Scheduler options that customize the delivery of elements.
- `customError`: A closure that executes if the publisher times out. The publisher sends the failure returned by this closure to the subscriber as the reason for termination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/timeout/init(upstream:interval:scheduler:options:customerror:))*