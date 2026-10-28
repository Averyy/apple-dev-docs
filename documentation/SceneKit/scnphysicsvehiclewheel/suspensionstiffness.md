# suspensionStiffness

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The spring coefficient of the suspension between the vehicle and the wheel.

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
var suspensionStiffness: CGFloat { get set }
```

```objc
@property CGFloat suspensionStiffness;
```

## Discussion

The spring coefficient determines both how quickly the wheel returns to its natural position after a shock (for example, when the vehicle runs over a bump) and how much force from the shock it transmits to the vehicle. The default spring coefficient is `2.0`.

## See Also

### Simulating Suspension
- [var suspensionCompression: CGFloat](./suspensioncompression.md)
  The coefficient that limits the speed of the suspension returning to its rest length when compressed.
- [var suspensionDamping: CGFloat](./suspensiondamping.md)
  The damping ratio that limits oscillation in the vehicle’s suspension.
- [var maximumSuspensionTravel: CGFloat](./maximumsuspensiontravel.md)
  The maximum distance that the wheel is allowed to move up or down relative to its connection point, in centimeters.
- [var maximumSuspensionForce: CGFloat](./maximumsuspensionforce.md)
  The maximum force of the suspension between the vehicle and the wheel, in newtons.
- [var suspensionRestLength: CGFloat](./suspensionrestlength.md)
  The resting length of the suspension, in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/suspensionstiffness)*