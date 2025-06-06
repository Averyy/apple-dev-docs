# isActive

**Framework**: SceneKit  
**Kind**: property

A Boolean value that determines whether the field’s effect is enabled.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var isActive: Bool { get set }
```

#### Discussion

If this value is [`false`](https://developer.apple.com/documentation/swift/false), the field does not apply forces to physics bodies in its area of effect. The default value is [`true`](https://developer.apple.com/documentation/swift/true).

Use this property, for example, to switch fields on and off as a gameplay mechanic.

## See Also

- [var strength: CGFloat](scnphysicsfield/strength.md)
  A multiplier for the force that the field applies to objects in its area of effect.
- [var falloffExponent: CGFloat](scnphysicsfield/falloffexponent.md)
  An exponent that determines how the field’s strength diminishes with distance.
- [var minimumDistance: CGFloat](scnphysicsfield/minimumdistance.md)
  The minimum value for distance-based effects.
- [var isExclusive: Bool](scnphysicsfield/isexclusive.md)
  A Boolean value that determines whether the field overrides other fields whose areas of effect it overlaps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/isactive)*