# replacing(with:atIndices:alongAxis:)

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
func replacing(with replacement: MLTensor, atIndices indices: MLTensor, alongAxis axis: Int) -> MLTensor
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
let updates = MLTensor(shape: [2, 1], scalars: [
    99,
    99
], scalarType: Float.self)
let y = x.replacing(atIndices: i, with: updates, alongAxis: 1)
// [[10, 99, 20],
//  [99, 40, 50]]
```

## Parameters

- `replacement`: The replacement values.
- `indices`: A 32-bit integer tensor containing indices to scatter values from  . Must have the same   shape as  . Must have the same shape as   except at  .
- `axis`: The axis to scatter to. Must be in the range  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/replacing(with:atindices:alongaxis:))*