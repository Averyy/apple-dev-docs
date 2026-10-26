# MPSCNNSoftMaxGradientNode

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A representation of a gradient softmax filter.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNSoftMaxGradientNode
```

```objc
@interface MPSCNNSoftMaxGradientNode : MPSNNGradientFilterNode
```

## Topics

### Initializers
- [init(sourceGradient: MPSNNImageNode, sourceImage: MPSNNImageNode, gradientState: MPSNNGradientStateNode)](./mpscnnsoftmaxgradientnode/init%28sourcegradient,sourceimage,gradientstate%29.md)
### Type Methods
- [+ nodeWithSourceGradient:sourceImage:gradientState:](./mpscnnsoftmaxgradientnode/nodewithsourcegradient_sourceimage_gradientstate_.md)

## Relationships

### Inherits From
- [MPSNNGradientFilterNode](./mpsnngradientfilternode.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Softmax Layer Nodes
- [class MPSCNNSoftMaxNode](./mpscnnsoftmaxnode.md)
  A representation of a softmax filter.
- [class MPSCNNLogSoftMaxNode](./mpscnnlogsoftmaxnode.md)
  A representation of a logarithmic softmax filter kernel.
- [class MPSCNNLogSoftMaxGradientNode](./mpscnnlogsoftmaxgradientnode.md)
  A representation of a gradient logarithmic softmax filter kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnsoftmaxgradientnode)*