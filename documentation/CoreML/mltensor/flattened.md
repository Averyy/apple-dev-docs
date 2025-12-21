# flattened()

**Framework**: Core ML  
**Kind**: method

Reshape to a one-dimensional tensor.

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
func flattened() -> MLTensor
```

#### Discussion

> **Note**: Flattening a zero-dimensional tensor will return a one-dimensional tensor.

For example:

```swift
let x = MLTensor(shape: [2, 2], scalars: [1, 2, 3, 4], scalarType: Float.self)
let y = x.flattened()
y.shape // is [4]
```

## See Also

- [func reshaped(to: [Int]) -> MLTensor](mltensor/reshaped(to:).md)
  Reshape to the specified shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/flattened())*