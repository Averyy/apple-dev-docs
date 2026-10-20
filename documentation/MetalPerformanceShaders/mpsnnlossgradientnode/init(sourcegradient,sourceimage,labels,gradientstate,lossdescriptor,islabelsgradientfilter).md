# init(sourceGradient:sourceImage:labels:gradientState:lossDescriptor:isLabelsGradientFilter:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(sourceGradient: MPSNNImageNode, sourceImage: MPSNNImageNode, labels: MPSNNImageNode, gradientState: MPSNNGradientStateNode?, lossDescriptor descriptor: MPSCNNLossDescriptor, isLabelsGradientFilter: Bool)
```

```objc
- (instancetype) initWithSourceGradient:(MPSNNImageNode *) sourceGradient sourceImage:(MPSNNImageNode *) sourceImage labels:(MPSNNImageNode *) labels gradientState:(MPSNNGradientStateNode *) gradientState lossDescriptor:(MPSCNNLossDescriptor *) descriptor isLabelsGradientFilter:(BOOL) isLabelsGradientFilter;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnlossgradientnode/init(sourcegradient:sourceimage:labels:gradientstate:lossdescriptor:islabelsgradientfilter:))*