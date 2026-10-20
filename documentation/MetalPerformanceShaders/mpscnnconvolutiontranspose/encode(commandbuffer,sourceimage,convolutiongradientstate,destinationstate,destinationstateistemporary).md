# encode(commandBuffer:sourceImage:convolutionGradientState:destinationState:destinationStateIsTemporary:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, convolutionGradientState: MPSCNNConvolutionGradientState?, destinationState outState: AutoreleasingUnsafeMutablePointer<MPSCNNConvolutionTransposeGradientState?>, destinationStateIsTemporary isTemporary: Bool) -> MPSImage
```

```objc
- (MPSImage *) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceImage:(MPSImage *) sourceImage convolutionGradientState:(MPSCNNConvolutionGradientState *) convolutionGradientState destinationState:(MPSCNNConvolutionTransposeGradientState **) outState destinationStateIsTemporary:(BOOL) isTemporary;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiontranspose/encode(commandbuffer:sourceimage:convolutiongradientstate:destinationstate:destinationstateistemporary:))*