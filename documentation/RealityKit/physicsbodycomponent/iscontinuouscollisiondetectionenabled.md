# isContinuousCollisionDetectionEnabled

**Framework**: RealityKit  
**Kind**: property

A Boolean that controls whether the physics simulation performs continuous collision detection.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
var isContinuousCollisionDetectionEnabled: Bool
```

#### Discussion

Set the value to `true` to perform continuous collision detection. The value is `false` by default, indicating the simulation should apply discrete collision detection.

Discrete collision detection considers only the position of a body once per rendered frame, or about every 16 milliseconds at 60 frames per second. Continuous collision detection considers the position of the body throughout the frame interval. The latter is more computationally expensive, but can help to avoid missing a collision for a quickly moving object, like a projectile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsbodycomponent/iscontinuouscollisiondetectionenabled)*