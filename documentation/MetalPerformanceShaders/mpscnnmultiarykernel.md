# MPSCNNMultiaryKernel

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNMultiaryKernel
```

```objc
@interface MPSCNNMultiaryKernel : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpscnnmultiarykernel/init%28coder,device%29.md)
- [init(device: any MTLDevice, sourceCount: Int)](./mpscnnmultiarykernel/init%28device,sourcecount%29.md)
### Instance Properties
- [var clipRect: MTLRegion](./mpscnnmultiarykernel/cliprect.md)
- [var destinationFeatureChannelOffset: Int](./mpscnnmultiarykernel/destinationfeaturechanneloffset.md)
- [var destinationImageAllocator: any MPSImageAllocator](./mpscnnmultiarykernel/destinationimageallocator.md)
- [var isBackwards: Bool](./mpscnnmultiarykernel/isbackwards.md)
- [var isStateModified: Bool](./mpscnnmultiarykernel/isstatemodified.md)
- [var padding: any MPSNNPadding](./mpscnnmultiarykernel/padding.md)
- [var sourceCount: Int](./mpscnnmultiarykernel/sourcecount.md)
### Instance Methods
- [func appendBatchBarrier() -> Bool](./mpscnnmultiarykernel/appendbatchbarrier%28%29.md)
- [func destinationImageDescriptor(sourceImages: [MPSImage], sourceStates: [MPSState]?) -> MPSImageDescriptor](./mpscnnmultiarykernel/destinationimagedescriptor%28sourceimages,sourcestates%29.md)
- [func dilationRateXatIndex(Int) -> Int](./mpscnnmultiarykernel/dilationratexatindex%28_%29.md)
- [func dilationRateYatIndex(Int) -> Int](./mpscnnmultiarykernel/dilationrateyatindex%28_%29.md)
- [func edgeMode(at: Int) -> MPSImageEdgeMode](./mpscnnmultiarykernel/edgemode%28at%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage]) -> MPSImage](./mpscnnmultiarykernel/encode%28commandbuffer,sourceimages%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationImage: MPSImage)](./mpscnnmultiarykernel/encode%28commandbuffer,sourceimages,destinationimage%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationState: AutoreleasingUnsafeMutablePointer<MPSState?>, destinationStateIsTemporary: Bool) -> MPSImage](./mpscnnmultiarykernel/encode%28commandbuffer,sourceimages,destinationstate,destinationstateistemporary%29.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [[MPSImage]]) -> [MPSImage]](./mpscnnmultiarykernel/encodebatch%28commandbuffer,sourceimages%29.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [[MPSImage]], destinationImages: [MPSImage])](./mpscnnmultiarykernel/encodebatch%28commandbuffer,sourceimages,destinationimages%29.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [[MPSImage]], destinationStates: AutoreleasingUnsafeMutablePointer<NSArray?>, destinationStateIsTemporary: Bool) -> [MPSImage]](./mpscnnmultiarykernel/encodebatch%28commandbuffer,sourceimages,destinationstates,destinationstateistemporary%29.md)
- [func isResultStateReusedAcrossBatch() -> Bool](./mpscnnmultiarykernel/isresultstatereusedacrossbatch%28%29.md)
- [func kernelHeight(at: Int) -> Int](./mpscnnmultiarykernel/kernelheight%28at%29.md)
- [func kernelWidth(at: Int) -> Int](./mpscnnmultiarykernel/kernelwidth%28at%29.md)
- [func offset(at: Int) -> MPSOffset](./mpscnnmultiarykernel/offset%28at%29.md)
- [func resultState(sourceImages: [MPSImage], sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?](./mpscnnmultiarykernel/resultstate%28sourceimages,sourcestates,destinationimage%29.md)
- [func resultStateBatch(sourceImages: [[MPSImage]], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSState]?](./mpscnnmultiarykernel/resultstatebatch%28sourceimages,sourcestates,destinationimage%29.md)
- [func setDilationRateX(Int, at: Int)](./mpscnnmultiarykernel/setdilationratex%28_,at%29.md)
- [func setDilationRateY(Int, at: Int)](./mpscnnmultiarykernel/setdilationratey%28_,at%29.md)
- [func setEdgeMode(MPSImageEdgeMode, at: Int)](./mpscnnmultiarykernel/setedgemode%28_,at%29.md)
- [func setKernelHeight(Int, at: Int)](./mpscnnmultiarykernel/setkernelheight%28_,at%29.md)
- [func setKernelWidth(Int, at: Int)](./mpscnnmultiarykernel/setkernelwidth%28_,at%29.md)
- [func setOffset(MPSOffset, at: Int)](./mpscnnmultiarykernel/setoffset%28_,at%29.md)
- [func setSourceFeatureChannelMaxCount(Int, at: Int)](./mpscnnmultiarykernel/setsourcefeaturechannelmaxcount%28_,at%29.md)
- [func setSourceFeatureChannelOffset(Int, at: Int)](./mpscnnmultiarykernel/setsourcefeaturechanneloffset%28_,at%29.md)
- [func setStrideInPixelsX(Int, at: Int)](./mpscnnmultiarykernel/setstrideinpixelsx%28_,at%29.md)
- [func setStrideInPixelsY(Int, at: Int)](./mpscnnmultiarykernel/setstrideinpixelsy%28_,at%29.md)
- [func sourceFeatureChannelMaxCount(at: Int) -> Int](./mpscnnmultiarykernel/sourcefeaturechannelmaxcount%28at%29.md)
- [func sourceFeatureChannelOffset(at: Int) -> Int](./mpscnnmultiarykernel/sourcefeaturechanneloffset%28at%29.md)
- [func stride(inPixelsXatIndex: Int) -> Int](./mpscnnmultiarykernel/stride%28inpixelsxatindex%29.md)
- [func stride(inPixelsYatIndex: Int) -> Int](./mpscnnmultiarykernel/stride%28inpixelsyatindex%29.md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?](./mpscnnmultiarykernel/temporaryresultstate%28commandbuffer,sourceimages,sourcestates,destinationimage%29.md)
- [func temporaryResultStateBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [[MPSImage]], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSState]?](./mpscnnmultiarykernel/temporaryresultstatebatch%28commandbuffer,sourceimages,sourcestates,destinationimage%29.md)

## Relationships

### Inherits From
- [MPSKernel](./mpskernel.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnmultiarykernel)*