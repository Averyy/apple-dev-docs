# <(_:_:)

**Framework**: Spatial  
**Kind**: op

Returns `true` if `lhs.degrees` is less than `rhs.degrees`.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
static func < (lhs: Angle2D, rhs: Angle2D) -> Bool
```

#### Discussion

Note that this operator compares the raw value of each angle and doesn’t normalize the values. For example, 360° does  equal 0°.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/angle2d/_(_:_:))*