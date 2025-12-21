# withMLTensorComputePolicy(_:_:)

**Framework**: Core ML  
**Kind**: func

Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.

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
func withMLTensorComputePolicy<R>(_ computePolicy: MLComputePolicy, _ body: () async throws -> R) async rethrows -> R
```

#### Return Value

The return value, if any, of the `body` closure.

## Parameters

- `computePolicy`: A compute policy that will be set before the closure gets called and restored after the closure returns.
- `body`: A nullary closure. If the closure has a return value, that value is also used as the return value of the    function.

## See Also

- [struct MLTensor](mltensor.md)
  A multi-dimensional array of numerical or Boolean scalars tailored to ML use cases, containing methods to perform transformations and mathematical operations efficiently using a ML compute device.
- [protocol MLTensorScalar](mltensorscalar.md)
  A type that represents the tensor scalar types supported by the framework. Don’t use this type directly.
- [protocol MLTensorRangeExpression](mltensorrangeexpression.md)
  A type that can be used to slice a dimension of a tensor. Don’t use this type directly.
- [func pointwiseMin(_:_:)](pointwisemin(_:_:).md)
  Computes the element-wise minimum of two tensors.
- [func pointwiseMax(_:_:)](pointwisemax(_:_:).md)
  Computes the element-wise minimum between two tensors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/withmltensorcomputepolicy(_:_:))*