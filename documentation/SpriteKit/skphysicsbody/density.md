# density

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The density of the object, in kilograms per square meter.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var density: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat density;
```

## Mentions

- [Configuring a Physics Body](../configuring-a-physics-body.md)

## Discussion

The actual unit is arbitrary as long as relative masses of objects are consistent throughout the game.

The [`mass`](./mass.md) and [`density`](./density.md) properties are interrelated. When you change the value of either property, the other property’s value is automatically recalculated to be consistent.

The default value is `1.0`.

## See Also

### Defining a Physics Body’s Physical Properties
- [Configuring a Physics Body](../configuring-a-physics-body.md)
  Move a physics body, and make it collide with other objects, by setting its physical properties once or changing them dynamically.
- [var mass: CGFloat](./mass.md)
  The mass of the body, in kilograms.
- [var area: CGFloat](./area.md)
  The area covered by the body.
- [var friction: CGFloat](./friction.md)
  The roughness of the surface of the physics body.
- [var restitution: CGFloat](./restitution.md)
  The bounciness of the physics body.
- [var linearDamping: CGFloat](./lineardamping.md)
  A property that reduces the body’s linear velocity.
- [var angularDamping: CGFloat](./angulardamping.md)
  A property that reduces the body’s rotational velocity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/density)*