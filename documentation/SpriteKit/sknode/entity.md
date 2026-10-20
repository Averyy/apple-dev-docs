# entity

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

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
weak var entity: GKEntity? { get set }
```

```objc
@property (nonatomic, weak) GKEntity * entity;
```

#### Discussion

The Entity-Component architecture in the GameplayKit framework is a way to more easily manage complex object graphs in your game. For more information on this architecture, read [Entities and Components](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/EntityComponent.html#//apple_ref/doc/uid/TP40015172-CH6) in [GameplayKit Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

When you add entities (and their components) to a scene in the Xcode SpriteKit Scene Editor, Xcode automatically  archive those entities alongside the SpriteKit scene content. Use the [`GKScene`](../../GameplayKit/gkscene.md) class to load the SpriteKit scene with its associated GameplayKit objects. Each entity associated with a SpriteKit node has a [`GKSKNodeComponent`](../../GameplayKit/gksknodecomponent.md) object that manages the relationship between the node and the [`GKEntity`](../../GameplayKit/gkentity.md) object it represents.

## See Also

### Adding GameplayKit Behaviors
- [class func obstacles(fromNodeBounds: [SKNode]) -> [GKPolygonObstacle]](./obstacles%28fromnodebounds%29.md)
  Converts each node into an obstacle by transforming its bounds into the scene’s coordinate system.
- [class func obstacles(fromNodePhysicsBodies: [SKNode]) -> [GKPolygonObstacle]](./obstacles%28fromnodephysicsbodies%29.md)
  Converts each node into an obstacle by transforming the node’s physics body shape into the scene’s coordinate system.
- [class func obstacles(fromSpriteTextures: [SKNode], accuracy: Float) -> [GKPolygonObstacle]](./obstacles%28fromspritetextures,accuracy%29.md)
  Turns each node into an obstacle by changing the node’s texture into a physics shape and converting it into the scene’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/entity)*