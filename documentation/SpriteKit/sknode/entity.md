# entity

**Framework**: SpriteKit  
**Kind**: property

The GameplayKit entity this node represents.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var entity: GKEntity? { get set }
```

#### Discussion

The Entity-Component architecture in the GameplayKit framework is a way to more easily manage complex object graphs in your game. For more information on this architecture, read [`Entities and Components`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/EntityComponent.html#//apple_ref/doc/uid/TP40015172-CH6) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

When you add entities (and their components) to a scene in the Xcode SpriteKit Scene Editor, Xcode automatically  archive those entities alongside the SpriteKit scene content. Use the [`GKScene`](https://developer.apple.com/documentation/GameplayKit/GKScene) class to load the SpriteKit scene with its associated GameplayKit objects. Each entity associated with a SpriteKit node has a [`GKSKNodeComponent`](https://developer.apple.com/documentation/GameplayKit/GKSKNodeComponent) object that manages the relationship between the node and the [`GKEntity`](https://developer.apple.com/documentation/GameplayKit/GKEntity) object it represents.

## See Also

- [class func obstacles(fromNodeBounds: [SKNode]) -> [GKPolygonObstacle]](sknode/obstacles(fromnodebounds:).md)
  Converts each node into an obstacle by transforming its bounds into the scene’s coordinate system.
- [class func obstacles(fromNodePhysicsBodies: [SKNode]) -> [GKPolygonObstacle]](sknode/obstacles(fromnodephysicsbodies:).md)
  Converts each node into an obstacle by transforming the node’s physics body shape into the scene’s coordinate system.
- [class func obstacles(fromSpriteTextures: [SKNode], accuracy: Float) -> [GKPolygonObstacle]](sknode/obstacles(fromspritetextures:accuracy:).md)
  Turns each node into an obstacle by changing the node’s texture into a physics shape and converting it into the scene’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/entity)*