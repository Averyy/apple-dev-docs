# MLCFullyConnectedLayer

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A layer that connects each input to each output within its layer.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCFullyConnectedLayer
```

```objc
@interface MLCFullyConnectedLayer : MLCLayer
```

## Overview

This is also known as a dense layer.

## Topics

### Creating Fully Connected Layers
- [convenience init?(weights: MLCTensor, biases: MLCTensor?, descriptor: MLCConvolutionDescriptor)](./mlcfullyconnectedlayer/init%28weights,biases,descriptor%29.md)
  Creates a fully connected layer with the weights, biases, and convolution descriptor you specify.
- [class MLCConvolutionDescriptor](./mlcconvolutiondescriptor.md)
  A configuration object you use to create a convolution or fully connected layer.
### Inspecting Fully Connected Layers
- [var descriptor: MLCConvolutionDescriptor](./mlcfullyconnectedlayer/descriptor.md)
  The configuration object you use to create the fully connected layer.
- [var weights: MLCTensor](./mlcfullyconnectedlayer/weights.md)
  The weights tensor you use for the fully connected layer.
- [var biases: MLCTensor?](./mlcfullyconnectedlayer/biases.md)
  The biases tensor you use for the fully connected layer.
- [var biasesParameter: MLCTensorParameter?](./mlcfullyconnectedlayer/biasesparameter.md)
  The biases tensor parameter you use for optimizer updates.
- [var weightsParameter: MLCTensorParameter](./mlcfullyconnectedlayer/weightsparameter.md)
  The weights tensor parameter you use for optimizer updates.

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
- [class MLCMatMulLayer](./mlcmatmullayer.md)
  A layer that multiplies matrices.
- [class MLCGramMatrixLayer](./mlcgrammatrixlayer.md)
  A layer that computes the uncentered cross-correlation values between the spacial planes of each feature channel of a tensor.
- [class MLCComparisonLayer](./mlccomparisonlayer.md)
  A layer that performs elementwise comparison of two tensors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcfullyconnectedlayer)*