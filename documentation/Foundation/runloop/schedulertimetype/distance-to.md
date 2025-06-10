# distance(to:)

**Framework**: Foundation  
**Kind**: method

Returns the distance to another run loop scheduler time.

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
func distance(to other: RunLoop.SchedulerTimeType) -> RunLoop.SchedulerTimeType.Stride
```

#### Return Value

The time interval between this time and the provided time.

## Parameters

- `other`: Another run loop time.

## See Also

- [RunLoop.SchedulerTimeType.Stride](runloop/schedulertimetype/stride.md)
  The interval by which run loop times advance.
- [func advanced(by: RunLoop.SchedulerTimeType.Stride) -> RunLoop.SchedulerTimeType](runloop/schedulertimetype/advanced(by:).md)
  Returns a run loop scheduler time calculated by advancing this instance’s time by the given interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/schedulertimetype/distance(to:))*