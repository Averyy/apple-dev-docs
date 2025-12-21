# MTL4AccelerationStructureBoundingBoxGeometryDescriptor

**Framework**: Metal  
**Kind**: class

Describes bounding-box geometry suitable for ray tracing.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class MTL4AccelerationStructureBoundingBoxGeometryDescriptor
```

#### Overview

You use bounding boxes to implement procedural geometry for ray tracing, such as spheres or any other shape you define by using intersection functions.

Use a [`MTLResidencySet`](mtlresidencyset.md) to mark residency of all buffers this descriptor references when you build this acceleration structure.

## Topics

### Instance Properties
- [var boundingBoxBuffer: MTL4BufferRange](mtl4accelerationstructureboundingboxgeometrydescriptor/boundingboxbuffer.md)
  References a buffer containing bounding box data in `MTLAxisAlignedBoundingBoxes` format.
- [var boundingBoxCount: Int](mtl4accelerationstructureboundingboxgeometrydescriptor/boundingboxcount.md)
  Describes the number of bounding boxes the `boundingBoxBuffer` contains.
- [var boundingBoxStride: Int](mtl4accelerationstructureboundingboxgeometrydescriptor/boundingboxstride.md)
  Assigns the stride, in bytes, between bounding boxes in the bounding box buffer `boundingBoxBuffer` references.

## Relationships

### Inherits From
- [MTL4AccelerationStructureGeometryDescriptor](mtl4accelerationstructuregeometrydescriptor.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MTL4AccelerationStructureGeometryDescriptor](mtl4accelerationstructuregeometrydescriptor.md)
  Base class for all Metal 4 acceleration structure geometry descriptors.
- [class MTLAccelerationStructureGeometryDescriptor](mtlaccelerationstructuregeometrydescriptor.md)
  A base class for descriptors that contain geometry data to convert into a ray-tracing acceleration structure.
- [class MTL4AccelerationStructureTriangleGeometryDescriptor](mtl4accelerationstructuretrianglegeometrydescriptor.md)
  Describes triangle geometry suitable for ray tracing.
- [class MTLAccelerationStructureTriangleGeometryDescriptor](mtlaccelerationstructuretrianglegeometrydescriptor.md)
  A description of a list of triangle primitives to turn into an acceleration structure.
- [class MTL4AccelerationStructureCurveGeometryDescriptor](mtl4accelerationstructurecurvegeometrydescriptor.md)
  Describes curve geometry suitable for ray tracing.
- [class MTLAccelerationStructureCurveGeometryDescriptor](mtlaccelerationstructurecurvegeometrydescriptor.md)
  A descriptor you configure with curve geometry for building acceleration structures.
- [enum MTLCurveType](mtlcurvetype.md)
- [enum MTLCurveBasis](mtlcurvebasis.md)
- [enum MTLCurveEndCaps](mtlcurveendcaps.md)
- [class MTLAccelerationStructureBoundingBoxGeometryDescriptor](mtlaccelerationstructureboundingboxgeometrydescriptor.md)
  A description of a list of bounding boxes to turn into an acceleration structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructureboundingboxgeometrydescriptor)*