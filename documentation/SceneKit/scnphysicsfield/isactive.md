# isActive

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the field’s effect is enabled.

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
var isActive: Bool { get set }
```

```objc
@property (nonatomic, getter=isActive) BOOL active;
```

#### Discussion

If this value is [`false`](../../Swift/false.md), the field does not apply forces to physics bodies in its area of effect. The default value is [`true`](../../Swift/true.md).

Use this property, for example, to switch fields on and off as a gameplay mechanic.

## See Also

### Specifying a Field’s Behavior
- [var strength: CGFloat](./strength.md)
  A multiplier for the force that the field applies to objects in its area of effect.
- [var falloffExponent: CGFloat](./falloffexponent.md)
  An exponent that determines how the field’s strength diminishes with distance.
- [var minimumDistance: CGFloat](./minimumdistance.md)
  The minimum value for distance-based effects.
- [var isExclusive: Bool](./isexclusive.md)
  A Boolean value that determines whether the field overrides other fields whose areas of effect it overlaps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/isactive)*