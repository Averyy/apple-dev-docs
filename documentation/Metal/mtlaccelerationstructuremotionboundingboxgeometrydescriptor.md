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

- [Improving Ray-Tracing Data Access Using Per-Primitive Data](improving-ray-tracing-data-access-using-per-primitive-data.md)

## Topics

### Specifying the Number of Bounding Boxes
- [var boundingBoxCount: Int](mtlaccelerationstructuremotionboundingboxgeometrydescriptor/boundingboxcount.md)
  The number of bounding boxes in each bounding box buffer.
### Specifying Bounding Boxes Data
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

- [class MTLAccelerationStructureMotionTriangleGeometryDescriptor](mtlaccelerationstructuremotiontrianglegeometrydescriptor.md)
  A description of a list of triangle primitives, as motion keyframe data, to turn into an acceleration structure.
- [class MTLAccelerationStructureMotionCurveGeometryDescriptor](mtlaccelerationstructuremotioncurvegeometrydescriptor.md)
- [class MTLMotionKeyframeData](mtlmotionkeyframedata.md)
  Geometry data for a specific keyframe to use in a moving object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotionboundingboxgeometrydescriptor)*