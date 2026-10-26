# MPSIntersectionDistancePrimitiveIndex

**Framework**: Metal Performance Shaders  
**Kind**: struct  
**Role**: Structure

An intersection result that contains the distance from the ray origin to the intersection point, and the index of the intersected primitive.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct MPSIntersectionDistancePrimitiveIndex
```

```c
typedef struct { ... } MPSIntersectionDistancePrimitiveIndex;
```

## Topics

### Initializers
- [init()](./mpsintersectiondistanceprimitiveindex/init%28%29.md)
- [init(distance: Float, primitiveIndex: UInt32)](./mpsintersectiondistanceprimitiveindex/init%28distance,primitiveindex%29.md)
### Instance Properties
- [var distance: Float](./mpsintersectiondistanceprimitiveindex/distance.md)
- [var primitiveIndex: UInt32](./mpsintersectiondistanceprimitiveindex/primitiveindex.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Structures
- [struct MPSCustomKernelArgumentCount](./mpscustomkernelargumentcount.md)
  A structure that contains the number of destination, source, and broadcaset textures used by a custom kernel.
- [struct MPSCustomKernelInfo](./mpscustomkernelinfo.md)
- [struct MPSCustomKernelSourceInfo](./mpscustomkernelsourceinfo.md)
- [struct MPSDimensionSlice](./mpsdimensionslice.md)
- [struct MPSImageCoordinate](./mpsimagecoordinate.md)
- [struct MPSImageRegion](./mpsimageregion.md)
- [struct MPSIntegerDivisionParams](./mpsintegerdivisionparams.md)
  Parameters that define the parts of a division operation.
- [struct MPSIntersectionDistance](./mpsintersectiondistance.md)
  An intersection result that contains the distance from the ray origin to the intersection point.
- [struct MPSIntersectionDistancePrimitiveIndexBufferIndex](./mpsintersectiondistanceprimitiveindexbufferindex.md)
- [struct MPSIntersectionDistancePrimitiveIndexBufferIndexCoordinates](./mpsintersectiondistanceprimitiveindexbufferindexcoordinates.md)
- [struct MPSIntersectionDistancePrimitiveIndexBufferIndexInstanceIndex](./mpsintersectiondistanceprimitiveindexbufferindexinstanceindex.md)
- [struct MPSIntersectionDistancePrimitiveIndexBufferIndexInstanceIndexCoordinates](./mpsintersectiondistanceprimitiveindexbufferindexinstanceindexcoordinates.md)
- [struct MPSIntersectionDistancePrimitiveIndexCoordinates](./mpsintersectiondistanceprimitiveindexcoordinates.md)
  An intersection result that contains the origin-intersection distance, intersected primitive index, and intersection point coordinates.
- [struct MPSIntersectionDistancePrimitiveIndexInstanceIndex](./mpsintersectiondistanceprimitiveindexinstanceindex.md)
  An intersection result that contains the origin-intersection distance, and intersected primitive and instance indices.
- [struct MPSIntersectionDistancePrimitiveIndexInstanceIndexCoordinates](./mpsintersectiondistanceprimitiveindexinstanceindexcoordinates.md)
  An intersection result that contains the origin-intersection distance, intersected primitive and instance indices, and intersection point coordinates.
- [MPSAxisAlignedBoundingBox](./mpsaxisalignedboundingbox-c.struct.md)
  An axis-aligned bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsintersectiondistanceprimitiveindex)*