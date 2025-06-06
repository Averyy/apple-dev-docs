# agentWillUpdate(_:)

**Framework**: GameplayKit  
**Kind**: method

Tells the delegate that an agent is about to perform its next simulation step.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func agentWillUpdate(_ agent: GKAgent)
```

#### Discussion

Implement this method when you want to update the agent simulation with data from an external source, such as node position and orientation information updated by the SceneKit or SpriteKit physics engine. Set the [`position`](gkagent2d/position.md) and [`rotation`](gkagent2d/rotation.md) properties of the agent (as a [`GKAgent2D`](gkagent2d.md) or [`GKAgent3D`](gkagent3d.md) object) so that the next simulation step will take your changes to those properties into account.

For more information, see [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Parameters

- `agent`: The agent object that will perform its next simulation step.

## See Also

- [func agentDidUpdate(GKAgent)](gkagentdelegate/agentdidupdate(_:).md)
  Tells the delegate that an agent has just performed a simulation step.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkagentdelegate/agentwillupdate(_:))*