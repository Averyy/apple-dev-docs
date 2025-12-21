# MTL4AccelerationStructureMotionCurveGeometryDescriptor

**Framework**: Metal  
**Kind**: class

Describes motion curve geometry, suitable for motion ray tracing.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class MTL4AccelerationStructureMotionCurveGeometryDescriptor
```

#### Overview

Use a [`MTLResidencySet`](mtlresidencyset.md) to mark residency of all buffers this descriptor references when you build this acceleration structure.

## Topics

### Instance Properties
- [var controlPointBuffers: MTL4BufferRange](mtl4accelerationstructuremotioncurvegeometrydescriptor/controlpointbuffers.md)
  Assigns a reference to a buffer where each entry contains a reference to a buffer of control points.
- [var controlPointCount: Int](mtl4accelerationstructuremotioncurvegeometrydescriptor/controlpointcount.md)
  Specifies the number of control points in the buffers the control point buffers reference.
- [var controlPointFormat: MTLAttributeFormat](mtl4accelerationstructuremotioncurvegeometrydescriptor/controlpointformat.md)
  Declares the format of the control points in the buffers that the control point buffers reference.
- [var controlPointStride: Int](mtl4accelerationstructuremotioncurvegeometrydescriptor/controlpointstride.md)
  Sets the stride, in bytes, between control points in the control point buffer.
- [var curveBasis: MTLCurveBasis](mtl4accelerationstructuremotioncurvegeometrydescriptor/curvebasis.md)
  Sets the curve basis function, determining how Metal interpolates the control points.
- [var curveEndCaps: MTLCurveEndCaps](mtl4accelerationstructuremotioncurvegeometrydescriptor/curveendcaps.md)
  Configures the type of curve end caps.
- [var curveType: MTLCurveType](mtl4accelerationstructuremotioncurvegeometrydescriptor/curvetype.md)
  Controls the curve type.
- [var indexBuffer: MTL4BufferRange](mtl4accelerationstructuremotioncurvegeometrydescriptor/indexbuffer.md)
  Assigns an optional index buffer containing references to control points in the control point buffers.
- [var indexType: MTLIndexType](mtl4accelerationstructuremotioncurvegeometrydescriptor/indextype.md)
  Configures the size of the indices the `indexBuffer` contains, which is typically either 16 or 32-bits for each index.
- [var radiusBuffers: MTL4BufferRange](mtl4accelerationstructuremotioncurvegeometrydescriptor/radiusbuffers.md)
  Assigns a reference to a buffer containing, in turn, references to curve radii buffers.
- [var radiusFormat: MTLAttributeFormat](mtl4accelerationstructuremotioncurvegeometrydescriptor/radiusformat.md)
  Sets the format of the radii in the radius buffer.
- [var radiusStride: Int](mtl4accelerationstructuremotioncurvegeometrydescriptor/radiusstride.md)
  Sets the stride, in bytes, between radii in the radius buffer.
- [var segmentControlPointCount: Int](mtl4accelerationstructuremotioncurvegeometrydescriptor/segmentcontrolpointcount.md)
  Controls the number of control points per curve segment.
- [var segmentCount: Int](mtl4accelerationstructuremotioncurvegeometrydescriptor/segmentcount.md)
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

- [class MTL4AccelerationStructureMotionTriangleGeometryDescriptor](mtl4accelerationstructuremotiontrianglegeometrydescriptor.md)
  Describes motion triangle geometry, suitable for motion ray tracing.
- [class MTLAccelerationStructureMotionTriangleGeometryDescriptor](mtlaccelerationstructuremotiontrianglegeometrydescriptor.md)
  A description of a list of triangle primitives, as motion keyframe data, to turn into an acceleration structure.
- [class MTLAccelerationStructureMotionCurveGeometryDescriptor](mtlaccelerationstructuremotioncurvegeometrydescriptor.md)
- [class MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor](mtl4accelerationstructuremotionboundingboxgeometrydescriptor.md)
  Describes motion bounding box geometry, suitable for motion ray tracing.
- [class MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor](mtlaccelerationstructuremotionboundingboxgeometrydescriptor.md)
  A description of a list of bounding boxes, as motion keyframe data, to turn into an acceleration structure.
- [class MTLMotionKeyframeData](mtlmotionkeyframedata.md)
  Geometry data for a specific keyframe to use in a moving instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor)*