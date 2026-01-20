# MPSCustomKernelInfo

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
struct MPSCustomKernelInfo
```

## Topics

### Initializers
- [init()](mpscustomkernelinfo/init.md)
- [init(clipOrigin: vector_ushort4, clipSize: vector_ushort4, destinationFeatureChannels: UInt16, destImageArraySize: UInt16, sourceImageCount: UInt16, threadgroupSize: UInt16, subbatchIndex: UInt16, subbatchStride: UInt16, idiv: MPSIntegerDivisionParams)](mpscustomkernelinfo/init(cliporigin:clipsize:destinationfeaturechannels:destimagearraysize:sourceimagecount:threadgroupsize:subbatchindex:subbatchstride:idiv:).md)
### Instance Properties
- [var clipOrigin: vector_ushort4](mpscustomkernelinfo/cliporigin.md)
- [var clipSize: vector_ushort4](mpscustomkernelinfo/clipsize.md)
- [var destImageArraySize: UInt16](mpscustomkernelinfo/destimagearraysize.md)
- [var destinationFeatureChannels: UInt16](mpscustomkernelinfo/destinationfeaturechannels.md)
- [var idiv: MPSIntegerDivisionParams](mpscustomkernelinfo/idiv.md)
- [var sourceImageCount: UInt16](mpscustomkernelinfo/sourceimagecount.md)
- [var subbatchIndex: UInt16](mpscustomkernelinfo/subbatchindex.md)
- [var subbatchStride: UInt16](mpscustomkernelinfo/subbatchstride.md)
- [var threadgroupSize: UInt16](mpscustomkernelinfo/threadgroupsize.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MPSCustomKernelArgumentCount](mpscustomkernelargumentcount.md)
  A structure that contains the number of destination, source, and broadcaset textures used by a custom kernel.
- [struct MPSCustomKernelSourceInfo](mpscustomkernelsourceinfo.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscustomkernelinfo)*