# BindableData

**Framework**: RealityKit  
**Kind**: protocol  
**Role**: Protocol

An opaque base protocol for bindable data objects.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
protocol BindableData
```

#### Overview

The templated bindable-value object, [`BindableValue`](./bindablevalue.md) `<T>`, determines that the value you choose for type `T` adopts this protocol. The types that the framework accepts are: [`Transform`](./transform.md), [`Float`](../Swift/float.md), [`Double`](../Swift/double.md), [`SIMD2`](../Swift/simd2.md), [`SIMD3`](../Swift/simd3.md), [`SIMD4`](../Swift/simd4.md), [`simd_quatf`](https://developer.apple.com/documentation/simd/simd_quatf), [`Bool`](../Swift/bool.md), [`Int`](../Swift/int.md), and [`String`](../Swift/string.md).

## Relationships

### Conforming Types
- [Transform](./transform.md)

## See Also

### Compliance-related protocols
- [protocol AnimatableData](./animatabledata.md)
  A functionality specification that animatable data types adopt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bindabledata)*