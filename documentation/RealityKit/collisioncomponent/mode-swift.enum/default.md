# CollisionComponent.Mode.default

**Framework**: RealityKit  
**Kind**: case

A default collision object.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
case `default`
```

#### Discussion

When two objects of this type collide, RealityKit computes the full contact details (contact points, normal vectors, penetration depths, and so on) and stores them in the contact set.

> **Note**: Collisions will fall through and do not collide by default, to enable colliding see the [`CollisionComponent.Mode.colliding`](collisioncomponent/mode-swift.enum/colliding.md) mode.

## See Also

- [CollisionComponent.Mode.trigger](collisioncomponent/mode-swift.enum/trigger.md)
  A trigger collision object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisioncomponent/mode-swift.enum/default)*