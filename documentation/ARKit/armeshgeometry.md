# ARMeshGeometry

**Framework**: ARKit  
**Kind**: class  
**Role**: Class

Mesh information stored in an efficient, array-based format.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+

## Declaration

```swift
class ARMeshGeometry
```

```objc
@interface ARMeshGeometry : NSObject
```

## Overview

The information in this class holds the geometry data for a single anchor of the scene mesh. Each vertex in the anchor’s mesh represents one connection point. Every three-vertex combination forms a unique triangle called a *face*. Each face includes an outside-directional normal and a [`classification`](./armeshgeometry/classification.md). If ARKit cannot classify a particular face, the value is `0`, –– the raw value for [`ARMeshClassification.none`](./armeshclassification/none.md).

## Topics

### Accessing Geometry Data
- [var vertices: ARGeometrySource](./armeshgeometry/vertices.md)
  The vertices of the mesh.
- [class ARGeometrySource](./argeometrysource.md)
  Mesh data in a buffer-based array.
### Getting Geometry Information
- [var classification: ARGeometrySource?](./armeshgeometry/classification.md)
  Classification for each face in the mesh.
- [enum ARMeshClassification](./armeshclassification.md)
  Enumeration of different classes of real-world objects that ARKit can identify.
- [var faces: ARGeometryElement](./armeshgeometry/faces.md)
  An object that contains a buffer of vertex indices of the geometry’s faces.
- [class ARGeometryElement](./argeometryelement.md)
  A container for index data, such as vertex indices of a face.
- [var normals: ARGeometrySource](./armeshgeometry/normals.md)
  Rays that define which direction is outside for each face.
### Initializers
- [init?(coder: NSCoder)](./armeshgeometry/init%28coder%29.md)

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

### Accessing the Mesh
- [var geometry: ARMeshGeometry](./armeshanchor/geometry.md)
  3D information about the mesh such as its shape and classifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/armeshgeometry)*