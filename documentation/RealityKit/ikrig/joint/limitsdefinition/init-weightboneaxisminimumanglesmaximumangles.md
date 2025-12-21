# init(weight:boneAxis:minimumAngles:maximumAngles:)

**Framework**: RealityKit  
**Kind**: init

Creates a joint limits definition.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
init(weight: Float = 1.0, boneAxis: IKRig.Joint.LimitsDefinition.Axis = .x, minimumAngles: SIMD3<Float> = [-2.0 * .pi, -2.0 * .pi, -2.0 * .pi], maximumAngles: SIMD3<Float> = [2.0 * .pi, 2.0 * .pi, 2.0 * .pi])
```

#### Discussion

> ❗ **Important**: The minimum angles need to be less than the maximum angles.

## Parameters

- `weight`: The weight of the joint rotation limit demand.
- `boneAxis`: The axis around which the bone twists.
- `minimumAngles`: The negative delta from the rest pose per-axis in radians.
- `maximumAngles`: The positive delta from the rest pose per-axis in radians.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/joint/limitsdefinition/init(weight:boneaxis:minimumangles:maximumangles:))*