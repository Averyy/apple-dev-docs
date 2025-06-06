# agentDidUpdate(_:)

**Framework**: GameplayKit  
**Kind**: method

Tells the delegate that an agent has just performed a simulation step.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func agentDidUpdate(_ agent: GKAgent)
```

#### Discussion

Implement this method when you want to update a display based on the latest data from the agent simulation. Read the [`position`](gkagent2d/position.md) and [`rotation`](gkagent2d/rotation.md) properties of the agent (as a [`GKAgent2D`](gkagent2d.md) or [`GKAgent3D`](gkagent3d.md) object), then set the corresponding attributes of the object that provides the agent’s visual representation.

## Parameters

- `agent`: The agent object that has just performed a simulation step.

## See Also

- [func agentWillUpdate(GKAgent)](gkagentdelegate/agentwillupdate(_:).md)
  Tells the delegate that an agent is about to perform its next simulation step.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkagentdelegate/agentdidupdate(_:))*