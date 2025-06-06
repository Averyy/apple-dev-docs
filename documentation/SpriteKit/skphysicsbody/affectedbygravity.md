# affectedByGravity

**Framework**: SpriteKit  
**Kind**: property

A Boolean value that indicates whether this physics body is affected by the physics world’s gravity.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var affectedByGravity: Bool { get set }
```

#### Discussion

The physics world’s [`gravity`](skphysicsworld/gravity.md) property defines the gravitational forces applied to volume-based bodies in the scene.

The default value is `true`. This property is ignored on edge-based bodies, which are always unaffected by gravity.

Physics bodies with `affectedByGravity` set to `false` are still affected by the gravity fields created by [`linearGravityField(withVector:)`](skfieldnode/lineargravityfield(withvector:).md) and [`radialGravityField()`](skfieldnode/radialgravityfield().md).

## See Also

- [var allowsRotation: Bool](skphysicsbody/allowsrotation.md)
  A Boolean value that indicates whether the physics body is affected by angular forces and impulses applied to it.
- [var isDynamic: Bool](skphysicsbody/isdynamic.md)
  A Boolean value that indicates whether the physics body is moved by the physics simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/affectedbygravity)*