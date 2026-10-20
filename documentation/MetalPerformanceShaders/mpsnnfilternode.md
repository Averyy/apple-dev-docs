# MPSNNFilterNode

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A placeholder node denoting a neural network filter stage.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNFilterNode
```

```objc
@interface MPSNNFilterNode : NSObject
```

## Topics

### Instance Properties
- [var label: String?](./mpsnnfilternode/label.md)
- [var paddingPolicy: any MPSNNPadding](./mpsnnfilternode/paddingpolicy.md)
- [protocol MPSNNPadding](./mpsnnpadding.md)
  The protocol that provides a description of how kernels should pad images.
- [var resultImage: MPSNNImageNode](./mpsnnfilternode/resultimage.md)
- [var resultState: MPSNNStateNode?](./mpsnnfilternode/resultstate.md)
- [var resultStates: [MPSNNStateNode]?](./mpsnnfilternode/resultstates.md)
- [class MPSNNStateNode](./mpsnnstatenode.md)
  A placeholder node denoting the position in the graph of a state object.
- [class MPSNNBinaryGradientStateNode](./mpsnnbinarygradientstatenode.md)
  A representation of the state created to record the properties of a binary gradient kernel.
- [class MPSNNGradientStateNode](./mpsnngradientstatenode.md)
  A representation of the state created to record the properties of a gradient kernel at the time it was encoded.
### Instance Methods
- [func gradientFilter(withSource: MPSNNImageNode) -> MPSNNGradientFilterNode](./mpsnnfilternode/gradientfilter%28withsource%29.md)
- [func gradientFilter(withSources: [MPSNNImageNode]) -> MPSNNGradientFilterNode](./mpsnnfilternode/gradientfilter%28withsources%29.md)
- [func gradientFilters(withSource: MPSNNImageNode) -> [MPSNNGradientFilterNode]](./mpsnnfilternode/gradientfilters%28withsource%29.md)
- [func gradientFilters(withSources: [MPSNNImageNode]) -> [MPSNNGradientFilterNode]](./mpsnnfilternode/gradientfilters%28withsources%29.md)
- [func trainingGraph(withSourceGradient: MPSNNImageNode?, nodeHandler: MPSGradientNodeBlock?) -> [MPSNNFilterNode]?](./mpsnnfilternode/traininggraph%28withsourcegradient,nodehandler%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [MPSCNNBatchNormalizationNode](./mpscnnbatchnormalizationnode.md)
- [MPSCNNConvolutionNode](./mpscnnconvolutionnode.md)
- [MPSCNNDilatedPoolingMaxNode](./mpscnndilatedpoolingmaxnode.md)
- [MPSCNNDropoutNode](./mpscnndropoutnode.md)
- [MPSCNNGroupNormalizationNode](./mpscnngroupnormalizationnode.md)
- [MPSCNNInstanceNormalizationNode](./mpscnninstancenormalizationnode.md)
- [MPSCNNLogSoftMaxNode](./mpscnnlogsoftmaxnode.md)
- [MPSCNNLossNode](./mpscnnlossnode.md)
- [MPSCNNNeuronNode](./mpscnnneuronnode.md)
- [MPSCNNNormalizationNode](./mpscnnnormalizationnode.md)
- [MPSCNNPoolingNode](./mpscnnpoolingnode.md)
- [MPSCNNSoftMaxNode](./mpscnnsoftmaxnode.md)
- [MPSCNNUpsamplingBilinearNode](./mpscnnupsamplingbilinearnode.md)
- [MPSCNNUpsamplingNearestNode](./mpscnnupsamplingnearestnode.md)
- [MPSCNNYOLOLossNode](./mpscnnyololossnode.md)
- [MPSNNBinaryArithmeticNode](./mpsnnbinaryarithmeticnode.md)
- [MPSNNConcatenationNode](./mpsnnconcatenationnode.md)
- [MPSNNForwardLossNode](./mpsnnforwardlossnode.md)
- [MPSNNGradientFilterNode](./mpsnngradientfilternode.md)
- [MPSNNGramMatrixCalculationNode](./mpsnngrammatrixcalculationnode.md)
- [MPSNNInitialGradientNode](./mpsnninitialgradientnode.md)
- [MPSNNPadNode](./mpsnnpadnode.md)
- [MPSNNReshapeNode](./mpsnnreshapenode.md)
- [MPSNNScaleNode](./mpsnnscalenode.md)
- [MPSNNUnaryReductionNode](./mpsnnunaryreductionnode.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Filter Node Base Classes
- [class MPSNNGradientFilterNode](./mpsnngradientfilternode.md)
  A representation of a gradient filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnfilternode)*