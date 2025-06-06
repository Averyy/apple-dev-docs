# maximumSuspensionForce

**Framework**: SceneKit  
**Kind**: property

The maximum force of the suspension between the vehicle and the wheel, in newtons.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var maximumSuspensionForce: CGFloat { get set }
```

#### Discussion

The physics simulation applies a force of no greater than this magnitude when contact with the ground causes the wheel to move relative to the vehicle. The default maximum suspension force is `6000.0`.

## See Also

- [var suspensionStiffness: CGFloat](scnphysicsvehiclewheel/suspensionstiffness.md)
  The spring coefficient of the suspension between the vehicle and the wheel.
- [var suspensionCompression: CGFloat](scnphysicsvehiclewheel/suspensioncompression.md)
  The coefficient that limits the speed of the suspension returning to its rest length when compressed.
- [var suspensionDamping: CGFloat](scnphysicsvehiclewheel/suspensiondamping.md)
  The damping ratio that limits oscillation in the vehicle’s suspension.
- [var maximumSuspensionTravel: CGFloat](scnphysicsvehiclewheel/maximumsuspensiontravel.md)
  The maximum distance that the wheel is allowed to move up or down relative to its connection point, in centimeters.
- [var suspensionRestLength: CGFloat](scnphysicsvehiclewheel/suspensionrestlength.md)
  The resting length of the suspension, in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/maximumsuspensionforce)*