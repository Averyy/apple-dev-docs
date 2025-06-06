# shapedArray(of:)

**Framework**: Core ML  
**Kind**: method

Returns a materialized representation of the tensor.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func shapedArray<Scalar>(of scalarType: Scalar.Type) async -> MLShapedArray<Scalar> where Scalar : MLShapedArrayScalar, Scalar : MLTensorScalar
```

#### Return Value

A `MLShapedArray` with the contents of the tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/shapedarray(of:))*