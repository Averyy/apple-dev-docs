# replacing(atIndices:with:alongAxis:)

**Framework**: Core ML  
**Kind**: method

Replaces slices along the specified indices with the given replacement values.

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
func replacing(atIndices indices: MLTensor, with replacement: some MLTensorScalar, alongAxis axis: Int) -> MLTensor
```

#### Return Value

The updated tensor.

#### Discussion

For example:

```swift
let x = MLTensor(shape: [2, 3], scalars: [
    10, 30, 20,
    60, 40, 50
], scalarType: Float.self)
let i = MLTensor(shape: [2, 1], scalars: [
    1,
    0
], scalarType: Int32.self)
let y = x.replacing(with: 99, atIndices: i, alongAxis: 1)
// [[10, 99, 20],
//  [99, 40, 50]]
```

## Parameters

- `indices`: A 32-bit integer tensor containing indices to scatter values from  .   must have the same   shape as   except at  . Must be in the range  .
- `replacement`: The replacement value.
- `axis`: The axis to scatter to.

## See Also

- [func replacing(with: MLTensor, atIndices: MLTensor, alongAxis: Int) -> MLTensor](mltensor/replacing(with:atindices:alongaxis:).md)
  Replaces slices along the specified indices with the given replacement values.
- [func replacing(with:where:)](mltensor/replacing(with:where:).md)
  Returns a new tensor replacing values from `other` with the corresponding element in `self` where the associated element in `mask` is `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/replacing(atindices:with:alongaxis:))*