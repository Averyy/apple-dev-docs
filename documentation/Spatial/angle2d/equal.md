# ==(_:_:)

**Framework**: Spatial  
**Kind**: op

Returns a Boolean value that indicates whether two angles are equal.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
static func == (lhs: Angle2D, rhs: Angle2D) -> Bool
```

#### Return Value

A Boolean value that indicates whether two values are equal.

#### Discussion

> **Note**: That this operator compares the raw value of each angle and doesn’t normalize the values. For example, 360° doesn’t equal 0°.

## Parameters

- `lhs`: The left-hand-side value.
- `rhs`: The right-hand-side value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/angle2d/==(_:_:))*