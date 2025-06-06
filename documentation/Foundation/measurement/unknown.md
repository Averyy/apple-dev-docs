# ==(_:_:)

**Framework**: Foundation  
**Kind**: op

Compare two measurements of the same `Dimension`.

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
static func == <LeftHandSideType, RightHandSideType>(lhs: Measurement<LeftHandSideType>, rhs: Measurement<RightHandSideType>) -> Bool where LeftHandSideType : Unit, RightHandSideType : Unit
```

#### Return Value

`true` if the measurements are equal.

#### Discussion

If `lhs.unit == rhs.unit`, returns `lhs.value == rhs.value`. Otherwise, converts `rhs` to the same unit as `lhs` and then compares the resulting values.

## See Also

- [static func != (Self, Self) -> Bool](measurement/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/==(_:_:))*