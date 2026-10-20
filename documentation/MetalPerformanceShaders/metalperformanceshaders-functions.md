# MetalPerformanceShaders Functions

**Framework**: Metal Performance Shaders  
**Role**: API Collection

## Topics

### Functions
- [func MPSDataTypeBitsCount(MPSDataType) -> Int](./mpsdatatypebitscount%28_%29.md)
- [func MPSFindIntegerDivisionParams(UInt16) -> MPSIntegerDivisionParams](./mpsfindintegerdivisionparams%28_%29.md)
  Returns the integer division parameters for a specified divisor.
- [func MPSGetCustomKernelBatchedDestinationIndex(MPSCustomKernelArgumentCount) -> UInt](./mpsgetcustomkernelbatcheddestinationindex%28_%29.md)
  Returns the index of the first destination texture argument.
- [func MPSGetCustomKernelBatchedSourceIndex(MPSCustomKernelArgumentCount, UInt, UInt) -> UInt](./mpsgetcustomkernelbatchedsourceindex%28_,_,_%29.md)
  Returns the index of the specified batched source texture argument.
- [func MPSGetCustomKernelBroadcastSourceIndex(MPSCustomKernelArgumentCount, UInt, UInt) -> UInt](./mpsgetcustomkernelbroadcastsourceindex%28_,_,_%29.md)
  Returns the index of the specified nonbatched source texture argument.
- [func MPSGetCustomKernelMaxBatchSize(MPSCustomKernelArgumentCount, UInt) -> UInt](./mpsgetcustomkernelmaxbatchsize%28_,_%29.md)
  Returns the maximum allowed batch size.
- [func MPSGetImageType(MPSImage) -> MPSImageType](./mpsgetimagetype%28_%29.md)
- [func MPSGetPreferredDevice(MPSDeviceOptions) -> (any MTLDevice)?](./mpsgetpreferreddevice%28_%29.md)
- [func MPSHintTemporaryMemoryHighWaterMark(any MTLCommandBuffer, Int)](./mpshinttemporarymemoryhighwatermark%28_,_%29.md)
  Triggers Metal Performance Shaders to prefetch a Metal heap of the indicated size into its internal cache.
- [func MPSImageBatchIncrementReadCount([MPSImage], Int) -> Int](./mpsimagebatchincrementreadcount%28_,_%29.md)
  Increments or decrements the read count of an image batch by a specified amount.
- [func MPSImageBatchIterate([MPSImage], (MPSImage, Int) -> Int) -> Int](./mpsimagebatchiterate%28_,_%29.md)
  Executes a callback block once for each unique image in a batch.
- [func MPSImageBatchResourceSize([MPSImage]) -> Int](./mpsimagebatchresourcesize%28_%29.md)
  Returns the number of bytes used to allocate the specified image batch.
- [func MPSImageBatchSynchronize([MPSImage], any MTLCommandBuffer)](./mpsimagebatchsynchronize%28_,_%29.md)
  Removes any copy of the specified image batch from the device’s caches, and, if needed, invalidates any CPU caches.
- [func MPSSetHeapCacheDuration(any MTLCommandBuffer, Double)](./mpssetheapcacheduration%28_,_%29.md)
  Sets the timeout after which unused cached Metal heaps are released.
- [func MPSSizeofMPSDataType(MPSDataType) -> Int](./mpssizeofmpsdatatype%28_%29.md)
- [func MPSStateBatchIncrementReadCount([MPSState]?, Int) -> Int](./mpsstatebatchincrementreadcount%28_,_%29.md)
  Increments or decrements the read count of a state batch by a specified amount.
- [func MPSStateBatchResourceSize([MPSState]?) -> Int](./mpsstatebatchresourcesize%28_%29.md)
  Returns the number of bytes used to allocate the specified state batch.
- [func MPSStateBatchSynchronize([MPSState], any MTLCommandBuffer)](./mpsstatebatchsynchronize%28_,_%29.md)
  Removes any copy of the specified state batch from the device’s caches, and, if needed, invalidates any CPU caches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/metalperformanceshaders-functions)*