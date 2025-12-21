# MLTensorScalar

**Framework**: Core ML  
**Kind**: protocol

A type that represents the tensor scalar types supported by the framework. Don’t use this type directly.

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
protocol MLTensorScalar : Sendable
```

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MLTensor](mltensor.md)
  A multi-dimensional array of numerical or Boolean scalars tailored to ML use cases, containing methods to perform transformations and mathematical operations efficiently using a ML compute device.
- [protocol MLTensorRangeExpression](mltensorrangeexpression.md)
  A type that can be used to slice a dimension of a tensor. Don’t use this type directly.
- [func pointwiseMin(_:_:)](pointwisemin(_:_:).md)
  Computes the element-wise minimum of two tensors.
- [func pointwiseMax(_:_:)](pointwisemax(_:_:).md)
  Computes the element-wise minimum between two tensors.
- [func withMLTensorComputePolicy(_:_:)](withmltensorcomputepolicy(_:_:).md)
  Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensorscalar)*