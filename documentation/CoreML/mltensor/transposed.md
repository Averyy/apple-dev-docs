# transposed()

**Framework**: Core ML  
**Kind**: method

Permutes the tensor with dimensions permuted in reverse order.

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
func transposed() -> MLTensor
```

#### Return Value

A permuted tensor.

#### Discussion

For example:

```swift
let x = MLTensor(shape: [1, 2, 3], scalars: [1, 2, 3, 4, 5, 6], scalarType: Float.self)
let y = x.transposed()
y.shape // is [3, 2, 1]
```

## See Also

- [func transposed(permutation:)](mltensor/transposed(permutation:).md)
  Permutes the dimensions of the tensor in the specified order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/transposed())*