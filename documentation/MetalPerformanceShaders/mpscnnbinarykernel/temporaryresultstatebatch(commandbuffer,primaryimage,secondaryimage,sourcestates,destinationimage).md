# temporaryResultStateBatch(commandBuffer:primaryImage:secondaryImage:sourceStates:destinationImage:)

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
func temporaryResultStateBatch(commandBuffer: any MTLCommandBuffer, primaryImage: [MPSImage], secondaryImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSState]?
```

```objc
- (MPSStateBatch *) temporaryResultStateBatchForCommandBuffer:(id<MTLCommandBuffer>) commandBuffer primaryImage:(MPSImageBatch *) primaryImage secondaryImage:(MPSImageBatch *) secondaryImage sourceStates:(NSArray<NSArray<MPSState *> *> *) sourceStates destinationImage:(MPSImageBatch *) destinationImage;
```

## See Also

### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage) -> MPSImage](./encode%28commandbuffer,primaryimage,secondaryimage%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, destinationImage: MPSImage)](./encode%28commandbuffer,primaryimage,secondaryimage,destinationimage%29.md)
- [func appendBatchBarrier() -> Bool](./appendbatchbarrier%28%29.md)
- [func batchEncodingStorageSize(primaryImage: [MPSImage], secondaryImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]?) -> Int](./batchencodingstoragesize%28primaryimage,secondaryimage,sourcestates,destinationimage%29.md)
- [func destinationImageDescriptor(forSourceImages: [MPSImage], sourceStates: [MPSState]?) -> MPSImageDescriptor](./destinationimagedescriptor%28forsourceimages,sourcestates%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, destinationState: AutoreleasingUnsafeMutablePointer<MPSState?>, destinationStateIsTemporary: Bool) -> MPSImage](./encode%28commandbuffer,primaryimage,secondaryimage,destinationstate,destinationstateistemporary%29.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, primaryImages: [MPSImage], secondaryImages: [MPSImage]) -> [MPSImage]](./encodebatch%28commandbuffer,primaryimages,secondaryimages%29.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, primaryImages: [MPSImage], secondaryImages: [MPSImage], destinationImages: [MPSImage])](./encodebatch%28commandbuffer,primaryimages,secondaryimages,destinationimages%29.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, primaryImages: [MPSImage], secondaryImages: [MPSImage], destinationStates: AutoreleasingUnsafeMutablePointer<NSArray?>, destinationStateIsTemporary: Bool) -> [MPSImage]](./encodebatch%28commandbuffer,primaryimages,secondaryimages,destinationstates,destinationstateistemporary%29.md)
- [func encodingStorageSize(primaryImage: MPSImage, secondaryImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage?) -> Int](./encodingstoragesize%28primaryimage,secondaryimage,sourcestates,destinationimage%29.md)
- [func isResultStateReusedAcrossBatch() -> Bool](./isresultstatereusedacrossbatch%28%29.md)
- [func resultState(primaryImage: MPSImage, secondaryImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?](./resultstate%28primaryimage,secondaryimage,sourcestates,destinationimage%29.md)
- [func resultStateBatch(primaryImage: [MPSImage], secondaryImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSState]?](./resultstatebatch%28primaryimage,secondaryimage,sourcestates,destinationimage%29.md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?](./temporaryresultstate%28commandbuffer,primaryimage,secondaryimage,sourcestates,destinationimage%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbinarykernel/temporaryresultstatebatch(commandbuffer:primaryimage:secondaryimage:sourcestates:destinationimage:))*