# init(upstream:interval:tolerance:scheduler:options:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that delays delivery of elements and completion to the downstream receiver.

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
init(upstream: Upstream, interval: Context.SchedulerTimeType.Stride, tolerance: Context.SchedulerTimeType.Stride, scheduler: Context, options: Context.SchedulerOptions? = nil)
```

## Parameters

- `upstream`: The publisher from which this publisher receives its elements.
- `interval`: The amount of time to delay.
- `tolerance`: The allowed tolerance in delivering delayed events. The   publisher may deliver elements this much sooner or later than the interval specifies.
- `scheduler`: The scheduler to deliver the delayed events.
- `options`: Options relevant to the scheduler’s behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/delay/init(upstream:interval:tolerance:scheduler:options:))*