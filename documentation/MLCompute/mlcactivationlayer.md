# MLCActivationLayer

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A layer that applies an activation function to the source tensor and produces an output.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCActivationLayer
```

```objc
@interface MLCActivationLayer : MLCLayer
```

## Overview

To construct an activation layer, create an activation descriptor and then pass it to the initializer.

> 💡 **Tip**:  If you don’t need to customize the behavior of the activation layer, you can save time by using [Preconfigured Activation Layers](./preconfigured-activation-layers.md) instead of creating a descriptor to use with an activation layer initializer.

## Topics

### Creating Activation Layers
- [convenience init(descriptor: MLCActivationDescriptor)](./mlcactivationlayer/init%28descriptor%29.md)
  Creates an activation layer with the descriptor you specify.
- [Preconfigured Activation Layers](./preconfigured-activation-layers.md)
  Obtain a preconfigured activation layer with common behavior.
- [class MLCActivationDescriptor](./mlcactivationdescriptor.md)
  A configuration object you use to create an activation layer.
### Inspecting Activation Layers
- [var descriptor: MLCActivationDescriptor](./mlcactivationlayer/descriptor.md)
  The configuration object you use to create an activation layer.

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
- [class MLCMultiheadAttentionLayer](./mlcmultiheadattentionlayer.md)
  A multihead, scaled dot-product attention layer that attends to one or more entries in the input key-value pairs.
- [class MLCSoftmaxLayer](./mlcsoftmaxlayer.md)
  A layer that outputs a probability distribution as attention weights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcactivationlayer)*