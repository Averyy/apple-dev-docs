# MLCActivationLayer

**Framework**: ML Compute  
**Kind**: class

A layer that applies an activation function to the source tensor and produces an output.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCActivationLayer
```

#### Overview

To construct an activation layer, create an activation descriptor and then pass it to the initializer.

> 💡 **Tip**:  If you don’t need to customize the behavior of the activation layer, you can save time by using [`Preconfigured Activation Layers`](preconfigured-activation-layers.md) instead of creating a descriptor to use with an activation layer initializer.

## Topics

### Creating Activation Layers
- [convenience init(descriptor: MLCActivationDescriptor)](mlcactivationlayer/init(descriptor:).md)
  Creates an activation layer with the descriptor you specify.
- [Preconfigured Activation Layers](preconfigured-activation-layers.md)
  Obtain a preconfigured activation layer with common behavior.
- [class MLCActivationDescriptor](mlcactivationdescriptor.md)
  A configuration object you use to create an activation layer.
### Inspecting Activation Layers
- [var descriptor: MLCActivationDescriptor](mlcactivationlayer/descriptor.md)
  The configuration object you use to create an activation layer.

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

- [class MLCMultiheadAttentionLayer](mlcmultiheadattentionlayer.md)
  A multihead, scaled dot-product attention layer that attends to one or more entries in the input key-value pairs.
- [class MLCSoftmaxLayer](mlcsoftmaxlayer.md)
  A layer that outputs a probability distribution as attention weights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcactivationlayer)*