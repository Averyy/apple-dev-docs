# init(source:convolutionGradientState:weights:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
init(source sourceNode: MPSNNImageNode, convolutionGradientState: MPSCNNConvolutionGradientStateNode?, weights: any MPSCNNConvolutionDataSource)
```

```objc
- (instancetype) initWithSource:(MPSNNImageNode *) sourceNode convolutionGradientState:(MPSCNNConvolutionGradientStateNode *) convolutionGradientState weights:(id<MPSCNNConvolutionDataSource>) weights;
```

## See Also

### Initializers
- [protocol MPSCNNConvolutionDataSource](../mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiontransposenode/init(source:convolutiongradientstate:weights:))*