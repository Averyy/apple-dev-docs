# speed

**Framework**: GameplayKit  
**Kind**: property

The agent’s current forward speed, in units per second.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var speed: Float { get set }
```

#### Discussion

This property measures only the agent’s speed in the direction it faces. The concrete subclasses of [`GKAgent`](gkagent.md) relate speed to orientation and position; see the [`velocity`](gkagent2d/velocity.md) ([`GKAgent2D`](gkagent2d.md)) or [`velocity`](gkagent3d/velocity.md) ([`GKAgent3D`](gkagent3d.md)) property for the appropriate subclass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkagent/speed)*