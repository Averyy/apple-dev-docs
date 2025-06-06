# lookAtAdditive(named:on:lookingAlong:orientationWeight:)

**Framework**: RealityKit  
**Kind**: method

Creates a constraint with only an orientational demand in additive look-at mode.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
static func lookAtAdditive(named name: String, on jointName: String, lookingAlong targetAxis: SIMD3<Float>, orientationWeight: SIMD3<Float> = [1, 1, 1]) -> IKRig.Constraint
```

#### Discussion

> **Note**: `IKOrientationDemand.Mode.additiveLookAt`

`IKOrientationDemand.Mode.additiveLookAt`

## Parameters

- `name`: The rig unique name of the constraint
- `jointName`: The name of the joint to constrain.
- `targetAxis`: The axis from the constrained joint to look-at target position in the local space   of the joint.
- `orientationWeight`: The weight of the orientation demand.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/constraint/lookatadditive(named:on:lookingalong:orientationweight:))*