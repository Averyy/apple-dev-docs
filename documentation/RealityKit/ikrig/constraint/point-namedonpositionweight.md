# point(named:on:positionWeight:)

**Framework**: RealityKit  
**Kind**: method

Creates a constraint with only a positional demand.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
static func point(named name: String, on jointName: String, positionWeight: SIMD3<Float> = [1, 1, 1]) -> IKRig.Constraint
```

## Parameters

- `name`: The rig unique name of the constraint
- `jointName`: The name of the joint to constrain.
- `positionWeight`: The weight of the position demand.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/constraint/point(named:on:positionweight:))*