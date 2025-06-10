# AnimatableData

**Framework**: RealityKit  
**Kind**: protocol

A functionality specification that animatable data types adopt.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
protocol AnimatableData
```

#### Overview

The templated animation objects, for example [`BlendTreeAnimation`](blendtreeanimation.md) `<Value>`, determine that the type you specify for `Value` adopts this protocol. The types that the framework accepts are: [`JointTransforms`](jointtransforms.md), [`Transform`](transform.md), [`Float`](https://developer.apple.com/documentation/Swift/Float), [`Double`](https://developer.apple.com/documentation/Swift/Double), [`SIMD2`](https://developer.apple.com/documentation/Swift/SIMD2), [`SIMD3`](https://developer.apple.com/documentation/Swift/SIMD3), [`SIMD4`](https://developer.apple.com/documentation/Swift/SIMD4), and [`simd_quatf`](https://developer.apple.com/documentation/simd/simd_quatf).

## Relationships

### Conforming Types
- [BlendShapeWeights](blendshapeweights.md)
- [JointTransforms](jointtransforms.md)
- [Transform](transform.md)

## See Also

- [protocol BindableData](bindabledata.md)
  An opaque base protocol for bindable data objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animatabledata)*