# encodingStorageSize(primaryImage:secondaryImage:sourceStates:destinationImage:)

**Framework**: Metal Performance Shaders  
**Kind**: method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func encodingStorageSize(primaryImage: MPSImage, secondaryImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage?) -> Int
```

## See Also

- [func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage) -> MPSImage](mpscnnbinarykernel/encode(commandbuffer:primaryimage:secondaryimage:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, destinationImage: MPSImage)](mpscnnbinarykernel/encode(commandbuffer:primaryimage:secondaryimage:destinationimage:).md)
- [func appendBatchBarrier() -> Bool](mpscnnbinarykernel/appendbatchbarrier.md)
- [func batchEncodingStorageSize(primaryImage: [MPSImage], secondaryImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]?) -> Int](mpscnnbinarykernel/batchencodingstoragesize(primaryimage:secondaryimage:sourcestates:destinationimage:).md)
- [func destinationImageDescriptor(forSourceImages: [MPSImage], sourceStates: [MPSState]?) -> MPSImageDescriptor](mpscnnbinarykernel/destinationimagedescriptor(forsourceimages:sourcestates:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, destinationState: AutoreleasingUnsafeMutablePointer<MPSState?>, destinationStateIsTemporary: Bool) -> MPSImage](mpscnnbinarykernel/encode(commandbuffer:primaryimage:secondaryimage:destinationstate:destinationstateistemporary:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, primaryImages: [MPSImage], secondaryImages: [MPSImage]) -> [MPSImage]](mpscnnbinarykernel/encodebatch(commandbuffer:primaryimages:secondaryimages:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, primaryImages: [MPSImage], secondaryImages: [MPSImage], destinationImages: [MPSImage])](mpscnnbinarykernel/encodebatch(commandbuffer:primaryimages:secondaryimages:destinationimages:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, primaryImages: [MPSImage], secondaryImages: [MPSImage], destinationStates: AutoreleasingUnsafeMutablePointer<NSArray?>, destinationStateIsTemporary: Bool) -> [MPSImage]](mpscnnbinarykernel/encodebatch(commandbuffer:primaryimages:secondaryimages:destinationstates:destinationstateistemporary:).md)
- [func isResultStateReusedAcrossBatch() -> Bool](mpscnnbinarykernel/isresultstatereusedacrossbatch.md)
- [func resultState(primaryImage: MPSImage, secondaryImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?](mpscnnbinarykernel/resultstate(primaryimage:secondaryimage:sourcestates:destinationimage:).md)
- [func resultStateBatch(primaryImage: [MPSImage], secondaryImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSState]?](mpscnnbinarykernel/resultstatebatch(primaryimage:secondaryimage:sourcestates:destinationimage:).md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?](mpscnnbinarykernel/temporaryresultstate(commandbuffer:primaryimage:secondaryimage:sourcestates:destinationimage:).md)
- [func temporaryResultStateBatch(commandBuffer: any MTLCommandBuffer, primaryImage: [MPSImage], secondaryImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSState]?](mpscnnbinarykernel/temporaryresultstatebatch(commandbuffer:primaryimage:secondaryimage:sourcestates:destinationimage:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbinarykernel/encodingstoragesize(primaryimage:secondaryimage:sourcestates:destinationimage:))*