# restitution

**Framework**: SpriteKit  
**Kind**: property

The bounciness of the physics body.

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
var restitution: CGFloat { get set }
```

#### Discussion

This property is used to determine how much energy the physics body loses when it bounces off another object. The property must be a value between `0.0` and `1.0`. The default value is `0.2`.

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
- [var linearDamping: CGFloat](skphysicsbody/lineardamping.md)
  A property that reduces the body’s linear velocity.
- [var angularDamping: CGFloat](skphysicsbody/angulardamping.md)
  A property that reduces the body’s rotational velocity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/restitution)*