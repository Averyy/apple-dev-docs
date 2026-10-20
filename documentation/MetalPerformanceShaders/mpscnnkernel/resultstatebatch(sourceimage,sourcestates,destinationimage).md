# resultStateBatch(sourceImage:sourceStates:destinationImage:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
func resultStateBatch(sourceImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSState]?
```

```objc
- (MPSStateBatch *) resultStateBatchForSourceImage:(MPSImageBatch *) sourceImage sourceStates:(NSArray<NSArray<MPSState *> *> *) sourceStates destinationImage:(MPSImageBatch *) destinationImage;
```

## See Also

### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage) -> MPSImage](./encode%28commandbuffer,sourceimage%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationImage: MPSImage)](./encode%28commandbuffer,sourceimage,destinationimage%29.md)
  Encodes a kernel into a command buffer.  The ensuing operation proceeds out-of-place.
- [func appendBatchBarrier() -> Bool](./appendbatchbarrier%28%29.md)
- [func batchEncodingStorageSize(sourceImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]?) -> Int](./batchencodingstoragesize%28sourceimage,sourcestates,destinationimage%29.md)
- [func destinationImageDescriptor(sourceImages: [MPSImage], sourceStates: [MPSState]?) -> MPSImageDescriptor](./destinationimagedescriptor%28sourceimages,sourcestates%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationState: MPSState, destinationImage: MPSImage)](./encode%28commandbuffer,sourceimage,destinationstate,destinationimage%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationState: AutoreleasingUnsafeMutablePointer<MPSState?>, destinationStateIsTemporary: Bool) -> MPSImage](./encode%28commandbuffer,sourceimage,destinationstate,destinationstateistemporary%29.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage]) -> [MPSImage]](./encodebatch%28commandbuffer,sourceimages%29.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationImages: [MPSImage])](./encodebatch%28commandbuffer,sourceimages,destinationimages%29.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationStates: [MPSState]?, destinationImages: [MPSImage])](./encodebatch%28commandbuffer,sourceimages,destinationstates,destinationimages%29.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationStates: AutoreleasingUnsafeMutablePointer<NSArray?>, destinationStateIsTemporary: Bool) -> [MPSImage]](./encodebatch%28commandbuffer,sourceimages,destinationstates,destinationstateistemporary%29.md)
- [func encodingStorageSize(sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage?) -> Int](./encodingstoragesize%28sourceimage,sourcestates,destinationimage%29.md)
- [func isResultStateReusedAcrossBatch() -> Bool](./isresultstatereusedacrossbatch%28%29.md)
- [func resultState(sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?](./resultstate%28sourceimage,sourcestates,destinationimage%29.md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?](./temporaryresultstate%28commandbuffer,sourceimage,sourcestates,destinationimage%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnkernel/resultstatebatch(sourceimage:sourcestates:destinationimage:))*