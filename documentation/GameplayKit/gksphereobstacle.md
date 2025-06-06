# GKSphereObstacle

**Framework**: GameplayKit  
**Kind**: class

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

#### Overview

To make agents ([`GKAgent`](gkagent.md) objects) avoid obstacles, create a goal with the [`init(toAvoid:maxPredictionTime:)`](gkgoal/init(toavoid:maxpredictiontime:)-7oslq.md) method. Agents affected by an avoid-obstacles goal will attempt to move such that their radius never overlaps that of a spherical obstacle.

To learn more about using goals and agents, see [`Agents, Goals, and Behaviors`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/Agent.html#//apple_ref/doc/uid/TP40015172-CH8) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Creating an Obstacle
- [init(radius: Float)](gksphereobstacle/init(radius:).md)
  Initializes a spherical obstacle with the specified radius.
### Placing an Obstacle
- [var position: vector_float3](gksphereobstacle/position.md)
  The position of the obstacle.
- [var radius: Float](gksphereobstacle/radius.md)
  The radius of the obstacle.

## Relationships

### Inherits From
- [GKObstacle](gkobstacle.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GKObstacle](gkobstacle.md)
  The abstract base class for objects representing impassable areas in a game world.
- [class GKCircleObstacle](gkcircleobstacle.md)
  A circular impassable area to be avoided by agents.
- [class GKPolygonObstacle](gkpolygonobstacle.md)
  A polygon-shaped impassable area in a 2D game world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gksphereobstacle)*