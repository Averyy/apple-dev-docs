# MPSCNNMultiaryKernel

**Framework**: Metal Performance Shaders  
**Kind**: class

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

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnmultiarykernel/init(coder:device:).md)
- [init(device: any MTLDevice, sourceCount: Int)](mpscnnmultiarykernel/init(device:sourcecount:).md)
### Instance Properties
- [var clipRect: MTLRegion](mpscnnmultiarykernel/cliprect.md)
- [var destinationFeatureChannelOffset: Int](mpscnnmultiarykernel/destinationfeaturechanneloffset.md)
- [var destinationImageAllocator: any MPSImageAllocator](mpscnnmultiarykernel/destinationimageallocator.md)
- [var isBackwards: Bool](mpscnnmultiarykernel/isbackwards.md)
- [var isStateModified: Bool](mpscnnmultiarykernel/isstatemodified.md)
- [var padding: any MPSNNPadding](mpscnnmultiarykernel/padding.md)
- [var sourceCount: Int](mpscnnmultiarykernel/sourcecount.md)
### Instance Methods
- [func appendBatchBarrier() -> Bool](mpscnnmultiarykernel/appendbatchbarrier.md)
- [func destinationImageDescriptor(sourceImages: [MPSImage], sourceStates: [MPSState]?) -> MPSImageDescriptor](mpscnnmultiarykernel/destinationimagedescriptor(sourceimages:sourcestates:).md)
- [func dilationRateXatIndex(Int) -> Int](mpscnnmultiarykernel/dilationratexatindex(_:).md)
- [func dilationRateYatIndex(Int) -> Int](mpscnnmultiarykernel/dilationrateyatindex(_:).md)
- [func edgeMode(at: Int) -> MPSImageEdgeMode](mpscnnmultiarykernel/edgemode(at:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage]) -> MPSImage](mpscnnmultiarykernel/encode(commandbuffer:sourceimages:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationImage: MPSImage)](mpscnnmultiarykernel/encode(commandbuffer:sourceimages:destinationimage:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationState: AutoreleasingUnsafeMutablePointer<MPSState?>, destinationStateIsTemporary: Bool) -> MPSImage](mpscnnmultiarykernel/encode(commandbuffer:sourceimages:destinationstate:destinationstateistemporary:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [[MPSImage]]) -> [MPSImage]](mpscnnmultiarykernel/encodebatch(commandbuffer:sourceimages:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [[MPSImage]], destinationImages: [MPSImage])](mpscnnmultiarykernel/encodebatch(commandbuffer:sourceimages:destinationimages:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [[MPSImage]], destinationStates: AutoreleasingUnsafeMutablePointer<NSArray?>, destinationStateIsTemporary: Bool) -> [MPSImage]](mpscnnmultiarykernel/encodebatch(commandbuffer:sourceimages:destinationstates:destinationstateistemporary:).md)
- [func isResultStateReusedAcrossBatch() -> Bool](mpscnnmultiarykernel/isresultstatereusedacrossbatch.md)
- [func kernelHeight(at: Int) -> Int](mpscnnmultiarykernel/kernelheight(at:).md)
- [func kernelWidth(at: Int) -> Int](mpscnnmultiarykernel/kernelwidth(at:).md)
- [func offset(at: Int) -> MPSOffset](mpscnnmultiarykernel/offset(at:).md)
- [func resultState(sourceImages: [MPSImage], sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?](mpscnnmultiarykernel/resultstate(sourceimages:sourcestates:destinationimage:).md)
- [func resultStateBatch(sourceImages: [[MPSImage]], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSState]?](mpscnnmultiarykernel/resultstatebatch(sourceimages:sourcestates:destinationimage:).md)
- [func setDilationRateX(Int, at: Int)](mpscnnmultiarykernel/setdilationratex(_:at:).md)
- [func setDilationRateY(Int, at: Int)](mpscnnmultiarykernel/setdilationratey(_:at:).md)
- [func setEdgeMode(MPSImageEdgeMode, at: Int)](mpscnnmultiarykernel/setedgemode(_:at:).md)
- [func setKernelHeight(Int, at: Int)](mpscnnmultiarykernel/setkernelheight(_:at:).md)
- [func setKernelWidth(Int, at: Int)](mpscnnmultiarykernel/setkernelwidth(_:at:).md)
- [func setOffset(MPSOffset, at: Int)](mpscnnmultiarykernel/setoffset(_:at:).md)
- [func setSourceFeatureChannelMaxCount(Int, at: Int)](mpscnnmultiarykernel/setsourcefeaturechannelmaxcount(_:at:).md)
- [func setSourceFeatureChannelOffset(Int, at: Int)](mpscnnmultiarykernel/setsourcefeaturechanneloffset(_:at:).md)
- [func setStrideInPixelsX(Int, at: Int)](mpscnnmultiarykernel/setstrideinpixelsx(_:at:).md)
- [func setStrideInPixelsY(Int, at: Int)](mpscnnmultiarykernel/setstrideinpixelsy(_:at:).md)
- [func sourceFeatureChannelMaxCount(at: Int) -> Int](mpscnnmultiarykernel/sourcefeaturechannelmaxcount(at:).md)
- [func sourceFeatureChannelOffset(at: Int) -> Int](mpscnnmultiarykernel/sourcefeaturechanneloffset(at:).md)
- [func stride(inPixelsXatIndex: Int) -> Int](mpscnnmultiarykernel/stride(inpixelsxatindex:).md)
- [func stride(inPixelsYatIndex: Int) -> Int](mpscnnmultiarykernel/stride(inpixelsyatindex:).md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?](mpscnnmultiarykernel/temporaryresultstate(commandbuffer:sourceimages:sourcestates:destinationimage:).md)
- [func temporaryResultStateBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [[MPSImage]], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSState]?](mpscnnmultiarykernel/temporaryresultstatebatch(commandbuffer:sourceimages:sourcestates:destinationimage:).md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnmultiarykernel)*