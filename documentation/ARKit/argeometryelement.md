# ARGeometryElement

**Framework**: ARKit  
**Kind**: class

A container for index data, such as vertex indices of a face.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
class ARGeometryElement
```

#### Overview

[`ARMeshGeometry`](armeshgeometry.md) uses geometry-elements to store face data (see [`faces`](armeshgeometry/faces.md)). Each face is defined by the primitive type, for example, [`ARGeometryPrimitiveType.triangle`](argeometryprimitivetype/triangle.md).

To demonstrate, an [`ARMeshGeometry`](armeshgeometry.md) instance with two triangle-type faces results in the following configuration:

- `faces` [`count`](argeometryelement/count.md) `= 2`
- `faces` [`indexCountPerPrimitive`](argeometryelement/indexcountperprimitive.md) `= 3` (because [`primitiveType`](argeometryelement/primitivetype.md) is [`ARGeometryPrimitiveType.triangle`](argeometryprimitivetype/triangle.md))
- `faces` [`bytesPerIndex`](argeometryelement/bytesperindex.md) `= 4` (because vertex indices are the type [`UInt32`](https://developer.apple.com/documentation/Swift/UInt32))
- The buffer’s total size in bytes `=` [`count`](argeometryelement/count.md) `*` [`indexCountPerPrimitive`](argeometryelement/indexcountperprimitive.md) `*` [`bytesPerIndex`](argeometryelement/bytesperindex.md) (which in this case, is `2 * 3 * 4 = 24` bytes)

## Topics

### Accessing Index Data
- [subscript(Int) -> [Int32]](argeometryelement/subscript(_:).md)
  Provides an array of vertex indices that respresents the geometric primitive at the subscripted index.
- [var buffer: any MTLBuffer](argeometryelement/buffer.md)
  A Metal buffer containing primitive data.
### Getting Index Information
- [var bytesPerIndex: Int](argeometryelement/bytesperindex.md)
  The number of bytes for each index.
- [var count: Int](argeometryelement/count.md)
  The number of primitives in the buffer.
- [var indexCountPerPrimitive: Int](argeometryelement/indexcountperprimitive.md)
  The number of indices for each primitive.
- [var primitiveType: ARGeometryPrimitiveType](argeometryelement/primitivetype.md)
  The geometry’s type of data (triangle, or line).
- [enum ARGeometryPrimitiveType](argeometryprimitivetype.md)
  The kind of connection between vertices.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var classification: ARGeometrySource?](armeshgeometry/classification.md)
  Classification for each face in the mesh.
- [enum ARMeshClassification](armeshclassification.md)
  Enumeration of different classes of real-world objects that ARKit can identify.
- [var faces: ARGeometryElement](armeshgeometry/faces.md)
  An object that contains a buffer of vertex indices of the geometry’s faces.
- [var normals: ARGeometrySource](armeshgeometry/normals.md)
  Rays that define which direction is outside for each face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeometryelement)*