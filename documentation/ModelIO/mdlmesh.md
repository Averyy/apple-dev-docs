# MDLMesh

**Framework**: Model I/O  
**Kind**: class

A container for vertex buffer data to be used in rendering a 3D object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLMesh
```

#### Overview

A mesh contains one or more [`MDLSubmesh`](mdlsubmesh.md) objects. Each submesh contains index buffer data that describes how the mesh’s vertices should be combined for drawing and references material information describing an intended surface appearance for the submesh. Typically, you obtain meshes by traversing the object hierarchy of a [`MDLAsset`](mdlasset.md) object, but you can also create meshes from your own vertex data or create parametric meshes. The [`MDLMesh`](mdlmesh.md) class also supports processing meshes to generate vertex attributes or to bake lighting information.

## Topics

### Creating a Custom Mesh
- [init(vertexBuffer: any MDLMeshBuffer, vertexCount: Int, descriptor: MDLVertexDescriptor, submeshes: [MDLSubmesh])](mdlmesh/init(vertexbuffer:vertexcount:descriptor:submeshes:).md)
  Creates a mesh from a single vertex buffer with the specified parameters.
- [init(vertexBuffers: [any MDLMeshBuffer], vertexCount: Int, descriptor: MDLVertexDescriptor, submeshes: [MDLSubmesh])](mdlmesh/init(vertexbuffers:vertexcount:descriptor:submeshes:).md)
  Creates a mesh by unifying vertex data from multiple sources with the specified parameters.
- [init(bufferAllocator: (any MDLMeshBufferAllocator)?)](mdlmesh/init(bufferallocator:).md)
- [class func newSubdividedMesh(MDLMesh, submeshIndex: Int, subdivisionLevels: Int) -> Self?](mdlmesh/newsubdividedmesh(_:submeshindex:subdivisionlevels:).md)
  Creates a new mesh by subdividing the specified mesh.
- [init(meshBySubdividingMesh: MDLMesh, submeshIndex: Int32, subdivisionLevels: UInt32, allocator: (any MDLMeshBufferAllocator)?)](mdlmesh/init(meshbysubdividingmesh:submeshindex:subdivisionlevels:allocator:).md)
### Working with Vertex Data
- [var boundingBox: MDLAxisAlignedBoundingBox](mdlmesh/boundingbox.md)
  The minimum region entirely enclosing the mesh’s vertex positions, expressed in the model coordinate system of the mesh.
- [var submeshes: NSMutableArray?](mdlmesh/submeshes.md)
  The array of submeshes to be used in rendering the mesh.
- [var vertexBuffers: [any MDLMeshBuffer]](mdlmesh/vertexbuffers.md)
  The array of buffers that provide vertex data for the mesh.
- [var vertexCount: Int](mdlmesh/vertexcount.md)
  The number of vertices in the mesh.
- [var vertexDescriptor: MDLVertexDescriptor](mdlmesh/vertexdescriptor.md)
  A description of the format and layout of the mesh’s vertex buffers.
- [var allocator: any MDLMeshBufferAllocator](mdlmesh/allocator.md)
- [func addAttribute(withName: String, format: MDLVertexFormat)](mdlmesh/addattribute(withname:format:).md)
  Adds a vertex attribute to the mesh and creates a new, empty corresponding vertex buffer.
- [func addAttribute(withName: String, format: MDLVertexFormat, type: String, data: Data, stride: Int)](mdlmesh/addattribute(withname:format:type:data:stride:).md)
- [func addAttribute(withName: String, format: MDLVertexFormat, type: String, data: Data, stride: Int, time: TimeInterval)](mdlmesh/addattribute(withname:format:type:data:stride:time:).md)
- [func removeAttributeNamed(String)](mdlmesh/removeattributenamed(_:).md)
- [func replaceAttributeNamed(String, with: MDLVertexAttributeData)](mdlmesh/replaceattributenamed(_:with:).md)
- [func updateAttributeNamed(String, with: MDLVertexAttributeData)](mdlmesh/updateattributenamed(_:with:).md)
- [func addUnwrappedTextureCoordinates(forAttributeNamed: String)](mdlmesh/addunwrappedtexturecoordinates(forattributenamed:).md)
- [func vertexAttributeData(forAttributeNamed: String) -> MDLVertexAttributeData?](mdlmesh/vertexattributedata(forattributenamed:).md)
  Returns the vertex data for the specified attribute.
- [func vertexAttributeData(forAttributeNamed: String, as: MDLVertexFormat) -> MDLVertexAttributeData?](mdlmesh/vertexattributedata(forattributenamed:as:).md)
### Generating Geometry Data
- [func addNormals(withAttributeNamed: String?, creaseThreshold: Float)](mdlmesh/addnormals(withattributenamed:creasethreshold:).md)
  Generates surface normal data for the mesh based on its vertex position data.
- [func addTangentBasis(forTextureCoordinateAttributeNamed: String, tangentAttributeNamed: String, bitangentAttributeNamed: String?)](mdlmesh/addtangentbasis(fortexturecoordinateattributenamed:tangentattributenamed:bitangentattributenamed:).md)
  Generates surface tangent and bitangent data for the mesh based on its vertex position and texture coordinate data.
- [func addTangentBasis(forTextureCoordinateAttributeNamed: String, normalAttributeNamed: String, tangentAttributeNamed: String)](mdlmesh/addtangentbasis(fortexturecoordinateattributenamed:normalattributenamed:tangentattributenamed:).md)
  Generates surface tangent data for the mesh based on its vertex position, surface normal, and texture coordinate data.
- [func makeVerticesUnique()](mdlmesh/makeverticesunique.md)
  Modifies the mesh’s vertex buffers so that no vertices are shared by multiple faces.
### Generating Ambient Occlusion Data
- [func generateAmbientOcclusionTexture(withQuality: Float, attenuationFactor: Float, objectsToConsider: [MDLObject], vertexAttributeNamed: String, materialPropertyNamed: String) -> Bool](mdlmesh/generateambientocclusiontexture(withquality:attenuationfactor:objectstoconsider:vertexattributenamed:materialpropertynamed:).md)
  Calculates ambient occlusion (AO) information for the mesh and saves it in the mesh as a material property texture.
- [func generateAmbientOcclusionTexture(withSize: vector_int2, raysPerSample: Int, attenuationFactor: Float, objectsToConsider: [MDLObject], vertexAttributeNamed: String, materialPropertyNamed: String) -> Bool](mdlmesh/generateambientocclusiontexture(withsize:rayspersample:attenuationfactor:objectstoconsider:vertexattributenamed:materialpropertynamed:).md)
  Calculates ambient occlusion (AO) information for the mesh and saves it in the mesh as a material property texture of the specified size.
- [func generateAmbientOcclusionVertexColors(withQuality: Float, attenuationFactor: Float, objectsToConsider: [MDLObject], vertexAttributeNamed: String) -> Bool](mdlmesh/generateambientocclusionvertexcolors(withquality:attenuationfactor:objectstoconsider:vertexattributenamed:).md)
  Calculates ambient occlusion (AO) information for the mesh and saves it in the mesh as a vertex color attribute.
- [func generateAmbientOcclusionVertexColors(withRaysPerSample: Int, attenuationFactor: Float, objectsToConsider: [MDLObject], vertexAttributeNamed: String) -> Bool](mdlmesh/generateambientocclusionvertexcolors(withrayspersample:attenuationfactor:objectstoconsider:vertexattributenamed:).md)
  Calculates ambient occlusion (AO) information for the mesh, using the specified number of rays per sample, and saves it in the mesh as a vertex color attribute.
### Generating Light Map Data
- [func generateLightMapTexture(withQuality: Float, lightsToConsider: [MDLLight], objectsToConsider: [MDLObject], vertexAttributeNamed: String, materialPropertyNamed: String) -> Bool](mdlmesh/generatelightmaptexture(withquality:lightstoconsider:objectstoconsider:vertexattributenamed:materialpropertynamed:).md)
  Calculates static lighting information for the mesh and saves it in the mesh as a material property texture.
- [func generateLightMapTexture(withTextureSize: vector_int2, lightsToConsider: [MDLLight], objectsToConsider: [MDLObject], vertexAttributeNamed: String, materialPropertyNamed: String) -> Bool](mdlmesh/generatelightmaptexture(withtexturesize:lightstoconsider:objectstoconsider:vertexattributenamed:materialpropertynamed:).md)
  Calculates static lighting information for the mesh and saves it in the mesh as a material property texture of the specified size.
- [func generateLightMapVertexColorsWithLights(toConsider: [MDLLight], objectsToConsider: [MDLObject], vertexAttributeNamed: String) -> Bool](mdlmesh/generatelightmapvertexcolorswithlights(toconsider:objectstoconsider:vertexattributenamed:).md)
  Calculates static lighting information for the mesh and saves it in the mesh as a vertex color attribute.
### Creating Parametric Meshes
- [class func newBox(withDimensions: vector_float3, segments: vector_uint3, geometryType: MDLGeometryType, inwardNormals: Bool, allocator: (any MDLMeshBufferAllocator)?) -> Self](mdlmesh/newbox(withdimensions:segments:geometrytype:inwardnormals:allocator:).md)
  Creates a mesh in the shape of a rectangular box or cube.
- [class func newEllipsoid(withRadii: vector_float3, radialSegments: Int, verticalSegments: Int, geometryType: MDLGeometryType, inwardNormals: Bool, hemisphere: Bool, allocator: (any MDLMeshBufferAllocator)?) -> Self](mdlmesh/newellipsoid(withradii:radialsegments:verticalsegments:geometrytype:inwardnormals:hemisphere:allocator:).md)
  Creates a mesh in the shape of an ellipsoid or sphere.
- [class func newCylinder(withHeight: Float, radii: vector_float2, radialSegments: Int, verticalSegments: Int, geometryType: MDLGeometryType, inwardNormals: Bool, allocator: (any MDLMeshBufferAllocator)?) -> Self](mdlmesh/newcylinder(withheight:radii:radialsegments:verticalsegments:geometrytype:inwardnormals:allocator:).md)
  Generates a mesh in the shape of a right circular or elliptical cylinder.
- [class func newEllipticalCone(withHeight: Float, radii: vector_float2, radialSegments: Int, verticalSegments: Int, geometryType: MDLGeometryType, inwardNormals: Bool, allocator: (any MDLMeshBufferAllocator)?) -> Self](mdlmesh/newellipticalcone(withheight:radii:radialsegments:verticalsegments:geometrytype:inwardnormals:allocator:).md)
  Generates a mesh in the shape of an elliptical or circular cone.
- [class func newPlane(withDimensions: vector_float2, segments: vector_uint2, geometryType: MDLGeometryType, allocator: (any MDLMeshBufferAllocator)?) -> Self](mdlmesh/newplane(withdimensions:segments:geometrytype:allocator:).md)
  Generates a mesh in the shape of a rectangular plane.
- [class func newCapsule(withHeight: Float, radii: vector_float2, radialSegments: Int, verticalSegments: Int, hemisphereSegments: Int, geometryType: MDLGeometryType, inwardNormals: Bool, allocator: (any MDLMeshBufferAllocator)?) -> Self](mdlmesh/newcapsule(withheight:radii:radialsegments:verticalsegments:hemispheresegments:geometrytype:inwardnormals:allocator:).md)
- [class func newIcosahedron(withRadius: Float, inwardNormals: Bool, allocator: (any MDLMeshBufferAllocator)?) -> Self](mdlmesh/newicosahedron(withradius:inwardnormals:allocator:).md)
  Generates a mesh in the shape of a regular 20-sided polyhedron with triangular faces.
- [class func newIcosahedron(withRadius: Float, inwardNormals: Bool, geometryType: MDLGeometryType, allocator: (any MDLMeshBufferAllocator)?) -> Self](mdlmesh/newicosahedron(withradius:inwardnormals:geometrytype:allocator:).md)
- [init(boxWithExtent: vector_float3, segments: vector_uint3, inwardNormals: Bool, geometryType: MDLGeometryType, allocator: (any MDLMeshBufferAllocator)?)](mdlmesh/init(boxwithextent:segments:inwardnormals:geometrytype:allocator:).md)
- [init(sphereWithExtent: vector_float3, segments: vector_uint2, inwardNormals: Bool, geometryType: MDLGeometryType, allocator: (any MDLMeshBufferAllocator)?)](mdlmesh/init(spherewithextent:segments:inwardnormals:geometrytype:allocator:).md)
- [init(cylinderWithExtent: vector_float3, segments: vector_uint2, inwardNormals: Bool, topCap: Bool, bottomCap: Bool, geometryType: MDLGeometryType, allocator: (any MDLMeshBufferAllocator)?)](mdlmesh/init(cylinderwithextent:segments:inwardnormals:topcap:bottomcap:geometrytype:allocator:).md)
- [init(coneWithExtent: vector_float3, segments: vector_uint2, inwardNormals: Bool, cap: Bool, geometryType: MDLGeometryType, allocator: (any MDLMeshBufferAllocator)?)](mdlmesh/init(conewithextent:segments:inwardnormals:cap:geometrytype:allocator:).md)
- [init(planeWithExtent: vector_float3, segments: vector_uint2, geometryType: MDLGeometryType, allocator: (any MDLMeshBufferAllocator)?)](mdlmesh/init(planewithextent:segments:geometrytype:allocator:).md)
- [init(icosahedronWithExtent: vector_float3, inwardNormals: Bool, geometryType: MDLGeometryType, allocator: (any MDLMeshBufferAllocator)?)](mdlmesh/init(icosahedronwithextent:inwardnormals:geometrytype:allocator:).md)
- [init(capsuleWithExtent: vector_float3, cylinderSegments: vector_uint2, hemisphereSegments: Int32, inwardNormals: Bool, geometryType: MDLGeometryType, allocator: (any MDLMeshBufferAllocator)?)](mdlmesh/init(capsulewithextent:cylindersegments:hemispheresegments:inwardnormals:geometrytype:allocator:).md)
- [init(hemisphereWithExtent: vector_float3, segments: vector_uint2, inwardNormals: Bool, cap: Bool, geometryType: MDLGeometryType, allocator: (any MDLMeshBufferAllocator)?)](mdlmesh/init(hemispherewithextent:segments:inwardnormals:cap:geometrytype:allocator:).md)
### Instance Methods
- [func addOrthTanBasis(forTextureCoordinateAttributeNamed: String, normalAttributeNamed: String, tangentAttributeNamed: String)](mdlmesh/addorthtanbasis(fortexturecoordinateattributenamed:normalattributenamed:tangentattributenamed:).md)
- [func flipTextureCoordinates(inAttributeNamed: String)](mdlmesh/fliptexturecoordinates(inattributenamed:).md)
- [func makeVerticesUniqueAndReturnError() throws](mdlmesh/makeverticesuniqueandreturnerror.md)

## Relationships

### Inherits From
- [MDLObject](mdlobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MDLNamed](mdlnamed.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MDLAsset](mdlasset.md)
  An indexed container for 3D objects and associated information, such as transform hierarchies, meshes, cameras, and lights.
- [class MDLObject](mdlobject.md)
  The base class for objects that are part of a 3D asset, including meshes, cameras, and lights.
- [class MDLTransform](mdltransform.md)
  A description of the local coordinate space transformations for a 3D object.
- [class MDLSubmesh](mdlsubmesh.md)
  A container for index buffer data and material information to be used in rendering all or part of a 3D object.
- [class MDLSubmeshTopology](mdlsubmeshtopology.md)
  A description of how a submesh’s index buffer data is arranged and how that arrangement should be used to produce the submesh’s intended 3D shape.
- [protocol MDLNamed](mdlnamed.md)
  The common interface for Model I/O objects that expose a human-readable name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmesh)*