# isExclusive

**Framework**: SceneKit  
**Kind**: property

A Boolean value that determines whether the field overrides other fields whose areas of effect it overlaps.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var isExclusive: Bool { get set }
```

#### Discussion

If this value is [`true`](https://developer.apple.com/documentation/swift/true) and a physics body is within this field’s region, SceneKit ignores the effects of all other fields that might otherwise affect the body. The default value is [`false`](https://developer.apple.com/documentation/swift/false).

If you set this property to [`true`](https://developer.apple.com/documentation/swift/true) on multiple fields in a scene, their regions should not overlap. If they do, the results are undefined.

## See Also

- [var strength: CGFloat](scnphysicsfield/strength.md)
  A multiplier for the force that the field applies to objects in its area of effect.
- [var falloffExponent: CGFloat](scnphysicsfield/falloffexponent.md)
  An exponent that determines how the field’s strength diminishes with distance.
- [var minimumDistance: CGFloat](scnphysicsfield/minimumdistance.md)
  The minimum value for distance-based effects.
- [var isActive: Bool](scnphysicsfield/isactive.md)
  A Boolean value that determines whether the field’s effect is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/isexclusive)*