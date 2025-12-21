# IKRig.Constraint.IKOrientationDemand.Mode.absoluteLookAt(targetAxis:)

**Framework**: RealityKit  
**Kind**: case

A mode which computes the rotation target as absolute look-at.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
case absoluteLookAt(targetAxis: SIMD3<Float>)
```

##### Demand Target

The rotation weight of [`animationOverrideWeight`](ikcomponent/constraint/animationoverrideweight.md) determines how the rotation target is calculated:

- A weight of  uses the `Source`.
- A weight of  uses the `Target`.
- A weight  results in a spherical linear interpolation between the `Source` and `Target`.

## Parameters

- `targetAxis`: The unit vector from the joint to the look-at target defined in the   model space of the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/constraint/ikorientationdemand/mode-swift.enum/absolutelookat(targetaxis:))*