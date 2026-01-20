# MetalPerformanceShaders Functions

**Framework**: Metal Performance Shaders

## Topics

### Functions
- [func MPSDataTypeBitsCount(MPSDataType) -> Int](mpsdatatypebitscount(_:).md)
- [func MPSFindIntegerDivisionParams(UInt16) -> MPSIntegerDivisionParams](mpsfindintegerdivisionparams(_:).md)
  Returns the integer division parameters for a specified divisor.
- [func MPSGetCustomKernelBatchedDestinationIndex(MPSCustomKernelArgumentCount) -> UInt](mpsgetcustomkernelbatcheddestinationindex(_:).md)
  Returns the index of the first destination texture argument.
- [func MPSGetCustomKernelBatchedSourceIndex(MPSCustomKernelArgumentCount, UInt, UInt) -> UInt](mpsgetcustomkernelbatchedsourceindex(_:_:_:).md)
  Returns the index of the specified batched source texture argument.
- [func MPSGetCustomKernelBroadcastSourceIndex(MPSCustomKernelArgumentCount, UInt, UInt) -> UInt](mpsgetcustomkernelbroadcastsourceindex(_:_:_:).md)
  Returns the index of the specified nonbatched source texture argument.
- [func MPSGetCustomKernelMaxBatchSize(MPSCustomKernelArgumentCount, UInt) -> UInt](mpsgetcustomkernelmaxbatchsize(_:_:).md)
  Returns the maximum allowed batch size.
- [func MPSGetImageType(MPSImage) -> MPSImageType](mpsgetimagetype(_:).md)
- [func MPSGetPreferredDevice(MPSDeviceOptions) -> (any MTLDevice)?](mpsgetpreferreddevice(_:).md)
- [func MPSHintTemporaryMemoryHighWaterMark(any MTLCommandBuffer, Int)](mpshinttemporarymemoryhighwatermark(_:_:).md)
  Triggers Metal Performance Shaders to prefetch a Metal heap of the indicated size into its internal cache.
- [func MPSImageBatchIncrementReadCount([MPSImage], Int) -> Int](mpsimagebatchincrementreadcount(_:_:).md)
  Increments or decrements the read count of an image batch by a specified amount.
- [func MPSImageBatchIterate([MPSImage], (MPSImage, Int) -> Int) -> Int](mpsimagebatchiterate(_:_:).md)
  Executes a callback block once for each unique image in a batch.
- [func MPSImageBatchResourceSize([MPSImage]) -> Int](mpsimagebatchresourcesize(_:).md)
  Returns the number of bytes used to allocate the specified image batch.
- [func MPSImageBatchSynchronize([MPSImage], any MTLCommandBuffer)](mpsimagebatchsynchronize(_:_:).md)
  Removes any copy of the specified image batch from the device’s caches, and, if needed, invalidates any CPU caches.
- [func MPSSetHeapCacheDuration(any MTLCommandBuffer, Double)](mpssetheapcacheduration(_:_:).md)
  Sets the timeout after which unused cached Metal heaps are released.
- [func MPSSizeofMPSDataType(MPSDataType) -> Int](mpssizeofmpsdatatype(_:).md)
- [func MPSStateBatchIncrementReadCount([MPSState]?, Int) -> Int](mpsstatebatchincrementreadcount(_:_:).md)
  Increments or decrements the read count of a state batch by a specified amount.
- [func MPSStateBatchResourceSize([MPSState]?) -> Int](mpsstatebatchresourcesize(_:).md)
  Returns the number of bytes used to allocate the specified state batch.
- [func MPSStateBatchSynchronize([MPSState], any MTLCommandBuffer)](mpsstatebatchsynchronize(_:_:).md)
  Removes any copy of the specified state batch from the device’s caches, and, if needed, invalidates any CPU caches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/metalperformanceshaders-functions)*