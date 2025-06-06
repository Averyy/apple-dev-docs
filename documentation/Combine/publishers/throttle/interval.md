# interval

**Framework**: Combine  
**Kind**: property

The interval in which to find and emit the most recent element.

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

- [let upstream: Upstream](publishers/throttle/upstream.md)
  The publisher from which this publisher receives elements.
- [let scheduler: Context](publishers/throttle/scheduler.md)
  The scheduler on which to publish elements.
- [let latest: Bool](publishers/throttle/latest.md)
  A Boolean value indicating whether to publish the most recent element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/throttle/interval)*