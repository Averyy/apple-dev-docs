# MLCSoftmaxLayer

**Framework**: ML Compute  
**Kind**: class

A layer that outputs a probability distribution as attention weights.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCSoftmaxLayer
```

## Topics

### Creating Softmax Layers
- [convenience init(operation: MLCSoftmaxOperation)](mlcsoftmaxlayer/init(operation:).md)
  Creates a softmax layer with the operation you specify.
- [convenience init(operation: MLCSoftmaxOperation, dimension: Int)](mlcsoftmaxlayer/init(operation:dimension:).md)
  Creates a softmax layer with the operation and dimension you specify.
- [enum MLCSoftmaxOperation](mlcsoftmaxoperation.md)
  A softmax operation.
### Inspecting Softmax Layers
- [var operation: MLCSoftmaxOperation](mlcsoftmaxlayer/operation.md)
  The softmax operation.
- [var dimension: Int](mlcsoftmaxlayer/dimension.md)
  The dimension over which you want to perform the softmax operation.

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

- [class MLCActivationLayer](mlcactivationlayer.md)
  A layer that applies an activation function to the source tensor and produces an output.
- [class MLCMultiheadAttentionLayer](mlcmultiheadattentionlayer.md)
  A multihead, scaled dot-product attention layer that attends to one or more entries in the input key-value pairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcsoftmaxlayer)*