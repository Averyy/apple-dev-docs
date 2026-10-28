# strength

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A multiplier for the force that the field applies to objects in its area of effect.

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
var strength: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat strength;
```

## Discussion

Each type of physics field defines its own behavior for strength values. For details, see the methods listed in Creating Physics Fields.

## See Also

### Specifying a Field’s Behavior
- [var falloffExponent: CGFloat](./falloffexponent.md)
  An exponent that determines how the field’s strength diminishes with distance.
- [var minimumDistance: CGFloat](./minimumdistance.md)
  The minimum value for distance-based effects.
- [var isActive: Bool](./isactive.md)
  A Boolean value that determines whether the field’s effect is enabled.
- [var isExclusive: Bool](./isexclusive.md)
  A Boolean value that determines whether the field overrides other fields whose areas of effect it overlaps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/strength)*