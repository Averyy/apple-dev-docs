# MDLSubmeshTopology

**Framework**: Model I/O  
**Kind**: class

A description of how a submesh’s index buffer data is arranged and how that arrangement should be used to produce the submesh’s intended 3D shape.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLSubmeshTopology
```

#### Overview

Model I/O creates topology objects when importing assets containing non-uniform index buffers (that is, index buffers not composed of a single primitive type such as triangles or quads). You can also use topology objects (or load assets from file formats supporting topology information) to describe models for surface subdivision, identifying which edges or vertices remain sharp or become smooth when you use the [`newSubdividedMesh(_:submeshIndex:subdivisionLevels:)`](mdlmesh/newsubdividedmesh(_:submeshindex:subdivisionlevels:).md) method.

## Topics

### Identifying Faces
- [var faceTopology: (any MDLMeshBuffer)?](mdlsubmeshtopology/facetopology.md)
  A buffer identifying the faces in the submesh and the number of vertices in each.
- [var faceCount: Int](mdlsubmeshtopology/facecount.md)
  The number of faces in the submesh’s face topology buffer.
### Identifying Creases
- [var edgeCreaseIndices: (any MDLMeshBuffer)?](mdlsubmeshtopology/edgecreaseindices.md)
  A buffer containing vertex indices that describe edges to be treated as creases during surface subdivision.
- [var edgeCreases: (any MDLMeshBuffer)?](mdlsubmeshtopology/edgecreases.md)
  A buffer containing sharpness values to be applied to edges during surface subdivision.
- [var edgeCreaseCount: Int](mdlsubmeshtopology/edgecreasecount.md)
  The number of entries in the edge creases buffers.
- [var vertexCreaseIndices: (any MDLMeshBuffer)?](mdlsubmeshtopology/vertexcreaseindices.md)
  A buffer containing vertex indices to be treated as creases during surface subdivision.
- [var vertexCreases: (any MDLMeshBuffer)?](mdlsubmeshtopology/vertexcreases.md)
  A buffer containing sharpness values to be applied to points during surface subdivision.
- [var vertexCreaseCount: Int](mdlsubmeshtopology/vertexcreasecount.md)
  The number of entries in the vertex creases buffers.
### Identifying Holes
- [var holes: (any MDLMeshBuffer)?](mdlsubmeshtopology/holes.md)
  An index buffer identifying faces to be treated as holes in the mesh during surface subdivision.
- [var holeCount: Int](mdlsubmeshtopology/holecount.md)
  The number of entries in the holes buffer.
### Initializers
- [init(submesh: MDLSubmesh)](mdlsubmeshtopology/init(submesh:).md)

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

- [class MDLAsset](mdlasset.md)
  An indexed container for 3D objects and associated information, such as transform hierarchies, meshes, cameras, and lights.
- [class MDLObject](mdlobject.md)
  The base class for objects that are part of a 3D asset, including meshes, cameras, and lights.
- [class MDLTransform](mdltransform.md)
  A description of the local coordinate space transformations for a 3D object.
- [class MDLMesh](mdlmesh.md)
  A container for vertex buffer data to be used in rendering a 3D object.
- [class MDLSubmesh](mdlsubmesh.md)
  A container for index buffer data and material information to be used in rendering all or part of a 3D object.
- [protocol MDLNamed](mdlnamed.md)
  The common interface for Model I/O objects that expose a human-readable name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlsubmeshtopology)*