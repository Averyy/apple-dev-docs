# MTLAccelerationStructureBoundingBoxGeometryDescriptor

**Framework**: Metal  
**Kind**: class

A description of a list of bounding boxes to turn into an acceleration structure.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class MTLAccelerationStructureBoundingBoxGeometryDescriptor
```

## Mentions

- [Improving ray-tracing data access using per-primitive data](improving-ray-tracing-data-access-using-per-primitive-data.md)

## Topics

### Specifying the number of bounding boxes
- [var boundingBoxCount: Int](mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxcount.md)
  The number of bounding boxes in the bounding box buffer.
### Specifying bounding boxes data
- [var boundingBoxBuffer: (any MTLBuffer)?](mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxbuffer.md)
  A buffer that contains an array of bounding box structures.
- [var boundingBoxBufferOffset: Int](mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxbufferoffset.md)
  The offset, in bytes, to the first bounding box in the buffer.
- [var boundingBoxStride: Int](mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxstride.md)
  The stride, in bytes, between bounding boxes in the buffer.

## Relationships

### Inherits From
- [MTLAccelerationStructureGeometryDescriptor](mtlaccelerationstructuregeometrydescriptor.md)
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
- [class MTL4AccelerationStructureBoundingBoxGeometryDescriptor](mtl4accelerationstructureboundingboxgeometrydescriptor.md)
  Describes bounding-box geometry suitable for ray tracing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureboundingboxgeometrydescriptor)*