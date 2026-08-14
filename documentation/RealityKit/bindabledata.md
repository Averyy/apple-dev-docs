# BindableData

**Framework**: RealityKit  
**Kind**: protocol

An opaque base protocol for bindable data objects.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
protocol BindableData
```

#### Overview

The templated bindable-value object, [`BindableValue`](bindablevalue.md) `<T>`, determines that the value you choose for type `T` adopts this protocol. The types that the framework accepts are: [`Transform`](transform.md), [`Float`](https://developer.apple.com/documentation/swift/float), [`Double`](https://developer.apple.com/documentation/swift/double), [`SIMD2`](https://developer.apple.com/documentation/swift/simd2), [`SIMD3`](https://developer.apple.com/documentation/swift/simd3), [`SIMD4`](https://developer.apple.com/documentation/swift/simd4), [`simd_quatf`](https://developer.apple.com/documentation/simd/simd_quatf), [`Bool`](https://developer.apple.com/documentation/swift/bool), [`Int`](https://developer.apple.com/documentation/swift/int), and [`String`](https://developer.apple.com/documentation/swift/string).

## Relationships

### Conforming Types
- [Transform](transform.md)

## See Also

- [protocol AnimatableData](animatabledata.md)
  A functionality specification that animatable data types adopt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bindabledata)*