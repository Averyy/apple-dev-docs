# MPSNNLabelsNode

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A placeholder node denoting the per-element weight buffer used by loss and gradient loss kernels.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSNNLabelsNode
```

```objc
@interface MPSNNLabelsNode : MPSNNStateNode
```

## Relationships

### Inherits From
- [MPSNNStateNode](./mpsnnstatenode.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Loss Layer Nodes
- [class MPSCNNLossNode](./mpscnnlossnode.md)
  A representation of a loss kernel.
- [class MPSCNNYOLOLossNode](./mpscnnyololossnode.md)
  A representation of a YOLO loss kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnlabelsnode)*