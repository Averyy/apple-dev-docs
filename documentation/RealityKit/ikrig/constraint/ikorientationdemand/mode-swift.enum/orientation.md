# IKRig.Constraint.IKOrientationDemand.Mode.orientation

**Framework**: RealityKit  
**Kind**: case

A mode which uses the set rotation target.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
case orientation
```

##### Demand Target

- **Source**: The model space orientation of the constrained joint from the FK demands pose.
- **Target**: The rotation component of [`target`](ikcomponent/constraint/target.md).

The rotation weight of [`animationOverrideWeight`](ikcomponent/constraint/animationoverrideweight.md) determines how the rotation target is calculated:

- A weight of **`0`** uses the `Source`.
- A weight of **`1`** uses the `Target`.
- A weight **between `0` and `1`** results in a spherical linear interpolation between the `Source` and `Target`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/constraint/ikorientationdemand/mode-swift.enum/orientation)*