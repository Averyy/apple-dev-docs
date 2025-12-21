# argmin(alongAxis:keepRank:)

**Framework**: Core ML  
**Kind**: method

Returns the indices of the minimum values along the specified axis.

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
func argmin(alongAxis axis: Int, keepRank: Bool = false) -> MLTensor
```

#### Return Value

The reduced tensor.

#### Discussion

```swift
let x = MLTensor(shape: [3, 2], scalars: [2, 3, 4, 5, 6, 7], scalarType: Float.self)
let y = x.argmin(alongAxis: 0)
y.shape // is [2]
y.scalarType // is Int32
await y.shapedArray(of: Int32.self) // is 0 0
```

## Parameters

- `axis`: The axis to reduce.
- `keepRank`: A Boolean indicating whether to keep the reduced axis or not. The default value is  .

## See Also

- [func argmax() -> MLTensor](mltensor/argmax.md)
  Returns the index of the maximum value of the flattened scalars.
- [func argmax(alongAxis: Int, keepRank: Bool) -> MLTensor](mltensor/argmax(alongaxis:keeprank:).md)
  Returns the indices of the maximum values along the specified axis.
- [func argmin() -> MLTensor](mltensor/argmin.md)
  Returns the index of the minimum value of the flattened scalars.
- [func argsort(alongAxis: Int, descendingOrder: Bool) -> MLTensor](mltensor/argsort(alongaxis:descendingorder:).md)
  Returns the indices (or arguments) of a tensor that give its sorted order along the specified axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/argmin(alongaxis:keeprank:))*