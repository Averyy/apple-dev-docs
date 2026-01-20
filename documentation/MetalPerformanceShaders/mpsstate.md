# MPSState

**Framework**: Metal Performance Shaders  
**Kind**: class

An opaque data container for large storage in MPS CNN filters.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSState
```

#### Overview

Some MPS CNN kernels produce additional information beyond an [`MPSImage`](mpsimage.md). These may be pooling indices where the result came from, convolution weights, or other information not contained in the usual [`MPSImage`](mpsimage.md) result from a [`MPSCNNKernel`](mpscnnkernel.md). An [`MPSState`](mpsstate.md) object typically contains one or more expensive [`MTLResource`](https://developer.apple.com/documentation/Metal/MTLResource) objects such as textures or buffers to store this information. It provides a base class with interfaces for managing this storage. Child classes may add additional functionality specific to their contents.

Some [`MPSState`](mpsstate.md) objects are temporary. Temporary state objects, for example, [`MPSTemporaryImage`](mpstemporaryimage.md) and [`MPSTemporaryMatrix`](mpstemporarymatrix.md), are for very short lived storage, perhaps just a few lines of code within the scope of a single [`MTLCommandBuffer`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer). They are very efficient for storage, as several temporary objects can share the same memory over the course of a command buffer. This can improve both memory usage and time spent in the kernel wiring down memory and such. You may find that some large CNN tasks can not be computed without them, as nontemporary storage would simply take up too much memory.

In exchange, the lifetime of the underlying storage in temporary [`MPSState`](mpsstate.md) objects needs to be carefully managed. ARC often waits until the end of scope to release objects. Temporary storage often needs to be released sooner than that. Consequently the lifetime of the data in the underlying Metal resources is managed by a [`readCount`](mpsstate/readcount.md) property. Each time a [`MPSCNNKernel`](mpscnnkernel.md) reads a temporary [`MPSState`](mpsstate.md) object the [`readCount`](mpsstate/readcount.md) is automatically decremented. When it reaches 0, the underlying storage is recycled for use by other MPS temporary objects, and the data is becomes undefined. If you need to consume the data multiple times, you should set the [`readCount`](mpsstate/readcount.md) to a larger number to prevent the data from becoming undefined. You may set the [`readCount`](mpsstate/readcount.md) to 0 yourself to return the storage to MPS, if for any reason, you realize that the [`MPSState`](mpsstate.md) object will no longer be used.

The contents of a temporary [`MPSState`](mpsstate.md) object are only valid from creation to the time the [`readCount`](mpsstate/readcount.md) reaches 0. The data is only valid for the [`MTLCommandBuffer`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer) on which it was created. Nontemporary [`MPSState`](mpsstate.md) objects are valid on any [`MTLCommandBuffer`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer) on the same device until they are released.

## Topics

### Instance Properties
- [var isTemporary: Bool](mpsstate/istemporary.md)
- [var label: String?](mpsstate/label.md)
- [var readCount: Int](mpsstate/readcount.md)
- [var resource: (any MTLResource)?](mpsstate/resource.md)
- [var resourceCount: Int](mpsstate/resourcecount.md)
### Initializers
- [init(device: any MTLDevice, bufferSize: Int)](mpsstate/init(device:buffersize:).md)
- [init(device: any MTLDevice, resourceList: MPSStateResourceList)](mpsstate/init(device:resourcelist:).md)
- [init(device: any MTLDevice, textureDescriptor: MTLTextureDescriptor)](mpsstate/init(device:texturedescriptor:).md)
- [init(resource: (any MTLResource)?)](mpsstate/init(resource:).md)
- [init(resources: [any MTLResource]?)](mpsstate/init(resources:).md)
### Instance Methods
- [func bufferSize(at: Int) -> Int](mpsstate/buffersize(at:).md)
- [func destinationImageDescriptor(forSourceImages: [MPSImage], sourceStates: [MPSState]?, for: MPSKernel, suggestedDescriptor: MPSImageDescriptor) -> MPSImageDescriptor](mpsstate/destinationimagedescriptor(forsourceimages:sourcestates:for:suggesteddescriptor:).md)
- [func resource(at: Int, allocateMemory: Bool) -> (any MTLResource)?](mpsstate/resource(at:allocatememory:).md)
- [func resourceSize() -> Int](mpsstate/resourcesize.md)
- [func resourceType(at: Int) -> MPSStateResourceType](mpsstate/resourcetype(at:).md)
- [func synchronize(on: any MTLCommandBuffer)](mpsstate/synchronize(on:).md)
- [func textureInfo(at: Int) -> MPSStateTextureInfo](mpsstate/textureinfo(at:).md)
### Type Methods
- [class func temporaryState(with: any MTLCommandBuffer) -> Self](mpsstate/temporarystate(with:).md)
- [class func temporaryState(with: any MTLCommandBuffer, bufferSize: Int) -> Self](mpsstate/temporarystate(with:buffersize:).md)
- [class func temporaryState(with: any MTLCommandBuffer, resourceList: MPSStateResourceList) -> Self](mpsstate/temporarystate(with:resourcelist:).md)
- [class func temporaryState(with: any MTLCommandBuffer, textureDescriptor: MTLTextureDescriptor) -> Self](mpsstate/temporarystate(with:texturedescriptor:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MPSCNNConvolutionWeightsAndBiasesState](mpscnnconvolutionweightsandbiasesstate.md)
- [MPSCNNLossLabels](mpscnnlosslabels.md)
- [MPSCNNNormalizationGammaAndBetaState](mpscnnnormalizationgammaandbetastate.md)
- [MPSCNNNormalizationMeanAndVarianceState](mpscnnnormalizationmeanandvariancestate.md)
- [MPSNDArrayGradientState](mpsndarraygradientstate.md)
- [MPSNNBinaryGradientState](mpsnnbinarygradientstate.md)
- [MPSNNGradientState](mpsnngradientstate.md)
- [MPSNNMultiaryGradientState](mpsnnmultiarygradientstate.md)
- [MPSRNNMatrixTrainingState](mpsrnnmatrixtrainingstate.md)
- [MPSRNNRecurrentImageState](mpsrnnrecurrentimagestate.md)
- [MPSRNNRecurrentMatrixState](mpsrnnrecurrentmatrixstate.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func encode(to: any MTLCommandBuffer, sourceImages: [MPSImage]) -> MPSImage?](mpsnngraph/encode(to:sourceimages:).md)
- [func encode(to: any MTLCommandBuffer, sourceImages: [MPSImage], sourceStates: [MPSState]?, intermediateImages: NSMutableArray?, destinationStates: NSMutableArray?) -> MPSImage?](mpsnngraph/encode(to:sourceimages:sourcestates:intermediateimages:destinationstates:).md)
- [class MPSNNBinaryGradientState](mpsnnbinarygradientstate.md)
  A class representing the state of a gradient binary kernel when it was encoded.
- [class MPSNNGradientState](mpsnngradientstate.md)
  A class representing the state of a gradient kernel when it was encoded.
- [func executeAsync(withSourceImages: [MPSImage], completionHandler: MPSNNGraphCompletionHandler) -> MPSImage](mpsnngraph/executeasync(withsourceimages:completionhandler:).md)
- [typealias MPSNNGraphCompletionHandler](mpsnngraphcompletionhandler.md)
  A notification when an asynchronous graph execution has finished.
- [func encodeBatch(to: any MTLCommandBuffer, sourceImages: [[MPSImage]], sourceStates: [[MPSState]]?) -> [MPSImage]?](mpsnngraph/encodebatch(to:sourceimages:sourcestates:).md)
- [func encodeBatch(to: any MTLCommandBuffer, sourceImages: [[MPSImage]], sourceStates: [[MPSState]]?, intermediateImages: NSMutableArray?, destinationStates: NSMutableArray?) -> [MPSImage]?](mpsnngraph/encodebatch(to:sourceimages:sourcestates:intermediateimages:destinationstates:).md)
- [func readCountForSourceImage(at: Int) -> Int](mpsnngraph/readcountforsourceimage(at:).md)
- [func readCountForSourceState(at: Int) -> Int](mpsnngraph/readcountforsourcestate(at:).md)
- [func reloadFromDataSources()](mpsnngraph/reloadfromdatasources.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsstate)*