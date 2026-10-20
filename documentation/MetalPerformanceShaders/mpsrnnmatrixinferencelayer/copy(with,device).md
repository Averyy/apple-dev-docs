# copy(with:device:)

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
func copy(with zone: NSZone? = nil, device: (any MTLDevice)?) -> Self
```

```objc
- (instancetype) copyWithZone:(NSZone *) zone device:(id<MTLDevice>) device;
```

## See Also

### Instance Methods
- [func encodeBidirectionalSequence(commandBuffer: any MTLCommandBuffer, sourceSequence: [MPSMatrix], destinationForwardMatrices: [MPSMatrix], destinationBackwardMatrices: [MPSMatrix]?)](./encodebidirectionalsequence%28commandbuffer,sourcesequence,destinationforwardmatrices,destinationbackwardmatrices%29.md)
- [func encodeSequence(commandBuffer: any MTLCommandBuffer, sourceMatrices: [MPSMatrix], destinationMatrices: [MPSMatrix], recurrentInputState: MPSRNNRecurrentMatrixState?, recurrentOutputStates: NSMutableArray?)](./encodesequence%28commandbuffer,sourcematrices,destinationmatrices,recurrentinputstate,recurrentoutputstates%29.md)
- [class MPSRNNRecurrentMatrixState](../mpsrnnrecurrentmatrixstate.md)
  A class holds all the data that’s passed from one sequence iteration of the matrix-based recurrent neural network layer to the next.
- [func encodeSequence(commandBuffer: any MTLCommandBuffer, sourceMatrices: [MPSMatrix], sourceOffsets: UnsafeMutablePointer<Int>?, destinationMatrices: [MPSMatrix], destinationOffsets: UnsafeMutablePointer<Int>?, recurrentInputState: MPSRNNRecurrentMatrixState?, recurrentOutputStates: NSMutableArray?)](./encodesequence%28commandbuffer,sourcematrices,sourceoffsets,destinationmatrices,destinationoffsets,recurrentinputstate,recurrentoutputstates%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnmatrixinferencelayer/copy(with:device:))*