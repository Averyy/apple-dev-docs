# MPSCNNBinaryKernel

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A convolution neural network kernel.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNBinaryKernel
```

```objc
@interface MPSCNNBinaryKernel : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpscnnbinarykernel/init%28coder,device%29.md)
- [init(device: any MTLDevice)](./mpscnnbinarykernel/init%28device%29.md)
### Instance Properties
- [var clipRect: MTLRegion](./mpscnnbinarykernel/cliprect.md)
- [var destinationFeatureChannelOffset: Int](./mpscnnbinarykernel/destinationfeaturechanneloffset.md)
- [var destinationImageAllocator: any MPSImageAllocator](./mpscnnbinarykernel/destinationimageallocator.md)
- [var isBackwards: Bool](./mpscnnbinarykernel/isbackwards.md)
- [var padding: any MPSNNPadding](./mpscnnbinarykernel/padding.md)
- [var primaryEdgeMode: MPSImageEdgeMode](./mpscnnbinarykernel/primaryedgemode.md)
- [var primaryOffset: MPSOffset](./mpscnnbinarykernel/primaryoffset.md)
- [var primaryStrideInPixelsX: Int](./mpscnnbinarykernel/primarystrideinpixelsx.md)
- [var primaryStrideInPixelsY: Int](./mpscnnbinarykernel/primarystrideinpixelsy.md)
- [var secondaryEdgeMode: MPSImageEdgeMode](./mpscnnbinarykernel/secondaryedgemode.md)
- [var secondaryOffset: MPSOffset](./mpscnnbinarykernel/secondaryoffset.md)
- [var secondaryStrideInPixelsX: Int](./mpscnnbinarykernel/secondarystrideinpixelsx.md)
- [var secondaryStrideInPixelsY: Int](./mpscnnbinarykernel/secondarystrideinpixelsy.md)
- [var isStateModified: Bool](./mpscnnbinarykernel/isstatemodified.md)
- [var primaryDilationRateX: Int](./mpscnnbinarykernel/primarydilationratex.md)
- [var primaryDilationRateY: Int](./mpscnnbinarykernel/primarydilationratey.md)
- [var primaryKernelHeight: Int](./mpscnnbinarykernel/primarykernelheight.md)
- [var primaryKernelWidth: Int](./mpscnnbinarykernel/primarykernelwidth.md)
- [var primarySourceFeatureChannelMaxCount: Int](./mpscnnbinarykernel/primarysourcefeaturechannelmaxcount.md)
- [var primarySourceFeatureChannelOffset: Int](./mpscnnbinarykernel/primarysourcefeaturechanneloffset.md)
- [var secondaryDilationRateX: Int](./mpscnnbinarykernel/secondarydilationratex.md)
- [var secondaryDilationRateY: Int](./mpscnnbinarykernel/secondarydilationratey.md)
- [var secondaryKernelHeight: Int](./mpscnnbinarykernel/secondarykernelheight.md)
- [var secondaryKernelWidth: Int](./mpscnnbinarykernel/secondarykernelwidth.md)
- [var secondarySourceFeatureChannelMaxCount: Int](./mpscnnbinarykernel/secondarysourcefeaturechannelmaxcount.md)
- [var secondarySourceFeatureChannelOffset: Int](./mpscnnbinarykernel/secondarysourcefeaturechanneloffset.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage) -> MPSImage](./mpscnnbinarykernel/encode%28commandbuffer,primaryimage,secondaryimage%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, destinationImage: MPSImage)](./mpscnnbinarykernel/encode%28commandbuffer,primaryimage,secondaryimage,destinationimage%29.md)
- [func appendBatchBarrier() -> Bool](./mpscnnbinarykernel/appendbatchbarrier%28%29.md)
- [func batchEncodingStorageSize(primaryImage: [MPSImage], secondaryImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]?) -> Int](./mpscnnbinarykernel/batchencodingstoragesize%28primaryimage,secondaryimage,sourcestates,destinationimage%29.md)
- [func destinationImageDescriptor(forSourceImages: [MPSImage], sourceStates: [MPSState]?) -> MPSImageDescriptor](./mpscnnbinarykernel/destinationimagedescriptor%28forsourceimages,sourcestates%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, destinationState: AutoreleasingUnsafeMutablePointer<MPSState?>, destinationStateIsTemporary: Bool) -> MPSImage](./mpscnnbinarykernel/encode%28commandbuffer,primaryimage,secondaryimage,destinationstate,destinationstateistemporary%29.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, primaryImages: [MPSImage], secondaryImages: [MPSImage]) -> [MPSImage]](./mpscnnbinarykernel/encodebatch%28commandbuffer,primaryimages,secondaryimages%29.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, primaryImages: [MPSImage], secondaryImages: [MPSImage], destinationImages: [MPSImage])](./mpscnnbinarykernel/encodebatch%28commandbuffer,primaryimages,secondaryimages,destinationimages%29.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, primaryImages: [MPSImage], secondaryImages: [MPSImage], destinationStates: AutoreleasingUnsafeMutablePointer<NSArray?>, destinationStateIsTemporary: Bool) -> [MPSImage]](./mpscnnbinarykernel/encodebatch%28commandbuffer,primaryimages,secondaryimages,destinationstates,destinationstateistemporary%29.md)
- [func encodingStorageSize(primaryImage: MPSImage, secondaryImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage?) -> Int](./mpscnnbinarykernel/encodingstoragesize%28primaryimage,secondaryimage,sourcestates,destinationimage%29.md)
- [func isResultStateReusedAcrossBatch() -> Bool](./mpscnnbinarykernel/isresultstatereusedacrossbatch%28%29.md)
- [func resultState(primaryImage: MPSImage, secondaryImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?](./mpscnnbinarykernel/resultstate%28primaryimage,secondaryimage,sourcestates,destinationimage%29.md)
- [func resultStateBatch(primaryImage: [MPSImage], secondaryImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSState]?](./mpscnnbinarykernel/resultstatebatch%28primaryimage,secondaryimage,sourcestates,destinationimage%29.md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?](./mpscnnbinarykernel/temporaryresultstate%28commandbuffer,primaryimage,secondaryimage,sourcestates,destinationimage%29.md)
- [func temporaryResultStateBatch(commandBuffer: any MTLCommandBuffer, primaryImage: [MPSImage], secondaryImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSState]?](./mpscnnbinarykernel/temporaryresultstatebatch%28commandbuffer,primaryimage,secondaryimage,sourcestates,destinationimage%29.md)

## Relationships

### Inherits From
- [MPSKernel](./mpskernel.md)
### Inherited By
- [MPSCNNArithmetic](./mpscnnarithmetic.md)
- [MPSCNNGradientKernel](./mpscnngradientkernel.md)
- [MPSNNGridSample](./mpsnngridsample.md)
- [MPSNNLossGradient](./mpsnnlossgradient.md)
- [MPSNNReduceBinary](./mpsnnreducebinary.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Layer Base Classes
- [class MPSCNNKernel](./mpscnnkernel.md)
  Base class for neural network layers.
- [class MPSCNNGradientKernel](./mpscnngradientkernel.md)
  The base class for gradient layers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbinarykernel)*