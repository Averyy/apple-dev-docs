# GKPolygonObstacle

**Framework**: GameplayKit  
**Kind**: class

A polygon-shaped impassable area in a 2D game world.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKPolygonObstacle
```

#### Overview

Polygon obstacles serve two purposes in GameplayKit: You can use polygon obstacles to construct a navigability graph of your game world (a [`GKObstacleGraph`](gkobstaclegraph.md) object) for use in pathfinding. You can also use polygon obstacles to define regions for agents ([`GKAgent`](gkagent.md) objects) to avoid, using the [`GKGoal`](gkgoal.md) method [`init(toAvoid:maxPredictionTime:)`](gkgoal/init(toavoid:maxpredictiontime:)-7oslq.md).

To easily create obstacles for use with a SpriteKit game, create and arrange a set of nodes that define the non-navigable regions of your game world. You can create such nodes programmatically, or use the SpriteKit Scene Editor in Xcode. If you’re already using nodes with physics bodies to keep sprites from entering those regions, you can reuse those nodes. Then, use the [`obstacles(fromNodeBounds:)`](https://developer.apple.com/documentation/SpriteKit/SKNode/obstacles(fromNodeBounds:)), [`obstacles(fromSpriteTextures:accuracy:)`](https://developer.apple.com/documentation/SpriteKit/SKNode/obstacles(fromSpriteTextures:accuracy:)), or [`obstacles(fromNodePhysicsBodies:)`](https://developer.apple.com/documentation/SpriteKit/SKNode/obstacles(fromNodePhysicsBodies:)) method to generate a set of [`GKPolygonObstacle`](gkpolygonobstacle.md) objects.

To learn more about both ways of using polygon obstacles, see [`Pathfinding`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/Pathfinding.html#//apple_ref/doc/uid/TP40015172-CH3) and [`Agents, Goals, and Behaviors`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/Agent.html#//apple_ref/doc/uid/TP40015172-CH8) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Inspecting Vertices
- [var vertexCount: Int](gkpolygonobstacle/vertexcount.md)
  The number of vertices that define the polygon-shaped area of the obstacle.
- [func vertex(at: Int) -> vector_float2](gkpolygonobstacle/vertex(at:).md)
  Returns the point coordinates of the specified vertex.
### Initializers
- [convenience init(points: [SIMD2<Float>])](gkpolygonobstacle/init(points:).md)

## Relationships

### Inherits From
- [GKObstacle](gkobstacle.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class GKObstacle](gkobstacle.md)
  The abstract base class for objects representing impassable areas in a game world.
- [class GKCircleObstacle](gkcircleobstacle.md)
  A circular impassable area to be avoided by agents.
- [class GKSphereObstacle](gksphereobstacle.md)
  A spherical impassable volume to be avoided by agents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkpolygonobstacle)*