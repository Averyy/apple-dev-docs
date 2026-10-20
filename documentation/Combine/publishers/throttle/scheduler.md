# scheduler

**Framework**: Combine  
**Kind**: property  
**Role**: Instance Property

The scheduler on which to publish elements.

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
let scheduler: Context
```

## See Also

### Inspecting publisher properties
- [let upstream: Upstream](./upstream.md)
  The publisher from which this publisher receives elements.
- [let interval: Context.SchedulerTimeType.Stride](./interval.md)
  The interval in which to find and emit the most recent element.
- [let latest: Bool](./latest.md)
  A Boolean value indicating whether to publish the most recent element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/throttle/scheduler)*