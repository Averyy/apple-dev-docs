# AnimatableData

**Framework**: RealityKit  
**Kind**: protocol  
**Role**: Protocol

A functionality specification that animatable data types adopt.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
protocol AnimatableData
```

## Overview

The templated animation objects, for example [`BlendTreeAnimation`](./blendtreeanimation.md) `<Value>`, determine that the type you specify for `Value` adopts this protocol. The types that the framework accepts are: [`JointTransforms`](./jointtransforms.md), [`Transform`](./transform.md), [`Float`](../Swift/float.md), [`Double`](../Swift/double.md), [`SIMD2`](../Swift/simd2.md), [`SIMD3`](../Swift/simd3.md), [`SIMD4`](../Swift/simd4.md), and [`simd_quatf`](../simd/simd_quatf.md).

## Relationships

### Conforming Types
- [BlendShapeWeights](./blendshapeweights.md)
- [JointTransforms](./jointtransforms.md)
- [Transform](./transform.md)

## See Also

### Compliance-related protocols
- [protocol BindableData](./bindabledata.md)
  An opaque base protocol for bindable data objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animatabledata)*