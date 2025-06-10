# pointwiseMax(_:_:)

**Framework**: Core ML  
**Kind**: func

Computes the element-wise minimum between two tensors.

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
func pointwiseMax(_ lhs: MLTensor, _ rhs: MLTensor) -> MLTensor
```

#### Discussion

For example:

```swift
let x = MLTensor([1.0, 3.0, 6.0])
let y = MLTensor([6.0, 3.0, 1.0])
let z = pointwiseMax(x, y)
await z.shapedArray(of: Float.self) // is [6.0, 3.0, 6.0]
```

Shapes must be broadcastable, where the broadcasted shape becomes the shape of the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/pointwisemax(_:_:)-8zmn3)*