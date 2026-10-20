# encodeSequence(commandBuffer:sourceImages:destinationImages:recurrentInputState:recurrentOutputStates:)

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
func encodeSequence(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationImages: [MPSImage], recurrentInputState: MPSRNNRecurrentImageState?, recurrentOutputStates: NSMutableArray?)
```

```objc
- (void) encodeSequenceToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceImages:(NSArray<MPSImage *> *) sourceImages destinationImages:(NSArray<MPSImage *> *) destinationImages recurrentInputState:(MPSRNNRecurrentImageState *) recurrentInputState recurrentOutputStates:(NSMutableArray<MPSRNNRecurrentImageState *> *) recurrentOutputStates;
```

## See Also

### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./copy%28with,device%29.md)
- [func encodeBidirectionalSequence(commandBuffer: any MTLCommandBuffer, sourceSequence: [MPSImage], destinationForwardImages: [MPSImage], destinationBackwardImages: [MPSImage]?)](./encodebidirectionalsequence%28commandbuffer,sourcesequence,destinationforwardimages,destinationbackwardimages%29.md)
- [class MPSRNNRecurrentImageState](../mpsrnnrecurrentimagestate.md)
  A class that holds all the data that’s passed from one sequence iteration of the image-based recurrent neural network layer (stack) to the next.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnimageinferencelayer/encodesequence(commandbuffer:sourceimages:destinationimages:recurrentinputstate:recurrentoutputstates:))*