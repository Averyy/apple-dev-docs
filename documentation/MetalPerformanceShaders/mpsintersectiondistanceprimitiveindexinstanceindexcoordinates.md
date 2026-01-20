# MPSIntersectionDistancePrimitiveIndexInstanceIndexCoordinates

**Framework**: Metal Performance Shaders  
**Kind**: struct

An intersection result that contains the origin-intersection distance, intersected primitive and instance indices, and intersection point coordinates.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MPSIntersectionDistancePrimitiveIndexInstanceIndexCoordinates
```

## Topics

### Initializers
- [init()](mpsintersectiondistanceprimitiveindexinstanceindexcoordinates/init.md)
- [init(distance: Float, primitiveIndex: UInt32, instanceIndex: UInt32, coordinates: vector_float2)](mpsintersectiondistanceprimitiveindexinstanceindexcoordinates/init(distance:primitiveindex:instanceindex:coordinates:).md)
### Instance Properties
- [var coordinates: vector_float2](mpsintersectiondistanceprimitiveindexinstanceindexcoordinates/coordinates.md)
- [var distance: Float](mpsintersectiondistanceprimitiveindexinstanceindexcoordinates/distance.md)
- [var instanceIndex: UInt32](mpsintersectiondistanceprimitiveindexinstanceindexcoordinates/instanceindex.md)
- [var primitiveIndex: UInt32](mpsintersectiondistanceprimitiveindexinstanceindexcoordinates/primitiveindex.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsintersectiondistanceprimitiveindexinstanceindexcoordinates)*