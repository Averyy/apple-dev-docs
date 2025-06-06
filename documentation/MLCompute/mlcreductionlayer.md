# MLCReductionLayer

**Framework**: ML Compute  
**Kind**: class

A layer that reduces tensor values across a specific dimension to a scalar value.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCReductionLayer
```

#### Overview

Use this layer to perform reduction operations on a given dimension. The output of this layer is a tensor of the same shape as the source tensor, except the layer sets the dimension to `1`.

## Topics

### Creating Reduction Layers
- [convenience init?(reductionType: MLCReductionType, dimension: Int)](mlcreductionlayer/init(reductiontype:dimension:).md)
  Creates a reduction layer using the reduction type and dimension you specify.
- [convenience init?(reductionType: MLCReductionType, dimensions: [Int])](mlcreductionlayer/init(reductiontype:dimensions:).md)
  Creates a reduction layer using the reduction type and dimensions you specify.
- [enum MLCReductionType](mlcreductiontype.md)
  Constants that describe a reduction operation type.
### Inspecting Reduction Layers
- [var reductionType: MLCReductionType](mlcreductionlayer/reductiontype.md)
  The function reduction type the system uses for reduction.
- [var dimension: Int](mlcreductionlayer/dimension.md)
  The dimension to perform the reduction operation on.
- [var dimensions: [Int]](mlcreductionlayer/dimensions-9oph6.md)
  The dimensions to perform the reduction operation on.

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
- [class MLCMatMulLayer](mlcmatmullayer.md)
  A layer that multiplies matrices.
- [class MLCFullyConnectedLayer](mlcfullyconnectedlayer.md)
  A layer that connects each input to each output within its layer.
- [class MLCGramMatrixLayer](mlcgrammatrixlayer.md)
  A layer that computes the uncentered cross-correlation values between the spacial planes of each feature channel of a tensor.
- [class MLCComparisonLayer](mlccomparisonlayer.md)
  A layer that performs elementwise comparison of two tensors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcreductionlayer)*