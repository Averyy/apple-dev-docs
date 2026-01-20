# MPSNNStateNode

**Framework**: Metal Performance Shaders  
**Kind**: class

A placeholder node denoting the position in the graph of a state object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNStateNode
```

## Topics

### Instance Properties
- [var handle: (any MPSHandle)?](mpsnnstatenode/handle.md)
- [var exportFromGraph: Bool](mpsnnstatenode/exportfromgraph.md)
- [var synchronizeResource: Bool](mpsnnstatenode/synchronizeresource.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MPSNNBinaryGradientStateNode](mpsnnbinarygradientstatenode.md)
- [MPSNNGradientStateNode](mpsnngradientstatenode.md)
- [MPSNNLabelsNode](mpsnnlabelsnode.md)
- [MPSNNMultiaryGradientStateNode](mpsnnmultiarygradientstatenode.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var label: String?](mpsnnfilternode/label.md)
- [var paddingPolicy: any MPSNNPadding](mpsnnfilternode/paddingpolicy.md)
- [protocol MPSNNPadding](mpsnnpadding.md)
  The protocol that provides a description of how kernels should pad images.
- [var resultImage: MPSNNImageNode](mpsnnfilternode/resultimage.md)
- [var resultState: MPSNNStateNode?](mpsnnfilternode/resultstate.md)
- [var resultStates: [MPSNNStateNode]?](mpsnnfilternode/resultstates.md)
- [class MPSNNBinaryGradientStateNode](mpsnnbinarygradientstatenode.md)
  A representation of the state created to record the properties of a binary gradient kernel.
- [class MPSNNGradientStateNode](mpsnngradientstatenode.md)
  A representation of the state created to record the properties of a gradient kernel at the time it was encoded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnstatenode)*