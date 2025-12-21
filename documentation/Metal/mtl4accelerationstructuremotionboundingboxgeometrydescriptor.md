# MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor

**Framework**: Metal  
**Kind**: class

Describes motion bounding box geometry, suitable for motion ray tracing.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor
```

#### Overview

You use bounding boxes to implement procedural geometry for ray tracing, such as spheres or any other shape you define by using intersection functions.

Use a [`MTLResidencySet`](mtlresidencyset.md) to mark residency of all buffers this descriptor references when you build this acceleration structure.

## Topics

### Instance Properties
- [var boundingBoxBuffers: MTL4BufferRange](mtl4accelerationstructuremotionboundingboxgeometrydescriptor/boundingboxbuffers.md)
  Configures a reference to a buffer where each entry contains a reference to a buffer of bounding boxes.
- [var boundingBoxCount: Int](mtl4accelerationstructuremotionboundingboxgeometrydescriptor/boundingboxcount.md)
  Declares the number of bounding boxes in each buffer that `boundingBoxBuffer` references.
- [var boundingBoxStride: Int](mtl4accelerationstructuremotionboundingboxgeometrydescriptor/boundingboxstride.md)
  Declares the stride, in bytes, between bounding boxes in the bounding box buffers each entry in `boundingBoxBuffer` references.

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
- [class MTL4AccelerationStructureMotionCurveGeometryDescriptor](mtl4accelerationstructuremotioncurvegeometrydescriptor.md)
  Describes motion curve geometry, suitable for motion ray tracing.
- [class MTLAccelerationStructureMotionCurveGeometryDescriptor](mtlaccelerationstructuremotioncurvegeometrydescriptor.md)
- [class MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor](mtlaccelerationstructuremotionboundingboxgeometrydescriptor.md)
  A description of a list of bounding boxes, as motion keyframe data, to turn into an acceleration structure.
- [class MTLMotionKeyframeData](mtlmotionkeyframedata.md)
  Geometry data for a specific keyframe to use in a moving instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotionboundingboxgeometrydescriptor)*