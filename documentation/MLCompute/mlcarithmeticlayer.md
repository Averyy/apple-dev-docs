# MLCArithmeticLayer

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A layer that performs an arithmetic operation.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCArithmeticLayer
```

```objc
@interface MLCArithmeticLayer : MLCLayer
```

## Topics

### Creating Arithmetic Layers
- [convenience init(operation: MLCArithmeticOperation)](./mlcarithmeticlayer/init%28operation%29.md)
  Creates an arithmetic layer with the operation you specify.
- [enum MLCArithmeticOperation](./mlcarithmeticoperation.md)
  Constants that describe an arithmetic operation.
### Inspecting Arithmetic Layers
- [var operation: MLCArithmeticOperation](./mlcarithmeticlayer/operation.md)
  The arithmetic layer’s operation.

## Relationships

### Inherits From
- [MLCLayer](./mlclayer.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Math Layers
- [class MLCReductionLayer](./mlcreductionlayer.md)
  A layer that reduces tensor values across a specific dimension to a scalar value.
- [class MLCMatMulLayer](./mlcmatmullayer.md)
  A layer that multiplies matrices.
- [class MLCFullyConnectedLayer](./mlcfullyconnectedlayer.md)
  A layer that connects each input to each output within its layer.
- [class MLCGramMatrixLayer](./mlcgrammatrixlayer.md)
  A layer that computes the uncentered cross-correlation values between the spacial planes of each feature channel of a tensor.
- [class MLCComparisonLayer](./mlccomparisonlayer.md)
  A layer that performs elementwise comparison of two tensors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcarithmeticlayer)*