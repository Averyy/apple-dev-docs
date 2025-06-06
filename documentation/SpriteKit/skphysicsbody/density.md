# density

**Framework**: SpriteKit  
**Kind**: property

The density of the object, in kilograms per square meter.

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
var density: CGFloat { get set }
```

## Mentions

- [Configuring a Physics Body](configuring-a-physics-body.md)

#### Discussion

The actual unit is arbitrary as long as relative masses of objects are consistent throughout the game.

The [`mass`](skphysicsbody/mass.md) and [`density`](skphysicsbody/density.md) properties are interrelated. When you change the value of either property, the other property’s value is automatically recalculated to be consistent.

The default value is `1.0`.

## See Also

- [Configuring a Physics Body](configuring-a-physics-body.md)
  Move a physics body, and make it collide with other objects, by setting its physical properties once or changing them dynamically.
- [var mass: CGFloat](skphysicsbody/mass.md)
  The mass of the body, in kilograms.
- [var area: CGFloat](skphysicsbody/area.md)
  The area covered by the body.
- [var friction: CGFloat](skphysicsbody/friction.md)
  The roughness of the surface of the physics body.
- [var restitution: CGFloat](skphysicsbody/restitution.md)
  The bounciness of the physics body.
- [var linearDamping: CGFloat](skphysicsbody/lineardamping.md)
  A property that reduces the body’s linear velocity.
- [var angularDamping: CGFloat](skphysicsbody/angulardamping.md)
  A property that reduces the body’s rotational velocity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/density)*