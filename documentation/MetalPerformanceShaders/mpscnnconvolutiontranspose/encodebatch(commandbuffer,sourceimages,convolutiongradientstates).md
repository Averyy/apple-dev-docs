# encodeBatch(commandBuffer:sourceImages:convolutionGradientStates:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages sourceImage: [MPSImage], convolutionGradientStates convolutionGradientState: [MPSCNNConvolutionGradientState]?) -> [MPSImage]
```

```objc
- (MPSImageBatch *) encodeBatchToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceImages:(MPSImageBatch *) sourceImage convolutionGradientStates:(MPSCNNConvolutionGradientStateBatch *) convolutionGradientState;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiontranspose/encodebatch(commandbuffer:sourceimages:convolutiongradientstates:))*