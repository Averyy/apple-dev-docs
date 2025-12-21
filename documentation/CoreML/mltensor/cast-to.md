# cast(to:)

**Framework**: Core ML  
**Kind**: method

Casts the elements of the tensor to the given scalar type.

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
func cast<Scalar>(to scalarType: Scalar.Type) -> MLTensor where Scalar : MLTensorScalar
```

#### Return Value

A new tensor with its contents cast to the given scalar type.

#### Discussion

For example:

```swift
let x = MLTensor([1, 2, 3], scalarType: Int32.self)
let y = x.cast(to: Float.self)
y.scalarType // is Float
```

## Parameters

- `scalarType`: The destination scalar type.

## See Also

- [func cast(like: MLTensor) -> MLTensor](mltensor/cast(like:).md)
  Casts the elements of the tensor to the scalar type of the given array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/cast(to:))*