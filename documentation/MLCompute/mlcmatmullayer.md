# MLCMatMulLayer

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A layer that multiplies matrices.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCMatMulLayer
```

```objc
@interface MLCMatMulLayer : MLCLayer
```

## Topics

### Creating Matrix Multiplication Layers
- [convenience init?(descriptor: MLCMatMulDescriptor)](./mlcmatmullayer/init%28descriptor%29.md)
  Creates a matrix multiplication layer with the specified descriptor you specify.
- [class MLCMatMulDescriptor](./mlcmatmuldescriptor.md)
  A configuration object you use to create a matrix multiplication layer.
### Inspecting Matrix Multiplication Layers
- [var descriptor: MLCMatMulDescriptor](./mlcmatmullayer/descriptor.md)
  The configuration object you use to create the matrix multiplication layer.

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
- [class MLCArithmeticLayer](./mlcarithmeticlayer.md)
  A layer that performs an arithmetic operation.
- [class MLCReductionLayer](./mlcreductionlayer.md)
  A layer that reduces tensor values across a specific dimension to a scalar value.
- [class MLCFullyConnectedLayer](./mlcfullyconnectedlayer.md)
  A layer that connects each input to each output within its layer.
- [class MLCGramMatrixLayer](./mlcgrammatrixlayer.md)
  A layer that computes the uncentered cross-correlation values between the spacial planes of each feature channel of a tensor.
- [class MLCComparisonLayer](./mlccomparisonlayer.md)
  A layer that performs elementwise comparison of two tensors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcmatmullayer)*