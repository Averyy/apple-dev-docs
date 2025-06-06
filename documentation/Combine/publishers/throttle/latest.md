# latest

**Framework**: Combine  
**Kind**: property

A Boolean value indicating whether to publish the most recent element.

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
let latest: Bool
```

#### Discussion

If `false`, the publisher emits the first element received during the interval.

## See Also

- [let upstream: Upstream](publishers/throttle/upstream.md)
  The publisher from which this publisher receives elements.
- [let interval: Context.SchedulerTimeType.Stride](publishers/throttle/interval.md)
  The interval in which to find and emit the most recent element.
- [let scheduler: Context](publishers/throttle/scheduler.md)
  The scheduler on which to publish elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/throttle/latest)*