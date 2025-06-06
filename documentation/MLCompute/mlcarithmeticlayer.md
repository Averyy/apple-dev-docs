# MLCArithmeticLayer

**Framework**: ML Compute  
**Kind**: class

A layer that performs an arithmetic operation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCArithmeticLayer
```

## Topics

### Creating Arithmetic Layers
- [convenience init(operation: MLCArithmeticOperation)](mlcarithmeticlayer/init(operation:).md)
  Creates an arithmetic layer with the operation you specify.
- [enum MLCArithmeticOperation](mlcarithmeticoperation.md)
  Constants that describe an arithmetic operation.
### Inspecting Arithmetic Layers
- [var operation: MLCArithmeticOperation](mlcarithmeticlayer/operation.md)
  The arithmetic layer’s operation.

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

- [class MLCReductionLayer](mlcreductionlayer.md)
  A layer that reduces tensor values across a specific dimension to a scalar value.
- [class MLCMatMulLayer](mlcmatmullayer.md)
  A layer that multiplies matrices.
- [class MLCFullyConnectedLayer](mlcfullyconnectedlayer.md)
  A layer that connects each input to each output within its layer.
- [class MLCGramMatrixLayer](mlcgrammatrixlayer.md)
  A layer that computes the uncentered cross-correlation values between the spacial planes of each feature channel of a tensor.
- [class MLCComparisonLayer](mlccomparisonlayer.md)
  A layer that performs elementwise comparison of two tensors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcarithmeticlayer)*