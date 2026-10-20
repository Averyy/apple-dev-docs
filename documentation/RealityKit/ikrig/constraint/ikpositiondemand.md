# IKRig.Constraint.IKPositionDemand

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A definition of a positional demand.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct IKPositionDemand
```

## Topics

### Initializers
- [init()](./ikpositiondemand/init%28%29.md)
  Creates a positional demand with default settings.
### Instance Properties
- [var influenceDepthMaxJointCount: Int](./ikpositiondemand/influencedepthmaxjointcount.md)
  The number of joints to be influenced by this demand.
- [var mode: IKRig.Constraint.IKPositionDemand.Mode](./ikpositiondemand/mode-swift.property.md)
  The mode of the positional demand.
- [var weight: SIMD3<Float>](./ikpositiondemand/weight.md)
  The per-axis weight this demand has on the pose.
### Enumerations
- [IKRig.Constraint.IKPositionDemand.Mode](./ikpositiondemand/mode-swift.enum.md)
  Describes the acting modes of positional demands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/constraint/ikpositiondemand)*