# MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor

**Framework**: Metal  
**Kind**: class

A description of a list of bounding boxes, as motion keyframe data, to turn into an acceleration structure.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor
```

## Mentions

- [Improving ray-tracing data access using per-primitive data](improving-ray-tracing-data-access-using-per-primitive-data.md)

## Topics

### Specifying the number of bounding boxes
- [var boundingBoxCount: Int](mtlaccelerationstructuremotionboundingboxgeometrydescriptor/boundingboxcount.md)
  The number of bounding boxes in each bounding box buffer.
### Specifying bounding boxes data
- [var boundingBoxBuffers: [MTLMotionKeyframeData]](mtlaccelerationstructuremotionboundingboxgeometrydescriptor/boundingboxbuffers.md)
  A array of motion keyframes, each containing bounding box data.
- [var boundingBoxStride: Int](mtlaccelerationstructuremotionboundingboxgeometrydescriptor/boundingboxstride.md)
  The stride, in bytes, between bounding boxes in each buffer.

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
- [class MTLAccelerationStructureMotionCurveGeometryDescriptor](mtlaccelerationstructuremotioncurvegeometrydescriptor.md)
- [class MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor](mtl4accelerationstructuremotionboundingboxgeometrydescriptor.md)
  Describes motion bounding box geometry, suitable for motion ray tracing.
- [class MTLMotionKeyframeData](mtlmotionkeyframedata.md)
  Geometry data for a specific keyframe to use in a moving instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotionboundingboxgeometrydescriptor)*