# MLCMatMulLayer

**Framework**: ML Compute  
**Kind**: class

A layer that multiplies matrices.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCMatMulLayer
```

## Topics

### Creating Matrix Multiplication Layers
- [convenience init?(descriptor: MLCMatMulDescriptor)](mlcmatmullayer/init(descriptor:).md)
  Creates a matrix multiplication layer with the specified descriptor you specify.
- [class MLCMatMulDescriptor](mlcmatmuldescriptor.md)
  A configuration object you use to create a matrix multiplication layer.
### Inspecting Matrix Multiplication Layers
- [var descriptor: MLCMatMulDescriptor](mlcmatmullayer/descriptor.md)
  The configuration object you use to create the matrix multiplication layer.

## Relationships

### Inherits From
- [MLCLayer](mlclayer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MLCArithmeticLayer](mlcarithmeticlayer.md)
  A layer that performs an arithmetic operation.
- [class MLCReductionLayer](mlcreductionlayer.md)
  A layer that reduces tensor values across a specific dimension to a scalar value.
- [class MLCFullyConnectedLayer](mlcfullyconnectedlayer.md)
  A layer that connects each input to each output within its layer.
- [class MLCGramMatrixLayer](mlcgrammatrixlayer.md)
  A layer that computes the uncentered cross-correlation values between the spacial planes of each feature channel of a tensor.
- [class MLCComparisonLayer](mlccomparisonlayer.md)
  A layer that performs elementwise comparison of two tensors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcmatmullayer)*