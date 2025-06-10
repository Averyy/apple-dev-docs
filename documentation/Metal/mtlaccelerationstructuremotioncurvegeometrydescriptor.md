# MTLAccelerationStructureMotionCurveGeometryDescriptor

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
class MTLAccelerationStructureMotionCurveGeometryDescriptor
```

## Mentions

- [Improving Ray-Tracing Data Access Using Per-Primitive Data](improving-ray-tracing-data-access-using-per-primitive-data.md)

## Topics

### Instance Properties
- [var controlPointBuffers: [MTLMotionKeyframeData]](mtlaccelerationstructuremotioncurvegeometrydescriptor/controlpointbuffers.md)
- [var controlPointCount: Int](mtlaccelerationstructuremotioncurvegeometrydescriptor/controlpointcount.md)
- [var controlPointFormat: MTLAttributeFormat](mtlaccelerationstructuremotioncurvegeometrydescriptor/controlpointformat.md)
- [var controlPointStride: Int](mtlaccelerationstructuremotioncurvegeometrydescriptor/controlpointstride.md)
- [var curveBasis: MTLCurveBasis](mtlaccelerationstructuremotioncurvegeometrydescriptor/curvebasis.md)
- [var curveEndCaps: MTLCurveEndCaps](mtlaccelerationstructuremotioncurvegeometrydescriptor/curveendcaps.md)
- [var curveType: MTLCurveType](mtlaccelerationstructuremotioncurvegeometrydescriptor/curvetype.md)
- [var indexBuffer: (any MTLBuffer)?](mtlaccelerationstructuremotioncurvegeometrydescriptor/indexbuffer.md)
- [var indexBufferOffset: Int](mtlaccelerationstructuremotioncurvegeometrydescriptor/indexbufferoffset.md)
- [var indexType: MTLIndexType](mtlaccelerationstructuremotioncurvegeometrydescriptor/indextype.md)
- [var radiusBuffers: [MTLMotionKeyframeData]](mtlaccelerationstructuremotioncurvegeometrydescriptor/radiusbuffers.md)
- [var radiusFormat: MTLAttributeFormat](mtlaccelerationstructuremotioncurvegeometrydescriptor/radiusformat.md)
- [var radiusStride: Int](mtlaccelerationstructuremotioncurvegeometrydescriptor/radiusstride.md)
- [var segmentControlPointCount: Int](mtlaccelerationstructuremotioncurvegeometrydescriptor/segmentcontrolpointcount.md)
- [var segmentCount: Int](mtlaccelerationstructuremotioncurvegeometrydescriptor/segmentcount.md)

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

- [class MTL4AccelerationStructureMotionTriangleGeometryDescriptor](mtl4accelerationstructuremotiontrianglegeometrydescriptor.md)
  Describes motion triangle geometry, suitable for motion ray tracing.
- [class MTLAccelerationStructureMotionTriangleGeometryDescriptor](mtlaccelerationstructuremotiontrianglegeometrydescriptor.md)
  A description of a list of triangle primitives, as motion keyframe data, to turn into an acceleration structure.
- [class MTL4AccelerationStructureMotionCurveGeometryDescriptor](mtl4accelerationstructuremotioncurvegeometrydescriptor.md)
  Describes motion curve geometry, suitable for motion ray tracing.
- [class MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor](mtl4accelerationstructuremotionboundingboxgeometrydescriptor.md)
  Describes motion bounding box geometry, suitable for motion ray tracing.
- [class MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor](mtlaccelerationstructuremotionboundingboxgeometrydescriptor.md)
  A description of a list of bounding boxes, as motion keyframe data, to turn into an acceleration structure.
- [class MTLMotionKeyframeData](mtlmotionkeyframedata.md)
  Geometry data for a specific keyframe to use in a moving object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotioncurvegeometrydescriptor)*