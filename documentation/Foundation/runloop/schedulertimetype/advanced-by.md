# advanced(by:)

**Framework**: Foundation  
**Kind**: method

Returns a run loop scheduler time calculated by advancing this instance’s time by the given interval.

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
func advanced(by n: RunLoop.SchedulerTimeType.Stride) -> RunLoop.SchedulerTimeType
```

#### Return Value

A dispatch queue time advanced by the given interval from this instance’s time.

## Parameters

- `n`: A time interval to advance.

## See Also

- [RunLoop.SchedulerTimeType.Stride](runloop/schedulertimetype/stride.md)
  The interval by which run loop times advance.
- [func distance(to: RunLoop.SchedulerTimeType) -> RunLoop.SchedulerTimeType.Stride](runloop/schedulertimetype/distance(to:).md)
  Returns the distance to another run loop scheduler time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/schedulertimetype/advanced(by:))*