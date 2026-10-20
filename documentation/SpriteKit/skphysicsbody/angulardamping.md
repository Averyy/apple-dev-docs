# angularDamping

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

A property that reduces the body’s rotational velocity.

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
var angularDamping: CGFloat { get set }
```

```objc
@property (nonatomic, assign) CGFloat angularDamping;
```

## Mentions

- [Pinning and Rotating Physics Bodies](../pinning-and-rotating-physics-bodies.md)

#### Discussion

This property is used to simulate fluid or air friction forces on the body. The property must be a value between `0.0` and `1.0`. The default value is `0.1`. If the value is `0.0`, no angular damping is applied to the object.

## See Also

### Defining a Physics Body’s Physical Properties
- [Configuring a Physics Body](../configuring-a-physics-body.md)
  Move a physics body, and make it collide with other objects, by setting its physical properties once or changing them dynamically.
- [var mass: CGFloat](./mass.md)
  The mass of the body, in kilograms.
- [var density: CGFloat](./density.md)
  The density of the object, in kilograms per square meter.
- [var area: CGFloat](./area.md)
  The area covered by the body.
- [var friction: CGFloat](./friction.md)
  The roughness of the surface of the physics body.
- [var restitution: CGFloat](./restitution.md)
  The bounciness of the physics body.
- [var linearDamping: CGFloat](./lineardamping.md)
  A property that reduces the body’s linear velocity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/angulardamping)*