# MLCComparisonLayer

**Framework**: ML Compute  
**Kind**: class

A layer that performs elementwise comparison of two tensors.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+

## Declaration

```swift
class MLCComparisonLayer
```

#### Overview

The layer returns a tensor with the shape equal to the largest shape of operations. It fills with the Boolean value `result[i] = op1[i] ? op2[i]`, where `?` corresponds to the  [`MLCComparisonOperation`](mlccomparisonoperation.md) you specify.

## Topics

### Creating Comparison Layers
- [convenience init(operation: MLCComparisonOperation)](mlccomparisonlayer/init(operation:).md)
  Creates a comparison layer with the operation you specify.
- [enum MLCComparisonOperation](mlccomparisonoperation.md)
  A comparison operation.
### Inspecting Comparison Layers
- [var operation: MLCComparisonOperation](mlccomparisonlayer/operation.md)
  The comparison layer’s operation.

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
- [class MLCGramMatrixLayer](mlcgrammatrixlayer.md)
  A layer that computes the uncentered cross-correlation values between the spacial planes of each feature channel of a tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlccomparisonlayer)*