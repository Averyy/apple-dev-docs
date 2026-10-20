# init(sourceGradient:sourceImage:convolutionGradientState:weights:)

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
init(sourceGradient: MPSNNImageNode, sourceImage: MPSNNImageNode, convolutionGradientState gradientState: MPSCNNConvolutionGradientStateNode, weights: (any MPSCNNConvolutionDataSource)?)
```

```objc
- (instancetype) initWithSourceGradient:(MPSNNImageNode *) sourceGradient sourceImage:(MPSNNImageNode *) sourceImage convolutionGradientState:(MPSCNNConvolutionGradientStateNode *) gradientState weights:(id<MPSCNNConvolutionDataSource>) weights;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnfullyconnectedgradientnode/init(sourcegradient:sourceimage:convolutiongradientstate:weights:))*