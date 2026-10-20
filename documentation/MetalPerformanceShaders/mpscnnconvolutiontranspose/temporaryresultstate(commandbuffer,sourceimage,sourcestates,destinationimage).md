# temporaryResultState(commandBuffer:sourceImage:sourceStates:destinationImage:)

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
func temporaryResultState(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, sourceStates: [MPSCNNConvolutionGradientState]?, destinationImage: MPSImage) -> MPSCNNConvolutionTransposeGradientState?
```

```objc
- (MPSCNNConvolutionTransposeGradientState *) temporaryResultStateForCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceImage:(MPSImage *) sourceImage sourceStates:(NSArray<MPSCNNConvolutionGradientState *> *) sourceStates destinationImage:(MPSImage *) destinationImage;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiontranspose/temporaryresultstate(commandbuffer:sourceimage:sourcestates:destinationimage:))*