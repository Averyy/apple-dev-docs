# GKSphereObstacle

**Framework**: GameplayKit  
**Kind**: class  
**Role**: Class

A spherical impassable volume to be avoided by agents.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class GKSphereObstacle
```

```objc
@interface GKSphereObstacle : GKObstacle
```

## Overview

To make agents ([`GKAgent`](./gkagent.md) objects) avoid obstacles, create a goal with the [`init(toAvoid:maxPredictionTime:)`](./gkgoal/init%28toavoid,maxpredictiontime%29-7oslq.md) method. Agents affected by an avoid-obstacles goal will attempt to move such that their radius never overlaps that of a spherical obstacle.

To learn more about using goals and agents, see [Agents, Goals, and Behaviors](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/Agent.html#//apple_ref/doc/uid/TP40015172-CH8) in [GameplayKit Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Creating an Obstacle
- [init(radius: Float)](./gksphereobstacle/init%28radius%29.md)
  Initializes a spherical obstacle with the specified radius.
- [+ obstacleWithRadius:](./gksphereobstacle/obstaclewithradius_.md)
  Creates a spherical obstacle with the specified radius.
### Placing an Obstacle
- [var position: vector_float3](./gksphereobstacle/position.md)
  The position of the obstacle.
- [var radius: Float](./gksphereobstacle/radius.md)
  The radius of the obstacle.

## Relationships

### Inherits From
- [GKObstacle](./gkobstacle.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Obstacles
- [class GKObstacle](./gkobstacle.md)
  The abstract base class for objects representing impassable areas in a game world.
- [class GKCircleObstacle](./gkcircleobstacle.md)
  A circular impassable area to be avoided by agents.
- [class GKPolygonObstacle](./gkpolygonobstacle.md)
  A polygon-shaped impassable area in a 2D game world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gksphereobstacle)*