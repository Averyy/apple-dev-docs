# MTL4AccelerationStructureMotionTriangleGeometryDescriptor

**Framework**: Metal  
**Kind**: class

Describes motion triangle geometry, suitable for motion ray tracing.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class MTL4AccelerationStructureMotionTriangleGeometryDescriptor
```

#### Overview

Use a [`MTLResidencySet`](mtlresidencyset.md) to mark residency of all buffers this descriptor references when you build this acceleration structure.

## Topics

### Instance Properties
- [var indexBuffer: MTL4BufferRange](mtl4accelerationstructuremotiontrianglegeometrydescriptor/indexbuffer.md)
  Assigns an optional index buffer containing references to vertices in the vertex buffers you reference through the vertex buffers property.
- [var indexType: MTLIndexType](mtl4accelerationstructuremotiontrianglegeometrydescriptor/indextype.md)
  Specifies the size of the indices the `indexBuffer` contains, which is typically either 16 or 32-bits for each index.
- [var transformationMatrixBuffer: MTL4BufferRange](mtl4accelerationstructuremotiontrianglegeometrydescriptor/transformationmatrixbuffer.md)
  Assings an optional reference to a buffer containing a `float4x3` transformation matrix.
- [var transformationMatrixLayout: MTLMatrixLayout](mtl4accelerationstructuremotiontrianglegeometrydescriptor/transformationmatrixlayout.md)
  Configures the layout for the transformation matrix in the transformation matrix buffer.
- [var triangleCount: Int](mtl4accelerationstructuremotiontrianglegeometrydescriptor/trianglecount.md)
  Declares the number of triangles in the vertex buffers that the buffer in the vertex buffers property references.
- [var vertexBuffers: MTL4BufferRange](mtl4accelerationstructuremotiontrianglegeometrydescriptor/vertexbuffers.md)
  Assigns a buffer where each entry contains a reference to a vertex buffer.
- [var vertexFormat: MTLAttributeFormat](mtl4accelerationstructuremotiontrianglegeometrydescriptor/vertexformat.md)
  Defines the format of the vertices in the vertex buffers.
- [var vertexStride: Int](mtl4accelerationstructuremotiontrianglegeometrydescriptor/vertexstride.md)
  Sets the stride, in bytes, between vertices in all the vertex buffer.

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

- [class MTLAccelerationStructureMotionTriangleGeometryDescriptor](mtlaccelerationstructuremotiontrianglegeometrydescriptor.md)
  A description of a list of triangle primitives, as motion keyframe data, to turn into an acceleration structure.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotiontrianglegeometrydescriptor)*