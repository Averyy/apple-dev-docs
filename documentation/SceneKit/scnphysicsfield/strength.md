# strength

**Framework**: SceneKit  
**Kind**: property

A multiplier for the force that the field applies to objects in its area of effect.

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
var strength: CGFloat { get set }
```

#### Discussion

Each type of physics field defines its own behavior for strength values. For details, see the methods listed in Creating Physics Fields.

## See Also

- [var falloffExponent: CGFloat](scnphysicsfield/falloffexponent.md)
  An exponent that determines how the field’s strength diminishes with distance.
- [var minimumDistance: CGFloat](scnphysicsfield/minimumdistance.md)
  The minimum value for distance-based effects.
- [var isActive: Bool](scnphysicsfield/isactive.md)
  A Boolean value that determines whether the field’s effect is enabled.
- [var isExclusive: Bool](scnphysicsfield/isexclusive.md)
  A Boolean value that determines whether the field overrides other fields whose areas of effect it overlaps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/strength)*