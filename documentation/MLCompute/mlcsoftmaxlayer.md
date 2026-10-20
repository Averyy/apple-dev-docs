# MLCSoftmaxLayer

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A layer that outputs a probability distribution as attention weights.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCSoftmaxLayer
```

```objc
@interface MLCSoftmaxLayer : MLCLayer
```

## Topics

### Creating Softmax Layers
- [convenience init(operation: MLCSoftmaxOperation)](./mlcsoftmaxlayer/init%28operation%29.md)
  Creates a softmax layer with the operation you specify.
- [convenience init(operation: MLCSoftmaxOperation, dimension: Int)](./mlcsoftmaxlayer/init%28operation,dimension%29.md)
  Creates a softmax layer with the operation and dimension you specify.
- [enum MLCSoftmaxOperation](./mlcsoftmaxoperation.md)
  A softmax operation.
### Inspecting Softmax Layers
- [var operation: MLCSoftmaxOperation](./mlcsoftmaxlayer/operation.md)
  The softmax operation.
- [var dimension: Int](./mlcsoftmaxlayer/dimension.md)
  The dimension over which you want to perform the softmax operation.

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

### Activation Layers
- [class MLCActivationLayer](./mlcactivationlayer.md)
  A layer that applies an activation function to the source tensor and produces an output.
- [class MLCMultiheadAttentionLayer](./mlcmultiheadattentionlayer.md)
  A multihead, scaled dot-product attention layer that attends to one or more entries in the input key-value pairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcsoftmaxlayer)*