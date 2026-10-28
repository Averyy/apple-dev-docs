# rotation

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The rotation of the agent around the z-axis.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var rotation: Float { get set }
```

```objc
@property (nonatomic) float rotation;
```

## Discussion

The agent updates its own position, rotation, and velocity according to its goals when you call its [`update(deltaTime:)`](./update%28deltatime%29.md) method.

However, you can still directly change the rotation of an agent. Do this when you want to move a static agent (that is, one with no goals) or override an agent’s behavior as a direct result of user input.

## See Also

### Managing an Agent’s Position and Orientation
- [var position: vector_float2](./position.md)
  The current position of the agent in 2D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkagent2d/rotation)*