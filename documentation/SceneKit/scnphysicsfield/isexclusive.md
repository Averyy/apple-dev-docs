# isExclusive

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the field overrides other fields whose areas of effect it overlaps.

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
var isExclusive: Bool { get set }
```

```objc
@property (nonatomic, getter=isExclusive) BOOL exclusive;
```

## Discussion

If this value is [`true`](../../Swift/true.md) and a physics body is within this field’s region, SceneKit ignores the effects of all other fields that might otherwise affect the body. The default value is [`false`](../../Swift/false.md).

If you set this property to [`true`](../../Swift/true.md) on multiple fields in a scene, their regions should not overlap. If they do, the results are undefined.

## See Also

### Specifying a Field’s Behavior
- [var strength: CGFloat](./strength.md)
  A multiplier for the force that the field applies to objects in its area of effect.
- [var falloffExponent: CGFloat](./falloffexponent.md)
  An exponent that determines how the field’s strength diminishes with distance.
- [var minimumDistance: CGFloat](./minimumdistance.md)
  The minimum value for distance-based effects.
- [var isActive: Bool](./isactive.md)
  A Boolean value that determines whether the field’s effect is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/isexclusive)*