# minimumDistance

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The minimum value for distance-based effects.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var minimumDistance: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat minimumDistance;
```

## Discussion

This property determines the beginning of the field’s falloff area. At distances less than the minimum, the field’s effect is at full strength. At greater distances, the field’s effect diminishes based on the value of the [`falloffExponent`](./falloffexponent.md) property. The default minimum distance is a very small (but nonzero) value.

## See Also

### Specifying a Field’s Behavior
- [var strength: CGFloat](./strength.md)
  A multiplier for the force that the field applies to objects in its area of effect.
- [var falloffExponent: CGFloat](./falloffexponent.md)
  An exponent that determines how the field’s strength diminishes with distance.
- [var isActive: Bool](./isactive.md)
  A Boolean value that determines whether the field’s effect is enabled.
- [var isExclusive: Bool](./isexclusive.md)
  A Boolean value that determines whether the field overrides other fields whose areas of effect it overlaps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/minimumdistance)*