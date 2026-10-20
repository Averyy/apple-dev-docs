# rotation

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The orientation of the agent in 3D space.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var rotation: matrix_float3x3 { get set }
```

```objc
@property (nonatomic, assign) matrix_float3x3 rotation;
```

#### Discussion

The agent updates its own position, rotation, and velocity according to its goals when you call its [`update(deltaTime:)`](./update%28deltatime%29.md) method.

However, you can still directly change the rotation of an agent. Do this when you want to move a static agent (that is, one with no goals) or override an agent’s behavior as a direct result of user input.

## See Also

### Managing an Agent’s Position and Orientation
- [var position: vector_float3](./position.md)
  The current position of the agent in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkagent3d/rotation)*