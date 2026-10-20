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

- **Source**: The model space orientation of the constrained joint from the FK demands pose.
- **Target**: The model space orientation aligning the associated `targetAxis` with the direction from the current model space joint position to [`lookAtTargetPosition`](ikcomponent/constraint/lookattargetposition.md).

The rotation weight of [`animationOverrideWeight`](ikcomponent/constraint/animationoverrideweight.md) determines how the rotation target is calculated:

- A weight of **`0`** uses the `Source`.
- A weight of **`1`** uses the `Target`.
- A weight **between `0` and `1`** results in a spherical linear interpolation between the `Source` and `Target`.

## Parameters

- `targetAxis`: The unit vector from the joint to the look-at target defined in the model space of the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/constraint/ikorientationdemand/mode-swift.enum/absolutelookat(targetaxis:))*