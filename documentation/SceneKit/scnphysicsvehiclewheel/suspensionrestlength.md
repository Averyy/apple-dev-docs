# suspensionRestLength

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The resting length of the suspension, in meters.

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
var suspensionRestLength: CGFloat { get set }
```

```objc
@property CGFloat suspensionRestLength;
```

## Discussion

This property measures the length of the simulated spring between the vehicle and its wheel when the spring is not stressed by the weight of either body. When the wheel receives a shock (for example, when the vehicle runs over a bump), SceneKit adds the difference between the wheel’s current position and its connection position to this rest length and then applies a force between the wheel and vehicle proportional to the total.

## See Also

### Simulating Suspension
- [var suspensionStiffness: CGFloat](./suspensionstiffness.md)
  The spring coefficient of the suspension between the vehicle and the wheel.
- [var suspensionCompression: CGFloat](./suspensioncompression.md)
  The coefficient that limits the speed of the suspension returning to its rest length when compressed.
- [var suspensionDamping: CGFloat](./suspensiondamping.md)
  The damping ratio that limits oscillation in the vehicle’s suspension.
- [var maximumSuspensionTravel: CGFloat](./maximumsuspensiontravel.md)
  The maximum distance that the wheel is allowed to move up or down relative to its connection point, in centimeters.
- [var maximumSuspensionForce: CGFloat](./maximumsuspensionforce.md)
  The maximum force of the suspension between the vehicle and the wheel, in newtons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/suspensionrestlength)*