# IKRig.Constraint.IKOrientationDemand.Mode.additiveLookAt(targetAxis:)

**Framework**: RealityKit  
**Kind**: case

A mode which computes the rotation target as additive look-at.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
case additiveLookAt(targetAxis: SIMD3<Float>)
```

##### Demand Target

The rotation weight of [`animationOverrideWeight`](ikcomponent/constraint/animationoverrideweight.md) determines how much of the `Delta` is added to the `Source`.

## Parameters

- `targetAxis`: The unit vector from the joint to the look-at target defined in the   local space of the constrained joint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/constraint/ikorientationdemand/mode-swift.enum/additivelookat(targetaxis:))*