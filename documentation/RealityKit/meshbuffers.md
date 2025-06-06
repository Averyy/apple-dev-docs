# MeshBuffers

**Framework**: RealityKit  
**Kind**: enum

An object that holds the data for an model entity’s mesh.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
enum MeshBuffers
```

## Topics

### Structures
- [MeshBuffers.Identifier](meshbuffers/identifier.md)
- [MeshBuffers.Semantic](meshbuffers/semantic.md)
### Type Aliases
- [MeshBuffers.BlendShapeOffsets](meshbuffers/blendshapeoffsets.md)
- [MeshBuffers.JointInfluences](meshbuffers/jointinfluences-swift.typealias.md)
- [MeshBuffers.Normals](meshbuffers/normals-swift.typealias.md)
- [MeshBuffers.Positions](meshbuffers/positions-swift.typealias.md)
- [MeshBuffers.Tangents](meshbuffers/tangents-swift.typealias.md)
- [MeshBuffers.TextureCoordinates](meshbuffers/texturecoordinates-swift.typealias.md)
- [MeshBuffers.TriangleIndices](meshbuffers/triangleindices-swift.typealias.md)
### Type Properties
- [static let bitangents: MeshBuffers.Semantic<SIMD3<Float>>](meshbuffers/bitangents.md)
- [static let jointInfluences: MeshBuffers.Semantic<MeshJointInfluence>](meshbuffers/jointinfluences-swift.type.property.md)
- [static let normals: MeshBuffers.Semantic<SIMD3<Float>>](meshbuffers/normals-swift.type.property.md)
- [static let positions: MeshBuffers.Semantic<SIMD3<Float>>](meshbuffers/positions-swift.type.property.md)
- [static let tangents: MeshBuffers.Semantic<SIMD3<Float>>](meshbuffers/tangents-swift.type.property.md)
- [static let textureCoordinates: MeshBuffers.Semantic<SIMD2<Float>>](meshbuffers/texturecoordinates-swift.type.property.md)
- [static let triangleIndices: MeshBuffers.Semantic<UInt32>](meshbuffers/triangleindices-swift.type.property.md)
### Type Methods
- [static func blendShapeOffsets(named: String) -> MeshBuffers.Semantic<SIMD3<Float>>](meshbuffers/blendshapeoffsets(named:).md)
- [static func custom<Value>(String, type: Value.Type) -> MeshBuffers.Semantic<Value>](meshbuffers/custom(_:type:).md)
### Enumerations
- [MeshBuffers.ElementType](meshbuffers/elementtype.md)
  The data type for each element of the buffer.
- [MeshBuffers.Rate](meshbuffers/rate.md)
  Defines how elements in the buffer map to features of the mesh.

## See Also

- [struct MeshBuffer](meshbuffer.md)
  Mesh buffer containing elements of any type.
- [protocol MeshBufferContainer](meshbuffercontainer.md)
  Conforming objects contain a table of mesh buffers.
- [protocol MeshBufferSemantic](meshbuffersemantic.md)
  A protocol that holds an identifier value for mesh buffers.
- [struct AnyMeshBuffer](anymeshbuffer.md)
  Mesh buffer stored in the container.
- [struct MeshInstanceCollection](meshinstancecollection.md)
  An object that holds a collection of mesh resource instances.
- [struct MeshModelCollection](meshmodelcollection.md)
  An object that holds a collection of mesh models.
- [struct MeshPartCollection](meshpartcollection.md)
  An object that holds a collection of mesh parts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshbuffers)*