# linearDamping

**Framework**: SpriteKit  
**Kind**: property

A property that reduces the body’s linear velocity.

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
var linearDamping: CGFloat { get set }
```

#### Discussion

This property is used to simulate fluid or air friction forces on the body. The property must be a value between `0.0` and `1.0`. The default value is `0.1`. If the value is `0.0`, no linear damping is applied to the object.

## See Also

- [Configuring a Physics Body](configuring-a-physics-body.md)
  Move a physics body, and make it collide with other objects, by setting its physical properties once or changing them dynamically.
- [var mass: CGFloat](skphysicsbody/mass.md)
  The mass of the body, in kilograms.
- [var density: CGFloat](skphysicsbody/density.md)
  The density of the object, in kilograms per square meter.
- [var area: CGFloat](skphysicsbody/area.md)
  The area covered by the body.
- [var friction: CGFloat](skphysicsbody/friction.md)
  The roughness of the surface of the physics body.
- [var restitution: CGFloat](skphysicsbody/restitution.md)
  The bounciness of the physics body.
- [var angularDamping: CGFloat](skphysicsbody/angulardamping.md)
  A property that reduces the body’s rotational velocity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/lineardamping)*