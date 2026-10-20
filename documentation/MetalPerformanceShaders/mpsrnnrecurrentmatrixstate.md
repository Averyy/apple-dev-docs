# MPSRNNRecurrentMatrixState

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A class holds all the data that’s passed from one sequence iteration of the matrix-based recurrent neural network layer to the next.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSRNNRecurrentMatrixState
```

```objc
@interface MPSRNNRecurrentMatrixState : MPSState
```

## Topics

### Instance Methods
- [func getMemoryCellMatrix(forLayerIndex: Int) -> MPSMatrix?](./mpsrnnrecurrentmatrixstate/getmemorycellmatrix%28forlayerindex%29.md)
- [func getRecurrentOutputMatrix(forLayerIndex: Int) -> MPSMatrix?](./mpsrnnrecurrentmatrixstate/getrecurrentoutputmatrix%28forlayerindex%29.md)

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
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./mpsrnnmatrixinferencelayer/copy%28with,device%29.md)
- [func encodeBidirectionalSequence(commandBuffer: any MTLCommandBuffer, sourceSequence: [MPSMatrix], destinationForwardMatrices: [MPSMatrix], destinationBackwardMatrices: [MPSMatrix]?)](./mpsrnnmatrixinferencelayer/encodebidirectionalsequence%28commandbuffer,sourcesequence,destinationforwardmatrices,destinationbackwardmatrices%29.md)
- [func encodeSequence(commandBuffer: any MTLCommandBuffer, sourceMatrices: [MPSMatrix], destinationMatrices: [MPSMatrix], recurrentInputState: MPSRNNRecurrentMatrixState?, recurrentOutputStates: NSMutableArray?)](./mpsrnnmatrixinferencelayer/encodesequence%28commandbuffer,sourcematrices,destinationmatrices,recurrentinputstate,recurrentoutputstates%29.md)
- [func encodeSequence(commandBuffer: any MTLCommandBuffer, sourceMatrices: [MPSMatrix], sourceOffsets: UnsafeMutablePointer<Int>?, destinationMatrices: [MPSMatrix], destinationOffsets: UnsafeMutablePointer<Int>?, recurrentInputState: MPSRNNRecurrentMatrixState?, recurrentOutputStates: NSMutableArray?)](./mpsrnnmatrixinferencelayer/encodesequence%28commandbuffer,sourcematrices,sourceoffsets,destinationmatrices,destinationoffsets,recurrentinputstate,recurrentoutputstates%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnrecurrentmatrixstate)*