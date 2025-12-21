# MTLAccelerationStructureCurveGeometryDescriptor

**Framework**: Metal  
**Kind**: class

A descriptor you configure with curve geometry for building acceleration structures.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class MTLAccelerationStructureCurveGeometryDescriptor
```

## Mentions

- [Improving ray-tracing data access using per-primitive data](improving-ray-tracing-data-access-using-per-primitive-data.md)

## Topics

### Instance Properties
- [var controlPointBuffer: (any MTLBuffer)?](mtlaccelerationstructurecurvegeometrydescriptor/controlpointbuffer.md)
  A buffer that contains curve control points.
- [var controlPointBufferOffset: Int](mtlaccelerationstructurecurvegeometrydescriptor/controlpointbufferoffset.md)
  The offset, in bytes, to the control point data in the buffer.
- [var controlPointCount: Int](mtlaccelerationstructurecurvegeometrydescriptor/controlpointcount.md)
  The number of control points in the control point buffer.
- [var controlPointFormat: MTLAttributeFormat](mtlaccelerationstructurecurvegeometrydescriptor/controlpointformat.md)
  The format of the control points in the buffer.
- [var controlPointStride: Int](mtlaccelerationstructurecurvegeometrydescriptor/controlpointstride.md)
  The stride, in bytes, between control points in the buffer.
- [var curveBasis: MTLCurveBasis](mtlaccelerationstructurecurvegeometrydescriptor/curvebasis.md)
  The basis function for the curve geometry.
- [var curveEndCaps: MTLCurveEndCaps](mtlaccelerationstructurecurvegeometrydescriptor/curveendcaps.md)
  An end-cap type for the curves in the geometry.
- [var curveType: MTLCurveType](mtlaccelerationstructurecurvegeometrydescriptor/curvetype.md)
  A curve type for curves in the geometry.
- [var indexBuffer: (any MTLBuffer)?](mtlaccelerationstructurecurvegeometrydescriptor/indexbuffer.md)
  A buffer that contains references to control points in the control point buffer.
- [var indexBufferOffset: Int](mtlaccelerationstructurecurvegeometrydescriptor/indexbufferoffset.md)
  The offset, in bytes, to the index data in the buffer.
- [var indexType: MTLIndexType](mtlaccelerationstructurecurvegeometrydescriptor/indextype.md)
  The size of each index in the index buffer.
- [var radiusBuffer: (any MTLBuffer)?](mtlaccelerationstructurecurvegeometrydescriptor/radiusbuffer.md)
  A buffer that contains the curve radius for each control point.
- [var radiusBufferOffset: Int](mtlaccelerationstructurecurvegeometrydescriptor/radiusbufferoffset.md)
  The offset, in bytes, to the radius data in the buffer.
- [var radiusFormat: MTLAttributeFormat](mtlaccelerationstructurecurvegeometrydescriptor/radiusformat.md)
  The format of each radius in the radius buffer.
- [var radiusStride: Int](mtlaccelerationstructurecurvegeometrydescriptor/radiusstride.md)
  The stride, in bytes, between the radius elements in the radius buffer.
- [var segmentControlPointCount: Int](mtlaccelerationstructurecurvegeometrydescriptor/segmentcontrolpointcount.md)
  The number of control points in each curve segment.
- [var segmentCount: Int](mtlaccelerationstructurecurvegeometrydescriptor/segmentcount.md)
  The number of curve segments in each curve of the geometry.

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
- [enum MTLCurveType](mtlcurvetype.md)
- [enum MTLCurveBasis](mtlcurvebasis.md)
- [enum MTLCurveEndCaps](mtlcurveendcaps.md)
- [class MTL4AccelerationStructureBoundingBoxGeometryDescriptor](mtl4accelerationstructureboundingboxgeometrydescriptor.md)
  Describes bounding-box geometry suitable for ray tracing.
- [class MTLAccelerationStructureBoundingBoxGeometryDescriptor](mtlaccelerationstructureboundingboxgeometrydescriptor.md)
  A description of a list of bounding boxes to turn into an acceleration structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor)*