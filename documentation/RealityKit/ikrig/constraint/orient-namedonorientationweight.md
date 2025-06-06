# orient(named:on:orientationWeight:)

**Framework**: RealityKit  
**Kind**: method

Creates a constraint with only an orientation demand.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
static func orient(named name: String, on jointName: String, orientationWeight: SIMD3<Float> = [1, 1, 1]) -> IKRig.Constraint
```

## Parameters

- `name`: The rig unique name of the constraint
- `jointName`: The name of the joint to constrain.
- `orientationWeight`: The weight of the orientation demand.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/constraint/orient(named:on:orientationweight:))*