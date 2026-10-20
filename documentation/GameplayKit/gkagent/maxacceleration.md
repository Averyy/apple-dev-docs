# maxAcceleration

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The upper limit to changes in the agent’s speed or direction.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var maxAcceleration: Float { get set }
```

```objc
@property (nonatomic) float maxAcceleration;
```

#### Discussion

When an agent evaluates the goals listed in its [`behavior`](./behavior.md) property, the result is an acceleration vector that changes the position and direction of the agent. If the magnitude of that vector, in units per second per second, is greater than this value, its effect is limited to this value. An agent with a low maximum acceleration will be slow to change speed and direction; an agent with a high maximum acceleration can start moving, stop, and turn more quickly.

## See Also

### Constraining an Agent’s Movement
- [var mass: Float](./mass.md)
  The resistance of the agent to changes in speed or direction.
- [var maxSpeed: Float](./maxspeed.md)
  The agent’s maximum forward speed, in units per second.
- [var radius: Float](./radius.md)
  The agent’s radius.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkagent/maxacceleration)*