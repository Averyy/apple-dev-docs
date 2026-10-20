# IKRig.Constraint.IKOrientationDemand

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A definition of an orientational demand.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct IKOrientationDemand
```

## Topics

### Initializers
- [init()](./ikorientationdemand/init%28%29.md)
  Creates an orientational demand with default settings.
### Instance Properties
- [var influenceDepthMaxJointCount: Int](./ikorientationdemand/influencedepthmaxjointcount.md)
  The number of joints to be influenced by this demand.
- [var mode: IKRig.Constraint.IKOrientationDemand.Mode](./ikorientationdemand/mode-swift.property.md)
  The mode of the orientational demand.
- [var weight: SIMD3<Float>](./ikorientationdemand/weight.md)
  The per-axis weight this demand has on the pose.
### Enumerations
- [IKRig.Constraint.IKOrientationDemand.Mode](./ikorientationdemand/mode-swift.enum.md)
  Describes the acting modes of an orientation demand.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/constraint/ikorientationdemand)*