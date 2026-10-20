# resultStateBatch(sourceImage:sourceStates:destinationImage:)

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
func resultStateBatch(sourceImage: [MPSImage], sourceStates: [[MPSCNNConvolutionGradientState]]?, destinationImage: [MPSImage]) -> [MPSCNNConvolutionTransposeGradientState]?
```

```objc
- (MPSCNNConvolutionTransposeGradientStateBatch *) resultStateBatchForSourceImage:(MPSImageBatch *) sourceImage sourceStates:(NSArray<NSArray<MPSCNNConvolutionGradientState *> *> *) sourceStates destinationImage:(MPSImageBatch *) destinationImage;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiontranspose/resultstatebatch(sourceimage:sourcestates:destinationimage:))*