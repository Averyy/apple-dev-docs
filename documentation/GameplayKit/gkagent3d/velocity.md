# velocity

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The current velocity of the agent in 3D space.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var velocity: vector_float3 { get }
```

```objc
@property (nonatomic, readonly) vector_float3 velocity;
```

#### Discussion

An agent’s velocity is a calculated property—the velocity vector is determined by an agent’s facing direction (its [`rotation`](./rotation.md) property) and its [`speed`](../gkagent/speed.md) property.

## See Also

### Running the Agent Simulation
- [func update(deltaTime: TimeInterval)](./update%28deltatime%29.md)
  Causes the agent to evaluate its goals and update its position, rotation, and velocity accordingly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkagent3d/velocity)*