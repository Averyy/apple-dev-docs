# MPSRNNRecurrentImageState

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A class that holds all the data that’s passed from one sequence iteration of the image-based recurrent neural network layer (stack) to the next.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSRNNRecurrentImageState
```

```objc
@interface MPSRNNRecurrentImageState : MPSState
```

## Topics

### Instance Methods
- [func getMemoryCellImage(forLayerIndex: Int) -> MPSImage?](./mpsrnnrecurrentimagestate/getmemorycellimage%28forlayerindex%29.md)
- [func getRecurrentOutputImage(forLayerIndex: Int) -> MPSImage?](./mpsrnnrecurrentimagestate/getrecurrentoutputimage%28forlayerindex%29.md)

## Relationships

### Inherits From
- [MPSState](./mpsstate.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./mpsrnnimageinferencelayer/copy%28with,device%29.md)
- [func encodeBidirectionalSequence(commandBuffer: any MTLCommandBuffer, sourceSequence: [MPSImage], destinationForwardImages: [MPSImage], destinationBackwardImages: [MPSImage]?)](./mpsrnnimageinferencelayer/encodebidirectionalsequence%28commandbuffer,sourcesequence,destinationforwardimages,destinationbackwardimages%29.md)
- [func encodeSequence(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationImages: [MPSImage], recurrentInputState: MPSRNNRecurrentImageState?, recurrentOutputStates: NSMutableArray?)](./mpsrnnimageinferencelayer/encodesequence%28commandbuffer,sourceimages,destinationimages,recurrentinputstate,recurrentoutputstates%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnrecurrentimagestate)*