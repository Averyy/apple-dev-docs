# <(_:_:)

**Framework**: Foundation  
**Kind**: op

Compare two measurements of the same `Unit`.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static func < <LeftHandSideType, RightHandSideType>(lhs: Measurement<LeftHandSideType>, rhs: Measurement<RightHandSideType>) -> Bool where LeftHandSideType : Unit, RightHandSideType : Unit
```

#### Return Value

`true` if the measurements can be compared and the `lhs` is less than the `rhs` converted value.

## See Also

- [static func > (Self, Self) -> Bool](measurement/_(_:_:)-648pf.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [static func >= (Self, Self) -> Bool](measurement/_=(_:_:)-lnsg.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [static func <= (Self, Self) -> Bool](measurement/_=(_:_:)-12fhs.md)
  Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/_(_:_:)-7pou4)*