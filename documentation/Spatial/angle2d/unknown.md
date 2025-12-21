# <(_:_:)

**Framework**: Spatial  
**Kind**: op

Returns `true` if `lhs.degrees` is less than `rhs.degrees`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static func < (lhs: Angle2D, rhs: Angle2D) -> Bool
```

#### Discussion

Note that this operator compares the raw value of each angle and doesn’t normalize the values. For example, 360° does  equal 0°.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/angle2d/_(_:_:))*