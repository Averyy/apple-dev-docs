# MPSNNForwardLossNode

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPSNNForwardLossNode : MPSNNFilterNode
```

## Topics

### Initializers
- [init(source: MPSNNImageNode, labels: MPSNNImageNode, lossDescriptor: MPSCNNLossDescriptor)](./mpsnnforwardlossnode/init%28source,labels,lossdescriptor%29.md)
- [init(source: MPSNNImageNode, labels: MPSNNImageNode, weights: MPSNNImageNode?, lossDescriptor: MPSCNNLossDescriptor)](./mpsnnforwardlossnode/init%28source,labels,weights,lossdescriptor%29-8c2l6.md)
- [convenience init(source: MPSNNImageNode, labels: MPSNNImageNode, weights: MPSNNImageNode, lossDescriptor: MPSCNNLossDescriptor)](./mpsnnforwardlossnode/init%28source,labels,weights,lossdescriptor%29-9bsd7.md)
- [init(sources: [MPSNNImageNode], lossDescriptor: MPSCNNLossDescriptor)](./mpsnnforwardlossnode/init%28sources,lossdescriptor%29.md)
### Instance Properties
- [var delta: Float](./mpsnnforwardlossnode/delta.md)
- [var epsilon: Float](./mpsnnforwardlossnode/epsilon.md)
- [var labelSmoothing: Float](./mpsnnforwardlossnode/labelsmoothing.md)
- [var lossType: MPSCNNLossType](./mpsnnforwardlossnode/losstype.md)
- [var numberOfClasses: Int](./mpsnnforwardlossnode/numberofclasses.md)
- [var propertyCallBack: (any MPSNNLossCallback)?](./mpsnnforwardlossnode/propertycallback.md)
- [var reduceAcrossBatch: Bool](./mpsnnforwardlossnode/reduceacrossbatch.md)
- [var reductionType: MPSCNNReductionType](./mpsnnforwardlossnode/reductiontype.md)
- [var weight: Float](./mpsnnforwardlossnode/weight.md)
### Instance Methods
- [func gradientFilter(withSource: MPSNNImageNode) -> MPSNNLossGradientNode](./mpsnnforwardlossnode/gradientfilter%28withsource%29.md)
- [func gradientFilter(withSources: [MPSNNImageNode]) -> MPSNNLossGradientNode](./mpsnnforwardlossnode/gradientfilter%28withsources%29.md)
- [func gradientFilters(withSource: MPSNNImageNode) -> [MPSNNLossGradientNode]](./mpsnnforwardlossnode/gradientfilters%28withsource%29.md)
- [func gradientFilters(withSources: [MPSNNImageNode]) -> [MPSNNLossGradientNode]](./mpsnnforwardlossnode/gradientfilters%28withsources%29.md)
### Type Methods
- [+ nodeWithSource:labels:lossDescriptor:](./mpsnnforwardlossnode/nodewithsource_labels_lossdescriptor_.md)
- [+ nodeWithSources:lossDescriptor:](./mpsnnforwardlossnode/nodewithsources_lossdescriptor_.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnforwardlossnode)*