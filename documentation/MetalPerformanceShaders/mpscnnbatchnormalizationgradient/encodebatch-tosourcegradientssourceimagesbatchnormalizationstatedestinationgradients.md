# encodeBatch(to:sourceGradients:sourceImages:batchNormalizationState:destinationGradients:)

**Framework**: Metal Performance Shaders  
**Kind**: method

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
func encodeBatch(to commandBuffer: any MTLCommandBuffer, sourceGradients: [MPSImage], sourceImages: [MPSImage], batchNormalizationState: MPSCNNBatchNormalizationState, destinationGradients: [MPSImage])
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbatchnormalizationgradient/encodebatch(to:sourcegradients:sourceimages:batchnormalizationstate:destinationgradients:))*