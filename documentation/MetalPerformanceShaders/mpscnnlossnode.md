# MPSCNNLossNode

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A representation of a loss kernel.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNLossNode
```

```objc
@interface MPSCNNLossNode : MPSNNFilterNode
```

## Topics

### Initializers
- [init(source: MPSNNImageNode, lossDescriptor: MPSCNNLossDescriptor)](./mpscnnlossnode/init%28source,lossdescriptor%29.md)
### Instance Properties
- [var inputLabels: MPSNNLabelsNode](./mpscnnlossnode/inputlabels.md)
### Type Methods
- [+ nodeWithSource:lossDescriptor:](./mpscnnlossnode/nodewithsource_lossdescriptor_.md)

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

### Loss Layer Nodes
- [class MPSCNNYOLOLossNode](./mpscnnyololossnode.md)
  A representation of a YOLO loss kernel.
- [class MPSNNLabelsNode](./mpsnnlabelsnode.md)
  A placeholder node denoting the per-element weight buffer used by loss and gradient loss kernels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnlossnode)*