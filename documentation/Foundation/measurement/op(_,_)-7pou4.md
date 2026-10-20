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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/_(_:_:)-7pou4)*