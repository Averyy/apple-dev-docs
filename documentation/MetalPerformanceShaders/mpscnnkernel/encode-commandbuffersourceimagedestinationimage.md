# encode(commandBuffer:sourceImage:destinationImage:)

**Framework**: Metal Performance Shaders  
**Kind**: method

Encodes a kernel into a command buffer.  The ensuing operation proceeds out-of-place.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationImage: MPSImage)
```

#### Discussion

The `destinationImage` object may not alias the `sourceImage` object.

## Parameters

- `commandBuffer`: A valid command buffer to receive the encoded filter.
- `sourceImage`: A valid source image.
- `destinationImage`: A valid destination image to be overwritten by the results.

## See Also

- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage) -> MPSImage](mpscnnkernel/encode(commandbuffer:sourceimage:).md)
- [func appendBatchBarrier() -> Bool](mpscnnkernel/appendbatchbarrier.md)
- [func batchEncodingStorageSize(sourceImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]?) -> Int](mpscnnkernel/batchencodingstoragesize(sourceimage:sourcestates:destinationimage:).md)
- [func destinationImageDescriptor(sourceImages: [MPSImage], sourceStates: [MPSState]?) -> MPSImageDescriptor](mpscnnkernel/destinationimagedescriptor(sourceimages:sourcestates:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationState: MPSState, destinationImage: MPSImage)](mpscnnkernel/encode(commandbuffer:sourceimage:destinationstate:destinationimage:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationState: AutoreleasingUnsafeMutablePointer<MPSState?>, destinationStateIsTemporary: Bool) -> MPSImage](mpscnnkernel/encode(commandbuffer:sourceimage:destinationstate:destinationstateistemporary:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage]) -> [MPSImage]](mpscnnkernel/encodebatch(commandbuffer:sourceimages:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationImages: [MPSImage])](mpscnnkernel/encodebatch(commandbuffer:sourceimages:destinationimages:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationStates: [MPSState]?, destinationImages: [MPSImage])](mpscnnkernel/encodebatch(commandbuffer:sourceimages:destinationstates:destinationimages:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationStates: AutoreleasingUnsafeMutablePointer<NSArray?>, destinationStateIsTemporary: Bool) -> [MPSImage]](mpscnnkernel/encodebatch(commandbuffer:sourceimages:destinationstates:destinationstateistemporary:).md)
- [func encodingStorageSize(sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage?) -> Int](mpscnnkernel/encodingstoragesize(sourceimage:sourcestates:destinationimage:).md)
- [func isResultStateReusedAcrossBatch() -> Bool](mpscnnkernel/isresultstatereusedacrossbatch.md)
- [func resultState(sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?](mpscnnkernel/resultstate(sourceimage:sourcestates:destinationimage:).md)
- [func resultStateBatch(sourceImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSState]?](mpscnnkernel/resultstatebatch(sourceimage:sourcestates:destinationimage:).md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?](mpscnnkernel/temporaryresultstate(commandbuffer:sourceimage:sourcestates:destinationimage:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnkernel/encode(commandbuffer:sourceimage:destinationimage:))*