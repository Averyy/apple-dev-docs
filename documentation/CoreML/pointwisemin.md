# pointwiseMin(_:_:)

**Framework**: Core ML  
**Kind**: func

Computes the element-wise minimum of two tensors.

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
func pointwiseMin(_ lhs: MLTensor, _ rhs: MLTensor) -> MLTensor
```

#### Discussion

For example:

```swift
let x = MLTensor([1.0, 3.0, 6.0])
let y = MLTensor([6.0, 3.0, 1.0])
let z = pointwiseMin(x, y)
await z.shapedArray(of: Float.self) // is [1.0, 3.0, 1.0]
```

Shapes must be broadcastable, where the broadcasted shape becomes the shape of the output.

## See Also

- [struct MLTensor](mltensor.md)
  A multi-dimensional array of numerical or Boolean scalars tailored to ML use cases, containing methods to perform transformations and mathematical operations efficiently using a ML compute device.
- [protocol MLTensorScalar](mltensorscalar.md)
  A type that represents the tensor scalar types supported by the framework. Don’t use this type directly.
- [protocol MLTensorRangeExpression](mltensorrangeexpression.md)
  A type that can be used to slice a dimension of a tensor. Don’t use this type directly.
- [func pointwiseMax(_:_:)](pointwisemax(_:_:).md)
  Computes the element-wise minimum between two tensors.
- [func withMLTensorComputePolicy(_:_:)](withmltensorcomputepolicy(_:_:).md)
  Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/pointwisemin(_:_:))*