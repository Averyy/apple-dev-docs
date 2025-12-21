# MTL4AccelerationStructureCurveGeometryDescriptor

**Framework**: Metal  
**Kind**: class

Describes curve geometry suitable for ray tracing.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class MTL4AccelerationStructureCurveGeometryDescriptor
```

#### Overview

Use a [`MTLResidencySet`](mtlresidencyset.md) to mark residency of all buffers this descriptor references when you build this acceleration structure.

## Topics

### Instance Properties
- [var controlPointBuffer: MTL4BufferRange](mtl4accelerationstructurecurvegeometrydescriptor/controlpointbuffer.md)
  References a buffer containing curve control points.
- [var controlPointCount: Int](mtl4accelerationstructurecurvegeometrydescriptor/controlpointcount.md)
  Declares the number of control points in the control point buffer.
- [var controlPointFormat: MTLAttributeFormat](mtl4accelerationstructurecurvegeometrydescriptor/controlpointformat.md)
  Declares the format of the control points the control point buffer references.
- [var controlPointStride: Int](mtl4accelerationstructurecurvegeometrydescriptor/controlpointstride.md)
  Sets the stride, in bytes, between control points in the control point buffer the control point buffer references.
- [var curveBasis: MTLCurveBasis](mtl4accelerationstructurecurvegeometrydescriptor/curvebasis.md)
  Controls the curve basis function, determining how Metal interpolates the control points.
- [var curveEndCaps: MTLCurveEndCaps](mtl4accelerationstructurecurvegeometrydescriptor/curveendcaps.md)
  Sets the type of curve end caps.
- [var curveType: MTLCurveType](mtl4accelerationstructurecurvegeometrydescriptor/curvetype.md)
  Controls the curve type.
- [var indexBuffer: MTL4BufferRange](mtl4accelerationstructurecurvegeometrydescriptor/indexbuffer.md)
  Assigns an optional index buffer containing references to control points in the control point buffer.
- [var indexType: MTLIndexType](mtl4accelerationstructurecurvegeometrydescriptor/indextype.md)
  Specifies the size of the indices the `indexBuffer` contains, which is typically either 16 or 32-bits for each index.
- [var radiusBuffer: MTL4BufferRange](mtl4accelerationstructurecurvegeometrydescriptor/radiusbuffer.md)
  Assigns a reference to a buffer containing the curve radius for each control point.
- [var radiusFormat: MTLAttributeFormat](mtl4accelerationstructurecurvegeometrydescriptor/radiusformat.md)
  Declares the format of the radii in the radius buffer.
- [var radiusStride: Int](mtl4accelerationstructurecurvegeometrydescriptor/radiusstride.md)
  Configures the stride, in bytes, between radii in the radius buffer.
- [var segmentControlPointCount: Int](mtl4accelerationstructurecurvegeometrydescriptor/segmentcontrolpointcount.md)
  Declares the number of control points per curve segment.
- [var segmentCount: Int](mtl4accelerationstructurecurvegeometrydescriptor/segmentcount.md)
  Declares the number of curve segments.

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
- [class MTLAccelerationStructureCurveGeometryDescriptor](mtlaccelerationstructurecurvegeometrydescriptor.md)
  A descriptor you configure with curve geometry for building acceleration structures.
- [enum MTLCurveType](mtlcurvetype.md)
- [enum MTLCurveBasis](mtlcurvebasis.md)
- [enum MTLCurveEndCaps](mtlcurveendcaps.md)
- [class MTL4AccelerationStructureBoundingBoxGeometryDescriptor](mtl4accelerationstructureboundingboxgeometrydescriptor.md)
  Describes bounding-box geometry suitable for ray tracing.
- [class MTLAccelerationStructureBoundingBoxGeometryDescriptor](mtlaccelerationstructureboundingboxgeometrydescriptor.md)
  A description of a list of bounding boxes to turn into an acceleration structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructurecurvegeometrydescriptor)*