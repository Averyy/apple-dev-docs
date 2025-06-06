# velocity

**Framework**: GameplayKit  
**Kind**: property

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

#### Discussion

An agent’s velocity is a calculated property—the velocity vector is determined by an agent’s facing direction (its [`rotation`](gkagent3d/rotation.md) property) and its [`speed`](gkagent/speed.md) property.

## See Also

- [func update(deltaTime: TimeInterval)](gkagent3d/update(deltatime:).md)
  Causes the agent to evaluate its goals and update its position, rotation, and velocity accordingly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkagent3d/velocity)*