# argmin()

**Framework**: Core ML  
**Kind**: method

Returns the index of the minimum value of the flattened scalars.

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
func argmin() -> MLTensor
```

#### Discussion

```swift
let x = MLTensor(shape: [3, 2], scalars: [2, 3, 4, 5, 6, 7], scalarType: Float.self)
let y = x.argmin()
y.shape // is []
y.scalarType // is Int32
await y.shapedArray(of: Int32.self) // is 0
```

## See Also

- [func argmax() -> MLTensor](mltensor/argmax.md)
  Returns the index of the maximum value of the flattened scalars.
- [func argmax(alongAxis: Int, keepRank: Bool) -> MLTensor](mltensor/argmax(alongaxis:keeprank:).md)
  Returns the indices of the maximum values along the specified axis.
- [func argmin(alongAxis: Int, keepRank: Bool) -> MLTensor](mltensor/argmin(alongaxis:keeprank:).md)
  Returns the indices of the minimum values along the specified axis.
- [func argsort(alongAxis: Int, descendingOrder: Bool) -> MLTensor](mltensor/argsort(alongaxis:descendingorder:).md)
  Returns the indices (or arguments) of a tensor that give its sorted order along the specified axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/argmin())*