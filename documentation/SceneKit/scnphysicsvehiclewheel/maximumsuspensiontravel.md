# maximumSuspensionTravel

**Framework**: SceneKit  
**Kind**: property

The maximum distance that the wheel is allowed to move up or down relative to its connection point, in centimeters.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var maximumSuspensionTravel: CGFloat { get set }
```

#### Discussion

 is the total distance a wheel is allowed to move (in both directions), in the coordinate system of the node containing the vehicle’s chassis. The default suspension travel is `500.0`.

## See Also

- [var suspensionStiffness: CGFloat](scnphysicsvehiclewheel/suspensionstiffness.md)
  The spring coefficient of the suspension between the vehicle and the wheel.
- [var suspensionCompression: CGFloat](scnphysicsvehiclewheel/suspensioncompression.md)
  The coefficient that limits the speed of the suspension returning to its rest length when compressed.
- [var suspensionDamping: CGFloat](scnphysicsvehiclewheel/suspensiondamping.md)
  The damping ratio that limits oscillation in the vehicle’s suspension.
- [var maximumSuspensionForce: CGFloat](scnphysicsvehiclewheel/maximumsuspensionforce.md)
  The maximum force of the suspension between the vehicle and the wheel, in newtons.
- [var suspensionRestLength: CGFloat](scnphysicsvehiclewheel/suspensionrestlength.md)
  The resting length of the suspension, in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/maximumsuspensiontravel)*