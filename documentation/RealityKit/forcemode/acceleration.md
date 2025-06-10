# ForceMode.acceleration

**Framework**: RealityKit  
**Kind**: case

A direct adjustment to a body’s linear or angular acceleration, independent of its mass or inertia.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
case acceleration
```

#### Discussion

The quantity that user sets via [`setForce(_:index:)`](forceeffectparameters/setforce(_:index:).md) has the units of distance / time^2. `acceleration` mode causes a change in acceleration independent of a body’s mass.

The quantity that user sets via [`setTorque(_:index:)`](forceeffectparameters/settorque(_:index:).md) has the units of 1 / time^2 or radian / time^2. `acceleration` mode causes a change in angular acceleration independent of a body’s mass or inertia.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/forcemode/acceleration)*