# init(pivotEntity:revolutions:orbitalAxis:isOrientedToPath:isAdditive:)

**Framework**: RealityKit  
**Kind**: init

Creates a new orbit entity action.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
init(pivotEntity: ActionEntityResolution, revolutions: Float, orbitalAxis: SIMD3<Float> = [0, 1, 0], isOrientedToPath: Bool = false, isAdditive: Bool = false)
```

## Parameters

- `pivotEntity`: The pivot entity that the targeted entity will orbit.
- `revolutions`: The number of rotations to complete before stopping.
- `orbitalAxis`: A vector that describes the axis of rotation (in world space).
- `isOrientedToPath`: Indicates whether the orbiting target entity updates   its orientation during the animation to orient itself   along the rotation path.
- `isAdditive`: A Boolean value that indicates whether the animation system additively blends   the action’s output with the base value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/orbitentityaction/init(pivotentity:revolutions:orbitalaxis:isorientedtopath:isadditive:))*