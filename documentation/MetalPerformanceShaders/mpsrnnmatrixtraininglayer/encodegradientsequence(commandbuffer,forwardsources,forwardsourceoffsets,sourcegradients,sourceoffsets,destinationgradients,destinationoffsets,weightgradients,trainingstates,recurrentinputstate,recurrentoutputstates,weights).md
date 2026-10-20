# encodeGradientSequence(commandBuffer:forwardSources:forwardSourceOffsets:sourceGradients:sourceOffsets:destinationGradients:destinationOffsets:weightGradients:trainingStates:recurrentInputState:recurrentOutputStates:weights:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func encodeGradientSequence(commandBuffer: any MTLCommandBuffer, forwardSources: [MPSMatrix], forwardSourceOffsets: UnsafeMutablePointer<Int>?, sourceGradients: [MPSMatrix], sourceOffsets sourceGradientOffsets: UnsafeMutablePointer<Int>?, destinationGradients: [MPSMatrix]?, destinationOffsets: UnsafeMutablePointer<Int>?, weightGradients: [MPSMatrix]?, trainingStates: [MPSRNNMatrixTrainingState], recurrentInputState: MPSRNNRecurrentMatrixState?, recurrentOutputStates: NSMutableArray?, weights: [MPSMatrix])
```

```objc
- (void) encodeGradientSequenceToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer forwardSources:(NSArray<MPSMatrix *> *) forwardSources forwardSourceOffsets:(NSUInteger *) forwardSourceOffsets sourceGradients:(NSArray<MPSMatrix *> *) sourceGradients sourceGradientOffsets:(NSUInteger *) sourceGradientOffsets destinationGradients:(NSArray<MPSMatrix *> *) destinationGradients destinationOffsets:(NSUInteger *) destinationOffsets weightGradients:(NSArray<MPSMatrix *> *) weightGradients trainingStates:(NSArray<MPSRNNMatrixTrainingState *> *) trainingStates recurrentInputState:(MPSRNNRecurrentMatrixState *) recurrentInputState recurrentOutputStates:(NSMutableArray<MPSRNNRecurrentMatrixState *> *) recurrentOutputStates weights:(NSArray<MPSMatrix *> *) weights;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnmatrixtraininglayer/encodegradientsequence(commandbuffer:forwardsources:forwardsourceoffsets:sourcegradients:sourceoffsets:destinationgradients:destinationoffsets:weightgradients:trainingstates:recurrentinputstate:recurrentoutputstates:weights:))*