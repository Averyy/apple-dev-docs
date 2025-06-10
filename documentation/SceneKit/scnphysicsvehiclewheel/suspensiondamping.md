# suspensionDamping

**Framework**: SceneKit  
**Kind**: property

The damping ratio that limits oscillation in the vehicle’s suspension.

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
var suspensionDamping: CGFloat { get set }
```

#### Discussion

 measures the tendency of the suspension to oscillate after a shock—in other words, for the vehicle to bounce up and down after running over a bump. The default damping ratio of `2.3` causes the wheel to return to its neutral position quickly after a shock. Values lower than `1.0` result in more oscillation.

## See Also

- [var suspensionStiffness: CGFloat](scnphysicsvehiclewheel/suspensionstiffness.md)
  The spring coefficient of the suspension between the vehicle and the wheel.
- [var suspensionCompression: CGFloat](scnphysicsvehiclewheel/suspensioncompression.md)
  The coefficient that limits the speed of the suspension returning to its rest length when compressed.
- [var maximumSuspensionTravel: CGFloat](scnphysicsvehiclewheel/maximumsuspensiontravel.md)
  The maximum distance that the wheel is allowed to move up or down relative to its connection point, in centimeters.
- [var maximumSuspensionForce: CGFloat](scnphysicsvehiclewheel/maximumsuspensionforce.md)
  The maximum force of the suspension between the vehicle and the wheel, in newtons.
- [var suspensionRestLength: CGFloat](scnphysicsvehiclewheel/suspensionrestlength.md)
  The resting length of the suspension, in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/suspensiondamping)*