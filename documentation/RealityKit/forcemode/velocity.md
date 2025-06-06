# ForceMode.velocity

**Framework**: RealityKit  
**Kind**: case

A direct adjustment to a body’s linear or angular velocity, independent of its mass or inertia.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
case velocity
```

#### Discussion

The quantity that user sets via [`setForce(_:index:)`](forceeffectparameters/setforce(_:index:).md) has the units of distance / time. `velocity` mode causes a change in velocity independent of a body’s mass.

The quantity that user sets via [`setTorque(_:index:)`](forceeffectparameters/settorque(_:index:).md) has the units of 1 / time or radian / time. `velocity` mode causes a change in angular velocity independent of a body’s mass or inertia.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/forcemode/velocity)*