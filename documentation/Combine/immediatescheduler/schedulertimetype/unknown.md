# ==(_:_:)

**Framework**: Combine  
**Kind**: op

Returns a Boolean value indicating whether two values are equal.

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
static func == (x: Self, y: Self) -> Bool
```

#### Discussion

Equality is the inverse of inequality. For any values `a` and `b`, `a == b` implies that `a != b` is `false`.

## Parameters

- `lhs`: A value to compare.
- `rhs`: Another value to compare.

## See Also

- [static func != (Self, Self) -> Bool](immediatescheduler/schedulertimetype/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func ... (Self) -> PartialRangeFrom<Self>](immediatescheduler/schedulertimetype/'...(_:)-6wy1j.md)
  Returns a partial range extending upward from a lower bound.
- [static func ... (Self) -> PartialRangeThrough<Self>](immediatescheduler/schedulertimetype/'...(_:)-5ai2g.md)
  Returns a partial range up to, and including, its upper bound.
- [static func ... (Self, Self) -> ClosedRange<Self>](immediatescheduler/schedulertimetype/'...(_:_:).md)
  Returns a closed range that contains both of its bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/immediatescheduler/schedulertimetype/==(_:_:))*