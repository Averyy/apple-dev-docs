# MPSCNNSoftMaxNode

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A representation of a softmax filter.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNSoftMaxNode
```

```objc
@interface MPSCNNSoftMaxNode : MPSNNFilterNode
```

## Topics

### Initializers
- [init(source: MPSNNImageNode)](./mpscnnsoftmaxnode/init%28source%29.md)

## Relationships

### Inherits From
- [MPSNNFilterNode](./mpsnnfilternode.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Softmax Layer Nodes
- [class MPSCNNLogSoftMaxNode](./mpscnnlogsoftmaxnode.md)
  A representation of a logarithmic softmax filter kernel.
- [class MPSCNNLogSoftMaxGradientNode](./mpscnnlogsoftmaxgradientnode.md)
  A representation of a gradient logarithmic softmax filter kernel.
- [class MPSCNNSoftMaxGradientNode](./mpscnnsoftmaxgradientnode.md)
  A representation of a gradient softmax filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnsoftmaxnode)*