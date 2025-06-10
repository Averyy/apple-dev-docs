# MTLAccelerationStructureCurveGeometryDescriptor

**Framework**: Metal  
**Kind**: class

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

- [Improving Ray-Tracing Data Access Using Per-Primitive Data](improving-ray-tracing-data-access-using-per-primitive-data.md)

## Topics

### Instance Properties
- [var controlPointBuffer: (any MTLBuffer)?](mtlaccelerationstructurecurvegeometrydescriptor/controlpointbuffer.md)
- [var controlPointBufferOffset: Int](mtlaccelerationstructurecurvegeometrydescriptor/controlpointbufferoffset.md)
- [var controlPointCount: Int](mtlaccelerationstructurecurvegeometrydescriptor/controlpointcount.md)
- [var controlPointFormat: MTLAttributeFormat](mtlaccelerationstructurecurvegeometrydescriptor/controlpointformat.md)
- [var controlPointStride: Int](mtlaccelerationstructurecurvegeometrydescriptor/controlpointstride.md)
- [var curveBasis: MTLCurveBasis](mtlaccelerationstructurecurvegeometrydescriptor/curvebasis.md)
- [var curveEndCaps: MTLCurveEndCaps](mtlaccelerationstructurecurvegeometrydescriptor/curveendcaps.md)
- [var curveType: MTLCurveType](mtlaccelerationstructurecurvegeometrydescriptor/curvetype.md)
- [var indexBuffer: (any MTLBuffer)?](mtlaccelerationstructurecurvegeometrydescriptor/indexbuffer.md)
- [var indexBufferOffset: Int](mtlaccelerationstructurecurvegeometrydescriptor/indexbufferoffset.md)
- [var indexType: MTLIndexType](mtlaccelerationstructurecurvegeometrydescriptor/indextype.md)
- [var radiusBuffer: (any MTLBuffer)?](mtlaccelerationstructurecurvegeometrydescriptor/radiusbuffer.md)
- [var radiusBufferOffset: Int](mtlaccelerationstructurecurvegeometrydescriptor/radiusbufferoffset.md)
- [var radiusFormat: MTLAttributeFormat](mtlaccelerationstructurecurvegeometrydescriptor/radiusformat.md)
- [var radiusStride: Int](mtlaccelerationstructurecurvegeometrydescriptor/radiusstride.md)
- [var segmentControlPointCount: Int](mtlaccelerationstructurecurvegeometrydescriptor/segmentcontrolpointcount.md)
- [var segmentCount: Int](mtlaccelerationstructurecurvegeometrydescriptor/segmentcount.md)

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