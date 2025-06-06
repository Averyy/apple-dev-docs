# <=(_:_:)

**Framework**: Foundation  
**Kind**: op

Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static func <= (lhs: Self, rhs: Self) -> Bool
```

#### Discussion

This is the default implementation of the less-than-or-equal-to operator (`<=`) for any type that conforms to `Comparable`.

## Parameters

- `lhs`: A value to compare.
- `rhs`: Another value to compare.

## See Also

- [static func > (Self, Self) -> Bool](measurement/_(_:_:)-648pf.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [static func >= (Self, Self) -> Bool](measurement/_=(_:_:)-lnsg.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [static func < <LeftHandSideType, RightHandSideType>(Measurement<LeftHandSideType>, Measurement<RightHandSideType>) -> Bool](measurement/_(_:_:)-7pou4.md)
  Compare two measurements of the same `Unit`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/_=(_:_:)-12fhs)*