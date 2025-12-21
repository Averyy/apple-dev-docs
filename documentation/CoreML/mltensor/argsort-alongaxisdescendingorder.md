# argsort(alongAxis:descendingOrder:)

**Framework**: Core ML  
**Kind**: method

Returns the indices (or arguments) of a tensor that give its sorted order along the specified axis.

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
func argsort(alongAxis axis: Int = -1, descendingOrder: Bool = false) -> MLTensor
```

#### Return Value

A `Int32` tensor of sorted indices.

#### Discussion

For example:

```swift
let x = MLTensor([1.0, 3.0, 2.0])
let y = x.argSort()
await y.shapedArray(of: Int32.self) // is [0, 2, 1]
```

## Parameters

- `axis`: The axis along which to sort. The default is  , which sorts the last axis.
- `descendingOrder`: A Boolean value that determines the sort order. The default is   which   sorts from largest to least.

## See Also

- [func argmax() -> MLTensor](mltensor/argmax.md)
  Returns the index of the maximum value of the flattened scalars.
- [func argmax(alongAxis: Int, keepRank: Bool) -> MLTensor](mltensor/argmax(alongaxis:keeprank:).md)
  Returns the indices of the maximum values along the specified axis.
- [func argmin() -> MLTensor](mltensor/argmin.md)
  Returns the index of the minimum value of the flattened scalars.
- [func argmin(alongAxis: Int, keepRank: Bool) -> MLTensor](mltensor/argmin(alongaxis:keeprank:).md)
  Returns the indices of the minimum values along the specified axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/argsort(alongaxis:descendingorder:))*