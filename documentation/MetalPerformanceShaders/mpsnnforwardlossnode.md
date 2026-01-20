# MPSNNForwardLossNode

**Framework**: Metal Performance Shaders  
**Kind**: class

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNForwardLossNode
```

## Topics

### Initializers
- [init(source: MPSNNImageNode, labels: MPSNNImageNode, lossDescriptor: MPSCNNLossDescriptor)](mpsnnforwardlossnode/init(source:labels:lossdescriptor:).md)
- [init(source: MPSNNImageNode, labels: MPSNNImageNode, weights: MPSNNImageNode?, lossDescriptor: MPSCNNLossDescriptor)](mpsnnforwardlossnode/init(source:labels:weights:lossdescriptor:)-8c2l6.md)
- [convenience init(source: MPSNNImageNode, labels: MPSNNImageNode, weights: MPSNNImageNode, lossDescriptor: MPSCNNLossDescriptor)](mpsnnforwardlossnode/init(source:labels:weights:lossdescriptor:)-9bsd7.md)
- [init(sources: [MPSNNImageNode], lossDescriptor: MPSCNNLossDescriptor)](mpsnnforwardlossnode/init(sources:lossdescriptor:).md)
### Instance Properties
- [var delta: Float](mpsnnforwardlossnode/delta.md)
- [var epsilon: Float](mpsnnforwardlossnode/epsilon.md)
- [var labelSmoothing: Float](mpsnnforwardlossnode/labelsmoothing.md)
- [var lossType: MPSCNNLossType](mpsnnforwardlossnode/losstype.md)
- [var numberOfClasses: Int](mpsnnforwardlossnode/numberofclasses.md)
- [var propertyCallBack: (any MPSNNLossCallback)?](mpsnnforwardlossnode/propertycallback.md)
- [var reduceAcrossBatch: Bool](mpsnnforwardlossnode/reduceacrossbatch.md)
- [var reductionType: MPSCNNReductionType](mpsnnforwardlossnode/reductiontype.md)
- [var weight: Float](mpsnnforwardlossnode/weight.md)
### Instance Methods
- [func gradientFilter(withSource: MPSNNImageNode) -> MPSNNLossGradientNode](mpsnnforwardlossnode/gradientfilter(withsource:).md)
- [func gradientFilter(withSources: [MPSNNImageNode]) -> MPSNNLossGradientNode](mpsnnforwardlossnode/gradientfilter(withsources:).md)
- [func gradientFilters(withSource: MPSNNImageNode) -> [MPSNNLossGradientNode]](mpsnnforwardlossnode/gradientfilters(withsource:).md)
- [func gradientFilters(withSources: [MPSNNImageNode]) -> [MPSNNLossGradientNode]](mpsnnforwardlossnode/gradientfilters(withsources:).md)

## Relationships

### Inherits From
- [MPSNNFilterNode](mpsnnfilternode.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnforwardlossnode)*