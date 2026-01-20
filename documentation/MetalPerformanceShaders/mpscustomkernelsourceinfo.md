# MPSCustomKernelSourceInfo

**Framework**: Metal Performance Shaders  
**Kind**: struct

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MPSCustomKernelSourceInfo
```

## Topics

### Initializers
- [init()](mpscustomkernelsourceinfo/init.md)
- [init(kernelOrigin: vector_short2, kernelPhase: vector_ushort2, kernelSize: vector_ushort2, offset: vector_short2, stride: vector_ushort2, dilationRate: vector_ushort2, featureChannelOffset: UInt16, featureChannels: UInt16, imageArrayOffset: UInt16, imageArraySize: UInt16)](mpscustomkernelsourceinfo/init(kernelorigin:kernelphase:kernelsize:offset:stride:dilationrate:featurechanneloffset:featurechannels:imagearrayoffset:imagearraysize:).md)
### Instance Properties
- [var dilationRate: vector_ushort2](mpscustomkernelsourceinfo/dilationrate.md)
- [var featureChannelOffset: UInt16](mpscustomkernelsourceinfo/featurechanneloffset.md)
- [var featureChannels: UInt16](mpscustomkernelsourceinfo/featurechannels.md)
- [var imageArrayOffset: UInt16](mpscustomkernelsourceinfo/imagearrayoffset.md)
- [var imageArraySize: UInt16](mpscustomkernelsourceinfo/imagearraysize.md)
- [var kernelOrigin: vector_short2](mpscustomkernelsourceinfo/kernelorigin.md)
- [var kernelPhase: vector_ushort2](mpscustomkernelsourceinfo/kernelphase.md)
- [var kernelSize: vector_ushort2](mpscustomkernelsourceinfo/kernelsize.md)
- [var offset: vector_short2](mpscustomkernelsourceinfo/offset.md)
- [var stride: vector_ushort2](mpscustomkernelsourceinfo/stride.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MPSCustomKernelArgumentCount](mpscustomkernelargumentcount.md)
  A structure that contains the number of destination, source, and broadcaset textures used by a custom kernel.
- [struct MPSCustomKernelInfo](mpscustomkernelinfo.md)
- [struct MPSDimensionSlice](mpsdimensionslice.md)
- [struct MPSImageCoordinate](mpsimagecoordinate.md)
- [struct MPSImageRegion](mpsimageregion.md)
- [struct MPSIntegerDivisionParams](mpsintegerdivisionparams.md)
  Parameters that define the parts of a division operation.
- [struct MPSIntersectionDistance](mpsintersectiondistance.md)
  An intersection result that contains the distance from the ray origin to the intersection point.
- [struct MPSIntersectionDistancePrimitiveIndex](mpsintersectiondistanceprimitiveindex.md)
  An intersection result that contains the distance from the ray origin to the intersection point, and the index of the intersected primitive.
- [struct MPSIntersectionDistancePrimitiveIndexBufferIndex](mpsintersectiondistanceprimitiveindexbufferindex.md)
- [struct MPSIntersectionDistancePrimitiveIndexBufferIndexCoordinates](mpsintersectiondistanceprimitiveindexbufferindexcoordinates.md)
- [struct MPSIntersectionDistancePrimitiveIndexBufferIndexInstanceIndex](mpsintersectiondistanceprimitiveindexbufferindexinstanceindex.md)
- [struct MPSIntersectionDistancePrimitiveIndexBufferIndexInstanceIndexCoordinates](mpsintersectiondistanceprimitiveindexbufferindexinstanceindexcoordinates.md)
- [struct MPSIntersectionDistancePrimitiveIndexCoordinates](mpsintersectiondistanceprimitiveindexcoordinates.md)
  An intersection result that contains the origin-intersection distance, intersected primitive index, and intersection point coordinates.
- [struct MPSIntersectionDistancePrimitiveIndexInstanceIndex](mpsintersectiondistanceprimitiveindexinstanceindex.md)
  An intersection result that contains the origin-intersection distance, and intersected primitive and instance indices.
- [struct MPSIntersectionDistancePrimitiveIndexInstanceIndexCoordinates](mpsintersectiondistanceprimitiveindexinstanceindexcoordinates.md)
  An intersection result that contains the origin-intersection distance, intersected primitive and instance indices, and intersection point coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscustomkernelsourceinfo)*