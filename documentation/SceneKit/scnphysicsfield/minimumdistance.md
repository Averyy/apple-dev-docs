# minimumDistance

**Framework**: SceneKit  
**Kind**: property

The minimum value for distance-based effects.

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
var minimumDistance: CGFloat { get set }
```

#### Discussion

This property determines the beginning of the field’s falloff area. At distances less than the minimum, the field’s effect is at full strength. At greater distances, the field’s effect diminishes based on the value of the [`falloffExponent`](scnphysicsfield/falloffexponent.md) property. The default minimum distance is a very small (but nonzero) value.

## See Also

- [var strength: CGFloat](scnphysicsfield/strength.md)
  A multiplier for the force that the field applies to objects in its area of effect.
- [var falloffExponent: CGFloat](scnphysicsfield/falloffexponent.md)
  An exponent that determines how the field’s strength diminishes with distance.
- [var isActive: Bool](scnphysicsfield/isactive.md)
  A Boolean value that determines whether the field’s effect is enabled.
- [var isExclusive: Bool](scnphysicsfield/isexclusive.md)
  A Boolean value that determines whether the field overrides other fields whose areas of effect it overlaps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/minimumdistance)*