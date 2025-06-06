# topK(_:)

**Framework**: Core ML  
**Kind**: method

Returns the  largest values along the last axis of the tensor.

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
func topK(_ k: Int) -> (values: MLTensor, indices: MLTensor)
```

#### Return Value

A tuple of (values, indices) with values containing the top k values along the last axis and indices, a `Int32` tensor, containing the indices to the corresponding values.

#### Discussion

> **Note**: The tensor must have at least k elements along its last axis and order returned by largest values which are equal is not deterministic.

The tensor must have at least k elements along its last axis and order returned by largest values which are equal is not deterministic.

For example:

```swift
let x = MLTensor(shape: [1, 5], scalars: [1.0, 2.0, 3.0, 4.0, 5.0])
let (values, indices) = x.topK(3)
// values = [[5.0, 4.0, 3.0]]
// indices = [[4, 3, 2]]
```

## Parameters

- `k`: The number of largest values to return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/topk(_:))*