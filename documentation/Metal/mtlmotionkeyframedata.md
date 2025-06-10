# MTLMotionKeyframeData

**Framework**: Metal  
**Kind**: class

Geometry data for a specific keyframe to use in a moving object.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class MTLMotionKeyframeData
```

#### Overview

A [`MTLMotionKeyframeData`](mtlmotionkeyframedata.md) object describes the location of geometry data for a keyframe. The exact type of data can vary, depending on which kind of motion descriptor you create. For a [`MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor`](mtlaccelerationstructuremotionboundingboxgeometrydescriptor.md) object, the buffer data is a list of bounding boxes. For a [`MTLAccelerationStructureMotionTriangleGeometryDescriptor`](mtlaccelerationstructuremotiontrianglegeometrydescriptor.md), the buffer data is a list of vertices.

## Topics

### Specifying the Keyframe Data
- [var buffer: (any MTLBuffer)?](mtlmotionkeyframedata/buffer.md)
  The buffer that holds the geometry data.
- [var offset: Int](mtlmotionkeyframedata/offset.md)
  The offset, in bytes, to the keyframe data.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
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
- [class MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor](mtlaccelerationstructuremotionboundingboxgeometrydescriptor.md)
  A description of a list of bounding boxes, as motion keyframe data, to turn into an acceleration structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlmotionkeyframedata)*