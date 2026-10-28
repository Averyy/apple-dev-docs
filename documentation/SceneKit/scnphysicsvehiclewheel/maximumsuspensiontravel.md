# maximumSuspensionTravel

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The maximum distance that the wheel is allowed to move up or down relative to its connection point, in centimeters.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var maximumSuspensionTravel: CGFloat { get set }
```

```objc
@property CGFloat maximumSuspensionTravel;
```

## Discussion

*Travel* is the total distance a wheel is allowed to move (in both directions), in the coordinate system of the node containing the vehicle’s chassis. The default suspension travel is `500.0`.

## See Also

### Simulating Suspension
- [var suspensionStiffness: CGFloat](./suspensionstiffness.md)
  The spring coefficient of the suspension between the vehicle and the wheel.
- [var suspensionCompression: CGFloat](./suspensioncompression.md)
  The coefficient that limits the speed of the suspension returning to its rest length when compressed.
- [var suspensionDamping: CGFloat](./suspensiondamping.md)
  The damping ratio that limits oscillation in the vehicle’s suspension.
- [var maximumSuspensionForce: CGFloat](./maximumsuspensionforce.md)
  The maximum force of the suspension between the vehicle and the wheel, in newtons.
- [var suspensionRestLength: CGFloat](./suspensionrestlength.md)
  The resting length of the suspension, in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/maximumsuspensiontravel)*