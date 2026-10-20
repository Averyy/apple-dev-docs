# encodeForwardSequence(commandBuffer:sourceMatrices:sourceOffsets:destinationMatrices:destinationOffsets:trainingStates:recurrentInputState:recurrentOutputStates:weights:)

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
func encodeForwardSequence(commandBuffer: any MTLCommandBuffer, sourceMatrices: [MPSMatrix], sourceOffsets: UnsafeMutablePointer<Int>?, destinationMatrices: [MPSMatrix], destinationOffsets: UnsafeMutablePointer<Int>?, trainingStates: NSMutableArray, recurrentInputState: MPSRNNRecurrentMatrixState?, recurrentOutputStates: NSMutableArray?, weights: [MPSMatrix])
```

```objc
- (void) encodeForwardSequenceToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceMatrices:(NSArray<MPSMatrix *> *) sourceMatrices sourceOffsets:(NSUInteger *) sourceOffsets destinationMatrices:(NSArray<MPSMatrix *> *) destinationMatrices destinationOffsets:(NSUInteger *) destinationOffsets trainingStates:(NSMutableArray<MPSRNNMatrixTrainingState *> *) trainingStates recurrentInputState:(MPSRNNRecurrentMatrixState *) recurrentInputState recurrentOutputStates:(NSMutableArray<MPSRNNRecurrentMatrixState *> *) recurrentOutputStates weights:(NSArray<MPSMatrix *> *) weights;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnmatrixtraininglayer/encodeforwardsequence(commandbuffer:sourcematrices:sourceoffsets:destinationmatrices:destinationoffsets:trainingstates:recurrentinputstate:recurrentoutputstates:weights:))*