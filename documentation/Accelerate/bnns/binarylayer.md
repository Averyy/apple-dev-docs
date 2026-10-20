# BNNS.BinaryLayer

**Framework**: Accelerate  
**Kind**: class  
**Role**: Class

The base class for layers that accept two inputs.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
class BinaryLayer
```

## Topics

### Applying a Binary Layer
- [func apply(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor) throws](./binarylayer/apply%28batchsize,inputa,inputb,output%29.md)
  Applies the layer to a set of input object pairs, writing the result to a set of output objects.
- [func applyBackward(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputAGradient: BNNSNDArrayDescriptor, generatingInputBGradient: BNNSNDArrayDescriptor) throws](./binarylayer/applybackward%28batchsize,inputa,inputb,output,outputgradient,generatinginputagradient,generatinginputbgradient%29.md)
  Applies the layer backward to generate input gradients.

## Relationships

### Inherits From
- [BNNS.Layer](./layer.md)

## See Also

### Base Classes
- [class Layer](./layer.md)
  The base class for layer objects that wrap filters and manage deinitialization.
- [class UnaryLayer](./unarylayer.md)
  The base class for layers that accept a single input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/binarylayer)*