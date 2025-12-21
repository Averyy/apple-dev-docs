# MTLAccelerationStructureTriangleGeometryDescriptor

**Framework**: Metal  
**Kind**: class

A description of a list of triangle primitives to turn into an acceleration structure.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class MTLAccelerationStructureTriangleGeometryDescriptor
```

## Mentions

- [Improving ray-tracing data access using per-primitive data](improving-ray-tracing-data-access-using-per-primitive-data.md)

## Topics

### Configuring the number of triangles
- [var triangleCount: Int](mtlaccelerationstructuretrianglegeometrydescriptor/trianglecount.md)
  The number of triangles in the buffers.
### Configuring index data
- [var indexType: MTLIndexType](mtlaccelerationstructuretrianglegeometrydescriptor/indextype.md)
  The data type of indices in the index buffer.
- [var indexBuffer: (any MTLBuffer)?](mtlaccelerationstructuretrianglegeometrydescriptor/indexbuffer.md)
  A buffer that contains indices for the vertices that compose the triangle list.
- [var indexBufferOffset: Int](mtlaccelerationstructuretrianglegeometrydescriptor/indexbufferoffset.md)
  The offset, in bytes, to the first index in the buffer.
### Configuring vertex data
- [var vertexFormat: MTLAttributeFormat](mtlaccelerationstructuretrianglegeometrydescriptor/vertexformat.md)
  The format of each vertex position in the vertex buffer property.
- [var vertexBuffer: (any MTLBuffer)?](mtlaccelerationstructuretrianglegeometrydescriptor/vertexbuffer.md)
  A buffer that contains vertex data.
- [var vertexBufferOffset: Int](mtlaccelerationstructuretrianglegeometrydescriptor/vertexbufferoffset.md)
  The offset, in bytes, for the first vertex in the vertex buffer.
- [var vertexStride: Int](mtlaccelerationstructuretrianglegeometrydescriptor/vertexstride.md)
  The stride, in bytes, between vertices in the vertex buffer.
### Configuring transformation data
- [var transformationMatrixLayout: MTLMatrixLayout](mtlaccelerationstructuretrianglegeometrydescriptor/transformationmatrixlayout.md)
- [var transformationMatrixBuffer: (any MTLBuffer)?](mtlaccelerationstructuretrianglegeometrydescriptor/transformationmatrixbuffer.md)
- [var transformationMatrixBufferOffset: Int](mtlaccelerationstructuretrianglegeometrydescriptor/transformationmatrixbufferoffset.md)

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
- [class MTL4AccelerationStructureCurveGeometryDescriptor](mtl4accelerationstructurecurvegeometrydescriptor.md)
  Describes curve geometry suitable for ray tracing.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor)*