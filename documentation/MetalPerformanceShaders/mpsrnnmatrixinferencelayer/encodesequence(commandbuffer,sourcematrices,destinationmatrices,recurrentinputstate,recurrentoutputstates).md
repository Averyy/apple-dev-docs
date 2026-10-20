# encodeSequence(commandBuffer:sourceMatrices:destinationMatrices:recurrentInputState:recurrentOutputStates:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func encodeSequence(commandBuffer: any MTLCommandBuffer, sourceMatrices: [MPSMatrix], destinationMatrices: [MPSMatrix], recurrentInputState: MPSRNNRecurrentMatrixState?, recurrentOutputStates: NSMutableArray?)
```

```objc
- (void) encodeSequenceToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceMatrices:(NSArray<MPSMatrix *> *) sourceMatrices destinationMatrices:(NSArray<MPSMatrix *> *) destinationMatrices recurrentInputState:(MPSRNNRecurrentMatrixState *) recurrentInputState recurrentOutputStates:(NSMutableArray<MPSRNNRecurrentMatrixState *> *) recurrentOutputStates;
```

## See Also

### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./copy%28with,device%29.md)
- [func encodeBidirectionalSequence(commandBuffer: any MTLCommandBuffer, sourceSequence: [MPSMatrix], destinationForwardMatrices: [MPSMatrix], destinationBackwardMatrices: [MPSMatrix]?)](./encodebidirectionalsequence%28commandbuffer,sourcesequence,destinationforwardmatrices,destinationbackwardmatrices%29.md)
- [class MPSRNNRecurrentMatrixState](../mpsrnnrecurrentmatrixstate.md)
  A class holds all the data that’s passed from one sequence iteration of the matrix-based recurrent neural network layer to the next.
- [func encodeSequence(commandBuffer: any MTLCommandBuffer, sourceMatrices: [MPSMatrix], sourceOffsets: UnsafeMutablePointer<Int>?, destinationMatrices: [MPSMatrix], destinationOffsets: UnsafeMutablePointer<Int>?, recurrentInputState: MPSRNNRecurrentMatrixState?, recurrentOutputStates: NSMutableArray?)](./encodesequence%28commandbuffer,sourcematrices,sourceoffsets,destinationmatrices,destinationoffsets,recurrentinputstate,recurrentoutputstates%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnmatrixinferencelayer/encodesequence(commandbuffer:sourcematrices:destinationmatrices:recurrentinputstate:recurrentoutputstates:))*