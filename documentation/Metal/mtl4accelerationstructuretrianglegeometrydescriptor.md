# MTL4AccelerationStructureTriangleGeometryDescriptor

**Framework**: Metal  
**Kind**: class

Describes triangle geometry suitable for ray tracing.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class MTL4AccelerationStructureTriangleGeometryDescriptor
```

#### Overview

Use a [`MTLResidencySet`](mtlresidencyset.md) to mark residency of all buffers this descriptor references when you build this acceleration structure.

## Topics

### Instance Properties
- [var indexBuffer: MTL4BufferRange](mtl4accelerationstructuretrianglegeometrydescriptor/indexbuffer.md)
  Sets an optional index buffer containing references to vertices in the `vertexBuffer`.
- [var indexType: MTLIndexType](mtl4accelerationstructuretrianglegeometrydescriptor/indextype.md)
  Configures the size of the indices the `indexBuffer` contains, which is typically either 16 or 32-bits for each index.
- [var transformationMatrixBuffer: MTL4BufferRange](mtl4accelerationstructuretrianglegeometrydescriptor/transformationmatrixbuffer.md)
  Assigns an optional reference to a buffer containing a `float4x3` transformation matrix.
- [var transformationMatrixLayout: MTLMatrixLayout](mtl4accelerationstructuretrianglegeometrydescriptor/transformationmatrixlayout.md)
  Configures the layout for the transformation matrix in the transformation matrix buffer.
- [var triangleCount: Int](mtl4accelerationstructuretrianglegeometrydescriptor/trianglecount.md)
  Declares the number of triangles in this geometry descriptor.
- [var vertexBuffer: MTL4BufferRange](mtl4accelerationstructuretrianglegeometrydescriptor/vertexbuffer.md)
  Associates a vertex buffer containing triangle vertices.
- [var vertexFormat: MTLAttributeFormat](mtl4accelerationstructuretrianglegeometrydescriptor/vertexformat.md)
  Describes the format of the vertices in the vertex buffer.
- [var vertexStride: Int](mtl4accelerationstructuretrianglegeometrydescriptor/vertexstride.md)
  Sets the stride, in bytes, between vertices in the vertex buffer.

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

- [class MTL4AccelerationStructureGeometryDescriptor](mtl4accelerationstructuregeometrydescriptor.md)
  Base class for all Metal 4 acceleration structure geometry descriptors.
- [class MTLAccelerationStructureGeometryDescriptor](mtlaccelerationstructuregeometrydescriptor.md)
  A base class for descriptors that contain geometry data to convert into a ray-tracing acceleration structure.
- [class MTLAccelerationStructureTriangleGeometryDescriptor](mtlaccelerationstructuretrianglegeometrydescriptor.md)
  A description of a list of triangle primitives to turn into an acceleration structure.
- [class MTL4AccelerationStructureCurveGeometryDescriptor](mtl4accelerationstructurecurvegeometrydescriptor.md)
  Describes curve geometry suitable for ray tracing.
- [class MTLAccelerationStructureCurveGeometryDescriptor](mtlaccelerationstructurecurvegeometrydescriptor.md)
- [enum MTLCurveType](mtlcurvetype.md)
- [enum MTLCurveBasis](mtlcurvebasis.md)
- [enum MTLCurveEndCaps](mtlcurveendcaps.md)
- [class MTL4AccelerationStructureBoundingBoxGeometryDescriptor](mtl4accelerationstructureboundingboxgeometrydescriptor.md)
  Describes bounding-box geometry suitable for ray tracing.
- [class MTLAccelerationStructureBoundingBoxGeometryDescriptor](mtlaccelerationstructureboundingboxgeometrydescriptor.md)
  A description of a list of bounding boxes to turn into an acceleration structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuretrianglegeometrydescriptor)*