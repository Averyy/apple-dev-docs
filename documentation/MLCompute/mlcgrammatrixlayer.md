# MLCGramMatrixLayer

**Framework**: ML Compute  
**Kind**: class

A layer that computes the uncentered cross-correlation values between the spacial planes of each feature channel of a tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCGramMatrixLayer
```

#### Overview

For example, if the input tensor batch function is:

`x = x[b, y, x, c]`

The computation performed by this layer is:

`y = y[b, 1, f, c] = alpha * sum_{x, y} x[b, y, x, f] * x[b, y, x, c]`

Interpret this operation as computing all combinations of fully connected layers between the different spatial planes of the input tensor.

The layer performs this operation independently for each tensor in a batch. Then the layer stores these results in the feature channel and x-coordinate indices of the output batch.

Legend:

## Topics

### Creating Gram Matrix Layers
- [convenience init(scale: Float)](mlcgrammatrixlayer/init(scale:).md)
  Creates a gram matrix layer with the scaling factor you specify.
### Inspecting Gram Matrix Layers
- [var scale: Float](mlcgrammatrixlayer/scale.md)
  The scaling factor.

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
- [class MLCMatMulLayer](mlcmatmullayer.md)
  A layer that multiplies matrices.
- [class MLCFullyConnectedLayer](mlcfullyconnectedlayer.md)
  A layer that connects each input to each output within its layer.
- [class MLCComparisonLayer](mlccomparisonlayer.md)
  A layer that performs elementwise comparison of two tensors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgrammatrixlayer)*