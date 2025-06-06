# suspensionCompression

**Framework**: SceneKit  
**Kind**: property

The coefficient that limits the speed of the suspension returning to its rest length when compressed.

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
var suspensionCompression: CGFloat { get set }
```

#### Discussion

The default suspension coefficient is `4.4`. Lower values cause the wheel to return to its natural position more quickly.

## See Also

- [var suspensionStiffness: CGFloat](scnphysicsvehiclewheel/suspensionstiffness.md)
  The spring coefficient of the suspension between the vehicle and the wheel.
- [var suspensionDamping: CGFloat](scnphysicsvehiclewheel/suspensiondamping.md)
  The damping ratio that limits oscillation in the vehicle’s suspension.
- [var maximumSuspensionTravel: CGFloat](scnphysicsvehiclewheel/maximumsuspensiontravel.md)
  The maximum distance that the wheel is allowed to move up or down relative to its connection point, in centimeters.
- [var maximumSuspensionForce: CGFloat](scnphysicsvehiclewheel/maximumsuspensionforce.md)
  The maximum force of the suspension between the vehicle and the wheel, in newtons.
- [var suspensionRestLength: CGFloat](scnphysicsvehiclewheel/suspensionrestlength.md)
  The resting length of the suspension, in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/suspensioncompression)*