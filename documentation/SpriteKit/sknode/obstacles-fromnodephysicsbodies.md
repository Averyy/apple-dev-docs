# obstacles(fromNodePhysicsBodies:)

**Framework**: SpriteKit  
**Kind**: method

Converts each node into an obstacle by transforming the node’s physics body shape into the scene’s coordinate system.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
class func obstacles(fromNodePhysicsBodies nodes: [SKNode]) -> [GKPolygonObstacle]
```

#### Return Value

An array of [`GKPolygonObstacle`](https://developer.apple.com/documentation/GameplayKit/GKPolygonObstacle) objects.

#### Discussion

Use the array of obstacles to create an obstacle graph ([`GKObstacleGraph`](https://developer.apple.com/documentation/GameplayKit/GKObstacleGraph)) in GameplayKit. See [`GameplayKit`](https://developer.apple.com/documentation/GameplayKit) and [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Parameters

- `nodes`: An array of   objects.

## See Also

- [var entity: GKEntity?](sknode/entity.md)
  The GameplayKit entity this node represents.
- [class func obstacles(fromNodeBounds: [SKNode]) -> [GKPolygonObstacle]](sknode/obstacles(fromnodebounds:).md)
  Converts each node into an obstacle by transforming its bounds into the scene’s coordinate system.
- [class func obstacles(fromSpriteTextures: [SKNode], accuracy: Float) -> [GKPolygonObstacle]](sknode/obstacles(fromspritetextures:accuracy:).md)
  Turns each node into an obstacle by changing the node’s texture into a physics shape and converting it into the scene’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/obstacles(fromnodephysicsbodies:))*