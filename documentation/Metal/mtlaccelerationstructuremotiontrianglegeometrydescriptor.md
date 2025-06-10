# MTLAccelerationStructureMotionTriangleGeometryDescriptor

**Framework**: Metal  
**Kind**: class

A description of a list of triangle primitives, as motion keyframe data, to turn into an acceleration structure.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class MTLAccelerationStructureMotionTriangleGeometryDescriptor
```

## Mentions

- [Improving Ray-Tracing Data Access Using Per-Primitive Data](improving-ray-tracing-data-access-using-per-primitive-data.md)

## Topics

### Specifying the Number of Triangles
- [var triangleCount: Int](mtlaccelerationstructuremotiontrianglegeometrydescriptor/trianglecount.md)
  The number of triangles in the buffers.
### Specifying Index Data
- [var indexBuffer: (any MTLBuffer)?](mtlaccelerationstructuremotiontrianglegeometrydescriptor/indexbuffer.md)
  A buffer that contains indices for the vertices that compose the triangle list.
- [var indexType: MTLIndexType](mtlaccelerationstructuremotiontrianglegeometrydescriptor/indextype.md)
  The data type of indices in the index buffer.
- [var indexBufferOffset: Int](mtlaccelerationstructuremotiontrianglegeometrydescriptor/indexbufferoffset.md)
  The offset, in bytes, to the first index in the buffer.
### Specifying Vertex Data
- [var vertexBuffers: [MTLMotionKeyframeData]](mtlaccelerationstructuremotiontrianglegeometrydescriptor/vertexbuffers.md)
  An array of motion keyframes, each containing triangle data.
- [var vertexStride: Int](mtlaccelerationstructuremotiontrianglegeometrydescriptor/vertexstride.md)
  The stride, in bytes, between vertices in each vertex buffer.
### Instance Properties
- [var transformationMatrixBuffer: (any MTLBuffer)?](mtlaccelerationstructuremotiontrianglegeometrydescriptor/transformationmatrixbuffer.md)
- [var transformationMatrixBufferOffset: Int](mtlaccelerationstructuremotiontrianglegeometrydescriptor/transformationmatrixbufferoffset.md)
- [var transformationMatrixLayout: MTLMatrixLayout](mtlaccelerationstructuremotiontrianglegeometrydescriptor/transformationmatrixlayout.md)
- [var vertexFormat: MTLAttributeFormat](mtlaccelerationstructuremotiontrianglegeometrydescriptor/vertexformat.md)

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
- [class MTL4AccelerationStructureMotionCurveGeometryDescriptor](mtl4accelerationstructuremotioncurvegeometrydescriptor.md)
  Describes motion curve geometry, suitable for motion ray tracing.
- [class MTLAccelerationStructureMotionCurveGeometryDescriptor](mtlaccelerationstructuremotioncurvegeometrydescriptor.md)
- [class MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor](mtl4accelerationstructuremotionboundingboxgeometrydescriptor.md)
  Describes motion bounding box geometry, suitable for motion ray tracing.
- [class MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor](mtlaccelerationstructuremotionboundingboxgeometrydescriptor.md)
  A description of a list of bounding boxes, as motion keyframe data, to turn into an acceleration structure.
- [class MTLMotionKeyframeData](mtlmotionkeyframedata.md)
  Geometry data for a specific keyframe to use in a moving object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotiontrianglegeometrydescriptor)*