# transposed(permutation:)

**Framework**: Core ML  
**Kind**: method

Permutes the dimensions of the tensor in the specified order.

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
func transposed(permutation: [Int]) -> MLTensor
```

#### Return Value

A permuted tensor.

#### Discussion

For example:

```swift
let x = MLTensor(shape: [1, 2, 3], scalars: [1, 2, 3, 4, 5, 6], scalarType: Float.self)
let y = x.transposed(permutation: [1, 0, 2])
y.shape // is [2, 1, 3]
```

## Parameters

- `permutation`: An array of integers defining the permutation, must be of length   and define   a valid permutation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/transposed(permutation:)-5t35l)*