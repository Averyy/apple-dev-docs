# <(_:_:)

**Framework**: Combine  
**Kind**: op

Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.

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
static func < (lhs: ImmediateScheduler.SchedulerTimeType.Stride, rhs: ImmediateScheduler.SchedulerTimeType.Stride) -> Bool
```

#### Discussion

This function is the only requirement of the `Comparable` protocol. The remainder of the relational operator functions are implemented by the standard library for any type that conforms to `Comparable`.

## Parameters

- `lhs`: A value to compare.
- `rhs`: Another value to compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/immediatescheduler/schedulertimetype/stride/_(_:_:))*