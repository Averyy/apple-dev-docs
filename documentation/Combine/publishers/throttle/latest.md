# latest

**Framework**: Combine  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

If `false`, the publisher emits the first element received during the interval.

## See Also

### Inspecting publisher properties
- [let upstream: Upstream](./upstream.md)
  The publisher from which this publisher receives elements.
- [let interval: Context.SchedulerTimeType.Stride](./interval.md)
  The interval in which to find and emit the most recent element.
- [let scheduler: Context](./scheduler.md)
  The scheduler on which to publish elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/throttle/latest)*