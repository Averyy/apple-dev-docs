# obstacles(fromNodeBounds:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Converts each node into an obstacle by transforming its bounds into the scene’s coordinate system.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
class func obstacles(fromNodeBounds nodes: [SKNode]) -> [GKPolygonObstacle]
```

```objc
+ (NSArray<GKPolygonObstacle *> *) obstaclesFromNodeBounds:(NSArray<SKNode *> *) nodes;
```

## Return Value

An array of [`GKPolygonObstacle`](../../GameplayKit/gkpolygonobstacle.md) objects.

## Discussion

Use the array of obstacles to create an obstacle graph ([`GKObstacleGraph`](../../GameplayKit/gkobstaclegraph.md)) in GameplayKit. See [GameplayKit](../../GameplayKit/GameplayKit.md) and [GameplayKit Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Parameters

- `nodes`: An array of [`SKNode`](../sknode.md) objects.

## See Also

### Adding GameplayKit Behaviors
- [var entity: GKEntity?](./entity.md)
  The GameplayKit entity this node represents.
- [class func obstacles(fromNodePhysicsBodies: [SKNode]) -> [GKPolygonObstacle]](./obstacles%28fromnodephysicsbodies%29.md)
  Converts each node into an obstacle by transforming the node’s physics body shape into the scene’s coordinate system.
- [class func obstacles(fromSpriteTextures: [SKNode], accuracy: Float) -> [GKPolygonObstacle]](./obstacles%28fromspritetextures,accuracy%29.md)
  Turns each node into an obstacle by changing the node’s texture into a physics shape and converting it into the scene’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/obstacles(fromnodebounds:))*