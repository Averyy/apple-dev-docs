# ForceMode.force

**Framework**: RealityKit  
**Kind**: case

A constant force or torque applied to a body, influencing motion over time.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
case force
```

#### Discussion

The quantity that user sets via [`setForce(_:index:)`](forceeffectparameters/setforce(_:index:).md) has the units of mass * distance /  time^2. i.e. a force ( mass * acceleration ). `force` mode causes a change in acceleration that varies proportionally to a body’s mass.

The quantity that user sets via [`setTorque(_:index:)`](forceeffectparameters/settorque(_:index:).md) has the units of mass * distance^2 / time^2. `force` mode causes a change in angular acceleration that varies proportionally to a body’s mass and inertia.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/forcemode/force)*