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

The rotation weight of [`animationOverrideWeight`](ikcomponent/constraint/animationoverrideweight.md) determines how the rotation target is calculated:

- A weight of  uses the `Source`.
- A weight of  uses the `Target`.
- A weight  results in a spherical linear interpolation between the `Source` and `Target`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/constraint/ikorientationdemand/mode-swift.enum/orientation)*