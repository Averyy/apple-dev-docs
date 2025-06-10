# ==(_:_:)

**Framework**: Spatial  
**Kind**: op

Returns a Boolean value indicating whether two angles are equal.

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
static func == (lhs: Angle2DFloat, rhs: Angle2DFloat) -> Bool
```

#### Discussion

Note that this operator compares the raw value of each angle and doesn’t normalize the values. For example, 360° does  0°.

## Parameters

- `lhs`: The first angle to compare.
- `rhs`: The second angle to compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/angle2dfloat/==(_:_:))*