# GKObstacle

**Framework**: GameplayKit  
**Kind**: class

The abstract base class for objects representing impassable areas in a game world.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKObstacle
```

#### Overview

You do not use this class directly; instead, create instances of its concrete subclasses [`GKCircleObstacle`](gkcircleobstacle.md), [`GKSphereObstacle`](gksphereobstacle.md), and [`GKPolygonObstacle`](gkpolygonobstacle.md). To make agents ([`GKAgent`](gkagent.md) objects) avoid obstacles, create a goal with the goalToAvoidObstacles:timeBeforeCollisionToAvoid: method.

To learn more about using goals and agents, see [`Agents, Goals, and Behaviors`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/Agent.html#//apple_ref/doc/uid/TP40015172-CH8) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

For more information, see [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [GKCircleObstacle](gkcircleobstacle.md)
- [GKPolygonObstacle](gkpolygonobstacle.md)
- [GKSphereObstacle](gksphereobstacle.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GKCircleObstacle](gkcircleobstacle.md)
  A circular impassable area to be avoided by agents.
- [class GKSphereObstacle](gksphereobstacle.md)
  A spherical impassable volume to be avoided by agents.
- [class GKPolygonObstacle](gkpolygonobstacle.md)
  A polygon-shaped impassable area in a 2D game world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkobstacle)*