# ARGeometrySource

**Framework**: ARKit  
**Kind**: class  
**Role**: Class

Mesh data in a buffer-based array.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+

## Declaration

```swift
class ARGeometrySource
```

```objc
@interface ARGeometrySource : NSObject
```

#### Overview

Mesh-anchor geometry ([`ARMeshGeometry`](./armeshgeometry.md)) uses geometry sources to hold 3D data like vertices, and normals, in an efficent, array-like format. A Metal buffer wraps the data, and other properties specify  how to interpret that data.

In the case that [`componentsPerVector`](./argeometrysource/componentspervector.md) is greater than 1, the element type of the geometry-source array is itself a sequence (pairs, triplets, and so on).

## Topics

### Accessing Geometry
- [subscript(Int32) -> (Float, Float, Float)](./argeometrysource/subscript%28_%29-3v98f.md)
  Provides the source float triplet at the subscripted index.
- [subscript(Int32) -> CUnsignedChar](./argeometrysource/subscript%28_%29-7jf4y.md)
  Provides the number at the subscripted index.
- [var buffer: any MTLBuffer](./argeometrysource/buffer.md)
  A Metal buffer that contains a list of vectors.
### Getting Geometry Information
- [var componentsPerVector: Int](./argeometrysource/componentspervector.md)
  The number of scalar components in each vector.
- [var count: Int](./argeometrysource/count.md)
  The number of vectors in the buffer.
- [var format: MTLVertexFormat](./argeometrysource/format.md)
  The type of vector data in the buffer.
- [var offset: Int](./argeometrysource/offset.md)
  The offset, in bytes, from the beginning of the buffer.
- [var stride: Int](./argeometrysource/stride.md)
  The length, in bytes, of the start of one vector in the buffer to the start of the next vector.
### Initializers
- [init?(coder: NSCoder)](./argeometrysource/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing Geometry Data
- [var vertices: ARGeometrySource](./armeshgeometry/vertices.md)
  The vertices of the mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeometrysource)*