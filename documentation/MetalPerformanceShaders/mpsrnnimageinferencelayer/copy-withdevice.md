# copy(with:device:)

**Framework**: Metal Performance Shaders  
**Kind**: method

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

## See Also

- [func encodeBidirectionalSequence(commandBuffer: any MTLCommandBuffer, sourceSequence: [MPSImage], destinationForwardImages: [MPSImage], destinationBackwardImages: [MPSImage]?)](mpsrnnimageinferencelayer/encodebidirectionalsequence(commandbuffer:sourcesequence:destinationforwardimages:destinationbackwardimages:).md)
- [func encodeSequence(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationImages: [MPSImage], recurrentInputState: MPSRNNRecurrentImageState?, recurrentOutputStates: NSMutableArray?)](mpsrnnimageinferencelayer/encodesequence(commandbuffer:sourceimages:destinationimages:recurrentinputstate:recurrentoutputstates:).md)
- [class MPSRNNRecurrentImageState](mpsrnnrecurrentimagestate.md)
  A class that holds all the data that’s passed from one sequence iteration of the image-based recurrent neural network layer (stack) to the next.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnimageinferencelayer/copy(with:device:))*