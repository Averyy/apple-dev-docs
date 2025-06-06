# IKRig.Joint.LimitsDefinition

**Framework**: RealityKit  
**Kind**: struct

A definition of joint rotation limits.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct LimitsDefinition
```

#### Overview

Limit angles are defined as relative to the rest pose.

> ❗ **Important**: The minimum angles need to be less than the maximum angles.

The minimum angles need to be less than the maximum angles.

## Topics

### Initializers
- [init(weight: Float, boneAxis: IKRig.Joint.LimitsDefinition.Axis, minimumAngles: SIMD3<Float>, maximumAngles: SIMD3<Float>)](ikrig/joint/limitsdefinition/init(weight:boneaxis:minimumangles:maximumangles:).md)
  Creates a joint limits definition.
### Instance Properties
- [var boneAxis: IKRig.Joint.LimitsDefinition.Axis](ikrig/joint/limitsdefinition/boneaxis.md)
  The axis around which the bone twists.
- [var maximumAngles: SIMD3<Float>](ikrig/joint/limitsdefinition/maximumangles.md)
  The positive delta from the rest pose per-axis in radians.
- [var minimumAngles: SIMD3<Float>](ikrig/joint/limitsdefinition/minimumangles.md)
  The negative delta from the rest pose per-axis in radians.
- [var weight: Float](ikrig/joint/limitsdefinition/weight.md)
  The weight of the joint rotation limit demand.
### Enumerations
- [IKRig.Joint.LimitsDefinition.Axis](ikrig/joint/limitsdefinition/axis.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/joint/limitsdefinition)*