# MeshBufferContainer

**Framework**: RealityKit  
**Kind**: protocol

Conforming objects contain a table of mesh buffers.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
protocol MeshBufferContainer
```

## Topics

### Accessing texture coordinates
- [var textureCoordinates1: MeshBuffers.TextureCoordinates?](meshbuffercontainer/texturecoordinates1.md)
  Buffer of texture coordinates set 1, if any.
- [var textureCoordinates2: MeshBuffers.TextureCoordinates?](meshbuffercontainer/texturecoordinates2.md)
  Buffer of texture coordinates set 2, if any.
- [var textureCoordinates3: MeshBuffers.TextureCoordinates?](meshbuffercontainer/texturecoordinates3.md)
  Buffer of texture coordinates set 3, if any.
- [var textureCoordinates4: MeshBuffers.TextureCoordinates?](meshbuffercontainer/texturecoordinates4.md)
  Buffer of texture coordinates set 4, if any.
- [var textureCoordinates5: MeshBuffers.TextureCoordinates?](meshbuffercontainer/texturecoordinates5.md)
  Buffer of texture coordinates set 5, if any.
- [var textureCoordinates6: MeshBuffers.TextureCoordinates?](meshbuffercontainer/texturecoordinates6.md)
  Buffer of texture coordinates set 6, if any.
- [var textureCoordinates7: MeshBuffers.TextureCoordinates?](meshbuffercontainer/texturecoordinates7.md)
  Buffer of texture coordinates set 7, if any.
### Instance Properties
- [var bitangents: MeshBuffers.Tangents?](meshbuffercontainer/bitangents.md)
  Buffer of bitangents, if any.
- [var blendShapeNames: [String]](meshbuffercontainer/blendshapenames.md)
  An array of blendShape names that exist in MeshBufferContainer
- [var buffers: [MeshBuffers.Identifier : AnyMeshBuffer]](meshbuffercontainer/buffers.md)
  Descriptors for the buffers.
- [var normals: MeshBuffers.Normals?](meshbuffercontainer/normals.md)
  Buffer of normals, if any.
- [var positions: MeshBuffers.Positions](meshbuffercontainer/positions.md)
  Positions of all the points.
- [var tangents: MeshBuffers.Tangents?](meshbuffercontainer/tangents.md)
  Buffer of tangents, if any.
- [var textureCoordinates: MeshBuffers.TextureCoordinates?](meshbuffercontainer/texturecoordinates.md)
  Buffer of texture coordinates, if any.
- [var uv2: MeshBuffers.UVs?](meshbuffercontainer/uv2.md)
  Buffer of UV data set 2, if any.
- [var uv3: MeshBuffers.UVs?](meshbuffercontainer/uv3.md)
  Buffer of UV data set 3, if any.
- [var uv4: MeshBuffers.UVs?](meshbuffercontainer/uv4.md)
  Buffer of UV data set 4, if any.
- [var uv5: MeshBuffers.UVs?](meshbuffercontainer/uv5.md)
  Buffer of UV data set 5, if any.
- [var uv6: MeshBuffers.UVs?](meshbuffercontainer/uv6.md)
  Buffer of UV data set 6, if any.
- [var uv7: MeshBuffers.UVs?](meshbuffercontainer/uv7.md)
  Buffer of UV data set 7, if any.
### Instance Methods
- [func blendShapeOffsets(named: String) -> MeshBuffers.BlendShapeOffsets?](meshbuffercontainer/blendshapeoffsets(named:).md)
- [func setBlendShapeOffsets(named: String, buffer: MeshBuffers.BlendShapeOffsets?)](meshbuffercontainer/setblendshapeoffsets(named:buffer:).md)
### Subscripts
- [subscript<S>(S) -> MeshBuffer<S.Element>?](meshbuffercontainer/subscript(_:).md)
  The buffer for a given semantic. There can only be one buffer for any given ID.

## Relationships

### Conforming Types
- [MeshDescriptor](meshdescriptor.md)
- [MeshResource.Part](meshresource/part.md)

## See Also

- [struct MeshBuffer](meshbuffer.md)
  Mesh buffer containing elements of any type.
- [protocol MeshBufferSemantic](meshbuffersemantic.md)
  A protocol that holds an identifier value for mesh buffers.
- [enum MeshBuffers](meshbuffers.md)
  An object that holds the data for an model entity’s mesh.
- [struct AnyMeshBuffer](anymeshbuffer.md)
  Mesh buffer stored in the container.
- [struct MeshInstanceCollection](meshinstancecollection.md)
  An object that holds a collection of mesh resource instances.
- [struct MeshModelCollection](meshmodelcollection.md)
  An object that holds a collection of mesh models.
- [struct MeshPartCollection](meshpartcollection.md)
  An object that holds a collection of mesh parts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshbuffercontainer)*