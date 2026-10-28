# area

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The area covered by the body.

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
var area: CGFloat { get }
```

```objc
@property (nonatomic, readonly) CGFloat area;
```

## Mentions

- [Configuring a Physics Body](../configuring-a-physics-body.md)

## Discussion

This property is used in conjunction with the [`density`](./density.md) property to calculate the body’s mass.

The value returned for the area is measured in meters: if you need to convert it into points — as used by SpriteKit — multiply the values by 150². The following listing shows how to calculate the area of a box which is ten points square.

```objc
let bodySize = CGSize(width: 10, height: 10)
let physicsBody = SKPhysicsBody(rectangleOf: bodySize)
let areaInPoints = physicsBody.area * pow(150, 2) // areaInPoints = 100
```

## See Also

### Defining a Physics Body’s Physical Properties
- [Configuring a Physics Body](../configuring-a-physics-body.md)
  Move a physics body, and make it collide with other objects, by setting its physical properties once or changing them dynamically.
- [var mass: CGFloat](./mass.md)
  The mass of the body, in kilograms.
- [var density: CGFloat](./density.md)
  The density of the object, in kilograms per square meter.
- [var friction: CGFloat](./friction.md)
  The roughness of the surface of the physics body.
- [var restitution: CGFloat](./restitution.md)
  The bounciness of the physics body.
- [var linearDamping: CGFloat](./lineardamping.md)
  A property that reduces the body’s linear velocity.
- [var angularDamping: CGFloat](./angulardamping.md)
  A property that reduces the body’s rotational velocity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/area)*