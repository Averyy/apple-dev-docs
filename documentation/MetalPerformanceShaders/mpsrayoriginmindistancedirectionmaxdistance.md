# MPSRayOriginMinDistanceDirectionMaxDistance

**Framework**: Metal Performance Shaders  
**Kind**: struct

A 3D ray with an origin, a direction, and an intersection distance range from the origin.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MPSRayOriginMinDistanceDirectionMaxDistance
```

## Topics

### Initializers
- [init()](mpsrayoriginmindistancedirectionmaxdistance/init.md)
- [init(origin: MPSPackedFloat3, minDistance: Float, direction: MPSPackedFloat3, maxDistance: Float)](mpsrayoriginmindistancedirectionmaxdistance/init(origin:mindistance:direction:maxdistance:).md)
### Instance Properties
- [var direction: MPSPackedFloat3](mpsrayoriginmindistancedirectionmaxdistance/direction.md)
- [var maxDistance: Float](mpsrayoriginmindistancedirectionmaxdistance/maxdistance.md)
- [var minDistance: Float](mpsrayoriginmindistancedirectionmaxdistance/mindistance.md)
- [var origin: MPSPackedFloat3](mpsrayoriginmindistancedirectionmaxdistance/origin.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MPSCustomKernelArgumentCount](mpscustomkernelargumentcount.md)
  A structure that contains the number of destination, source, and broadcaset textures used by a custom kernel.
- [struct MPSCustomKernelInfo](mpscustomkernelinfo.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrayoriginmindistancedirectionmaxdistance)*