# update(deltaTime:)

**Framework**: GameplayKit  
**Kind**: method

Causes the agent to evaluate its goals and update its position, rotation, and velocity accordingly.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func update(deltaTime seconds: TimeInterval)
```

#### Discussion

You call this method directly on an individual agent, or on all the agents in your game through a [`GKComponentSystem`](gkcomponentsystem.md) object, whenever you want to run a step of the agent simulation. Typically, a game updates its agent simulation whenever it prepares to draw a new frame—for example, in the [`update(_:)`](https://developer.apple.com/documentation/SpriteKit/SKScene/update(_:)) method of a SpriteKit [`SKScene`](https://developer.apple.com/documentation/SpriteKit/SKScene) object.

## See Also

- [var velocity: vector_float2](gkagent2d/velocity.md)
  The current velocity of the agent in 2D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkagent2d/update(deltatime:))*