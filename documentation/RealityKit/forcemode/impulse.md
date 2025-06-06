# ForceMode.impulse

**Framework**: RealityKit  
**Kind**: case

A direct adjustment to a body’s linear or angular momentum.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
case impulse
```

#### Discussion

The quantity that user sets via [`setForce(_:index:)`](forceeffectparameters/setforce(_:index:).md) has the units of mass * distance / time. `impulse` mode causes a change in linear momentum.

The quantity that user sets via [`setTorque(_:index:)`](forceeffectparameters/settorque(_:index:).md) has the units of mass * distance^2 / time. `impulse` mode causes a change in angular momentum.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/forcemode/impulse)*