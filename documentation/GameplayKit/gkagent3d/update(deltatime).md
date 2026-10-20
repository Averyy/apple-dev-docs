# update(deltaTime:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) updateWithDeltaTime:(NSTimeInterval) seconds;
```

#### Discussion

You call this method directly on an individual agent, or on all the agents in your game through a [`GKComponentSystem`](../gkcomponentsystem.md) object, whenever you want to run a step of the agent simulation. Typically, a game updates its agent simulation whenever it prepares to draw a new frame—for example, in the [`update(_:)`](../../SpriteKit/skscene/update%28_%29.md) method of a SpriteKit [`SKScene`](../../SpriteKit/skscene.md) object.

## See Also

### Running the Agent Simulation
- [var velocity: vector_float3](./velocity.md)
  The current velocity of the agent in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkagent3d/update(deltatime:))*