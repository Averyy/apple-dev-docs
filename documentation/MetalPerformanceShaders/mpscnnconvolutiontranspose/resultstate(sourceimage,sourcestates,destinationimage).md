# resultState(sourceImage:sourceStates:destinationImage:)

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
func resultState(sourceImage: MPSImage, sourceStates: [MPSCNNConvolutionGradientState]?, destinationImage: MPSImage) -> MPSCNNConvolutionTransposeGradientState?
```

```objc
- (MPSCNNConvolutionTransposeGradientState *) resultStateForSourceImage:(MPSImage *) sourceImage sourceStates:(NSArray<MPSCNNConvolutionGradientState *> *) sourceStates destinationImage:(MPSImage *) destinationImage;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiontranspose/resultstate(sourceimage:sourcestates:destinationimage:))*