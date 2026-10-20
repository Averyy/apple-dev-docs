# exportWeightsAndBiases(with:resultStateCanBeTemporary:)

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
func exportWeightsAndBiases(with commandBuffer: any MTLCommandBuffer, resultStateCanBeTemporary: Bool) -> MPSCNNConvolutionWeightsAndBiasesState
```

```objc
- (MPSCNNConvolutionWeightsAndBiasesState *) exportWeightsAndBiasesWithCommandBuffer:(id<MTLCommandBuffer>) commandBuffer resultStateCanBeTemporary:(BOOL) resultStateCanBeTemporary;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiontranspose/exportweightsandbiases(with:resultstatecanbetemporary:))*