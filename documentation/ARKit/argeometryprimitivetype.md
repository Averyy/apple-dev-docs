# ARGeometryPrimitiveType

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

The kind of connection between vertices.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+

## Declaration

```swift
enum ARGeometryPrimitiveType
```

```c
enum ARGeometryPrimitiveType : NSInteger;
```

## Overview

When you enable [`sceneReconstruction`](./arworldtrackingconfiguration/scenereconstruction.md) on a world-tracking configuration, ARKit provies a wireframe mesh that models the shape of the real world using a collection of connected vertices. ARKit uses [`ARGeometryPrimitiveType`](./argeometryprimitivetype.md) to indicate how a particular property of that mesh is interpreted. For example, a mesh geometry’s [`faces`](./armeshgeometry/faces.md) property specifies that each face within the geometry is of type [`ARGeometryPrimitiveType.triangle`](./argeometryprimitivetype/triangle.md).

## Topics

### Type of Connection
- [ARGeometryPrimitiveType.line](./argeometryprimitivetype/line.md)
  A line segment in which a line connects two vertices.
- [ARGeometryPrimitiveType.triangle](./argeometryprimitivetype/triangle.md)
  Three vertices that connect to form a triangle.
### Initializers
- [init?(rawValue: Int)](./argeometryprimitivetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting Index Information
- [var bytesPerIndex: Int](./argeometryelement/bytesperindex.md)
  The number of bytes for each index.
- [var count: Int](./argeometryelement/count.md)
  The number of primitives in the buffer.
- [var indexCountPerPrimitive: Int](./argeometryelement/indexcountperprimitive.md)
  The number of indices for each primitive.
- [var primitiveType: ARGeometryPrimitiveType](./argeometryelement/primitivetype.md)
  The geometry’s type of data (triangle, or line).


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeometryprimitivetype)*