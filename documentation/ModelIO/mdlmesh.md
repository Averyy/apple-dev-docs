# MDLMesh

**Framework**: Model I/O  
**Kind**: class  
**Role**: Class

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

```objc
@interface MDLMesh : MDLObject
```

#### Overview

A mesh contains one or more [`MDLSubmesh`](./mdlsubmesh.md) objects. Each submesh contains index buffer data that describes how the mesh’s vertices should be combined for drawing and references material information describing an intended surface appearance for the submesh. Typically, you obtain meshes by traversing the object hierarchy of a [`MDLAsset`](./mdlasset.md) object, but you can also create meshes from your own vertex data or create parametric meshes. The [`MDLMesh`](./mdlmesh.md) class also supports processing meshes to generate vertex attributes or to bake lighting information.

## Topics

### Creating a Custom Mesh
- [init(vertexBuffer: any MDLMeshBuffer, vertexCount: Int, descriptor: MDLVertexDescriptor, submeshes: [MDLSubmesh])](./mdlmesh/init%28vertexbuffer,vertexcount,descriptor,submeshes%29.md)
  Creates a mesh from a single vertex buffer with the specified parameters.
- [init(vertexBuffers: [any MDLMeshBuffer], vertexCount: Int, descriptor: MDLVertexDescriptor, submeshes: [MDLSubmesh])](./mdlmesh/init%28vertexbuffers,vertexcount,descriptor,submeshes%29.md)
  Creates a mesh by unifying vertex data from multiple sources with the specified parameters.
- [init(bufferAllocator: (any MDLMeshBufferAllocator)?)](./mdlmesh/init%28bufferallocator%29.md)
- [class func newSubdividedMesh(MDLMesh, submeshIndex: Int, subdivisionLevels: Int) -> Self?](./mdlmesh/newsubdividedmesh%28_,submeshindex,subdivisionlevels%29.md)
  Creates a new mesh by subdividing the specified mesh.
- [init(meshBySubdividingMesh: MDLMesh, submeshIndex: Int32, subdivisionLevels: UInt32, allocator: (any MDLMeshBufferAllocator)?)](./mdlmesh/init%28meshbysubdividingmesh,submeshindex,subdivisionlevels,allocator%29.md)
### Working with Vertex Data
- [var boundingBox: MDLAxisAlignedBoundingBox](./mdlmesh/boundingbox.md)
  The minimum region entirely enclosing the mesh’s vertex positions, expressed in the model coordinate system of the mesh.
- [var submeshes: NSMutableArray?](./mdlmesh/submeshes.md)
  The array of submeshes to be used in rendering the mesh.
- [var vertexBuffers: [any MDLMeshBuffer]](./mdlmesh/vertexbuffers.md)
  The array of buffers that provide vertex data for the mesh.
- [var vertexCount: Int](./mdlmesh/vertexcount.md)
  The number of vertices in the mesh.
- [var vertexDescriptor: MDLVertexDescriptor](./mdlmesh/vertexdescriptor.md)
  A description of the format and layout of the mesh’s vertex buffers.
- [var allocator: any MDLMeshBufferAllocator](./mdlmesh/allocator.md)
- [func addAttribute(withName: String, format: MDLVertexFormat)](./mdlmesh/addattribute%28withname,format%29.md)
  Adds a vertex attribute to the mesh and creates a new, empty corresponding vertex buffer.
- [func addAttribute(withName: String, format: MDLVertexFormat, type: String, data: Data, stride: Int)](./mdlmesh/addattribute%28withname,format,type,data,stride%29.md)
- [func addAttribute(withName: String, format: MDLVertexFormat, type: String, data: Data, stride: Int, time: TimeInterval)](./mdlmesh/addattribute%28withname,format,type,data,stride,time%29.md)
- [func removeAttributeNamed(String)](./mdlmesh/removeattributenamed%28_%29.md)
- [func replaceAttributeNamed(String, with: MDLVertexAttributeData)](./mdlmesh/replaceattributenamed%28_,with%29.md)
- [func updateAttributeNamed(String, with: MDLVertexAttributeData)](./mdlmesh/updateattributenamed%28_,with%29.md)
- [func addUnwrappedTextureCoordinates(forAttributeNamed: String)](./mdlmesh/addunwrappedtexturecoordinates%28forattributenamed%29.md)
- [func vertexAttributeData(forAttributeNamed: String) -> MDLVertexAttributeData?](./mdlmesh/vertexattributedata%28forattributenamed%29.md)
  Returns the vertex data for the specified attribute.
- [func vertexAttributeData(forAttributeNamed: String, as: MDLVertexFormat) -> MDLVertexAttributeData?](./mdlmesh/vertexattributedata%28forattributenamed,as%29.md)
### Generating Geometry Data
- [func addNormals(withAttributeNamed: String?, creaseThreshold: Float)](./mdlmesh/addnormals%28withattributenamed,creasethreshold%29.md)
  Generates surface normal data for the mesh based on its vertex position data.
- [func addTangentBasis(forTextureCoordinateAttributeNamed: String, tangentAttributeNamed: String, bitangentAttributeNamed: String?)](./mdlmesh/addtangentbasis%28fortexturecoordinateattributenamed,tangentattributenamed,bitangentattributenamed%29.md)
  Generates surface tangent and bitangent data for the mesh based on its vertex position and texture coordinate data.
- [func addTangentBasis(forTextureCoordinateAttributeNamed: String, normalAttributeNamed: String, tangentAttributeNamed: String)](./mdlmesh/addtangentbasis%28fortexturecoordinateattributenamed,normalattributenamed,tangentattributenamed%29.md)
  Generates surface tangent data for the mesh based on its vertex position, surface normal, and texture coordinate data.
- [func makeVerticesUnique()](./mdlmesh/makeverticesunique%28%29.md)
  Modifies the mesh’s vertex buffers so that no vertices are shared by multiple faces.
### Generating Ambient Occlusion Data
- [func generateAmbientOcclusionTexture(withQuality: Float, attenuationFactor: Float, objectsToConsider: [MDLObject], vertexAttributeNamed: String, materialPropertyNamed: String) -> Bool](./mdlmesh/generateambientocclusiontexture%28withquality,attenuationfactor,objectstoconsider,vertexattributenamed,materialpropertynamed%29.md)
  Calculates ambient occlusion (AO) information for the mesh and saves it in the mesh as a material property texture.
- [func generateAmbientOcclusionTexture(withSize: vector_int2, raysPerSample: Int, attenuationFactor: Float, objectsToConsider: [MDLObject], vertexAttributeNamed: String, materialPropertyNamed: String) -> Bool](./mdlmesh/generateambientocclusiontexture%28withsize,rayspersample,attenuationfactor,objectstoconsider,vertexattributenamed,materialpropertynamed%29.md)
  Calculates ambient occlusion (AO) information for the mesh and saves it in the mesh as a material property texture of the specified size.
- [func generateAmbientOcclusionVertexColors(withQuality: Float, attenuationFactor: Float, objectsToConsider: [MDLObject], vertexAttributeNamed: String) -> Bool](./mdlmesh/generateambientocclusionvertexcolors%28withquality,attenuationfactor,objectstoconsider,vertexattributenamed%29.md)
  Calculates ambient occlusion (AO) information for the mesh and saves it in the mesh as a vertex color attribute.
- [func generateAmbientOcclusionVertexColors(withRaysPerSample: Int, attenuationFactor: Float, objectsToConsider: [MDLObject], vertexAttributeNamed: String) -> Bool](./mdlmesh/generateambientocclusionvertexcolors%28withrayspersample,attenuationfactor,objectstoconsider,vertexattributenamed%29.md)
  Calculates ambient occlusion (AO) information for the mesh, using the specified number of rays per sample, and saves it in the mesh as a vertex color attribute.
### Generating Light Map Data
- [func generateLightMapTexture(withQuality: Float, lightsToConsider: [MDLLight], objectsToConsider: [MDLObject], vertexAttributeNamed: String, materialPropertyNamed: String) -> Bool](./mdlmesh/generatelightmaptexture%28withquality,lightstoconsider,objectstoconsider,vertexattributenamed,materialpropertynamed%29.md)
  Calculates static lighting information for the mesh and saves it in the mesh as a material property texture.
- [func generateLightMapTexture(withTextureSize: vector_int2, lightsToConsider: [MDLLight], objectsToConsider: [MDLObject], vertexAttributeNamed: String, materialPropertyNamed: String) -> Bool](./mdlmesh/generatelightmaptexture%28withtexturesize,lightstoconsider,objectstoconsider,vertexattributenamed,materialpropertynamed%29.md)
  Calculates static lighting information for the mesh and saves it in the mesh as a material property texture of the specified size.
- [func generateLightMapVertexColorsWithLights(toConsider: [MDLLight], objectsToConsider: [MDLObject], vertexAttributeNamed: String) -> Bool](./mdlmesh/generatelightmapvertexcolorswithlights%28toconsider,objectstoconsider,vertexattributenamed%29.md)
  Calculates static lighting information for the mesh and saves it in the mesh as a vertex color attribute.
### Creating Parametric Meshes
- [class func newBox(withDimensions: vector_float3, segments: vector_uint3, geometryType: MDLGeometryType, inwardNormals: Bool, allocator: (any MDLMeshBufferAllocator)?) -> Self](./mdlmesh/newbox%28withdimensions,segments,geometrytype,inwardnormals,allocator%29.md)
  Creates a mesh in the shape of a rectangular box or cube.
- [class func newEllipsoid(withRadii: vector_float3, radialSegments: Int, verticalSegments: Int, geometryType: MDLGeometryType, inwardNormals: Bool, hemisphere: Bool, allocator: (any MDLMeshBufferAllocator)?) -> Self](./mdlmesh/newellipsoid%28withradii,radialsegments,verticalsegments,geometrytype,inwardnormals,hemisphere,allocator%29.md)
  Creates a mesh in the shape of an ellipsoid or sphere.
- [class func newCylinder(withHeight: Float, radii: vector_float2, radialSegments: Int, verticalSegments: Int, geometryType: MDLGeometryType, inwardNormals: Bool, allocator: (any MDLMeshBufferAllocator)?) -> Self](./mdlmesh/newcylinder%28withheight,radii,radialsegments,verticalsegments,geometrytype,inwardnormals,allocator%29.md)
  Generates a mesh in the shape of a right circular or elliptical cylinder.
- [class func newEllipticalCone(withHeight: Float, radii: vector_float2, radialSegments: Int, verticalSegments: Int, geometryType: MDLGeometryType, inwardNormals: Bool, allocator: (any MDLMeshBufferAllocator)?) -> Self](./mdlmesh/newellipticalcone%28withheight,radii,radialsegments,verticalsegments,geometrytype,inwardnormals,allocator%29.md)
  Generates a mesh in the shape of an elliptical or circular cone.
- [class func newPlane(withDimensions: vector_float2, segments: vector_uint2, geometryType: MDLGeometryType, allocator: (any MDLMeshBufferAllocator)?) -> Self](./mdlmesh/newplane%28withdimensions,segments,geometrytype,allocator%29.md)
  Generates a mesh in the shape of a rectangular plane.
- [class func newCapsule(withHeight: Float, radii: vector_float2, radialSegments: Int, verticalSegments: Int, hemisphereSegments: Int, geometryType: MDLGeometryType, inwardNormals: Bool, allocator: (any MDLMeshBufferAllocator)?) -> Self](./mdlmesh/newcapsule%28withheight,radii,radialsegments,verticalsegments,hemispheresegments,geometrytype,inwardnormals,allocator%29.md)
- [class func newIcosahedron(withRadius: Float, inwardNormals: Bool, allocator: (any MDLMeshBufferAllocator)?) -> Self](./mdlmesh/newicosahedron%28withradius,inwardnormals,allocator%29.md)
  Generates a mesh in the shape of a regular 20-sided polyhedron with triangular faces.
- [class func newIcosahedron(withRadius: Float, inwardNormals: Bool, geometryType: MDLGeometryType, allocator: (any MDLMeshBufferAllocator)?) -> Self](./mdlmesh/newicosahedron%28withradius,inwardnormals,geometrytype,allocator%29.md)
- [init(boxWithExtent: vector_float3, segments: vector_uint3, inwardNormals: Bool, geometryType: MDLGeometryType, allocator: (any MDLMeshBufferAllocator)?)](./mdlmesh/init%28boxwithextent,segments,inwardnormals,geometrytype,allocator%29.md)
- [init(sphereWithExtent: vector_float3, segments: vector_uint2, inwardNormals: Bool, geometryType: MDLGeometryType, allocator: (any MDLMeshBufferAllocator)?)](./mdlmesh/init%28spherewithextent,segments,inwardnormals,geometrytype,allocator%29.md)
- [init(cylinderWithExtent: vector_float3, segments: vector_uint2, inwardNormals: Bool, topCap: Bool, bottomCap: Bool, geometryType: MDLGeometryType, allocator: (any MDLMeshBufferAllocator)?)](./mdlmesh/init%28cylinderwithextent,segments,inwardnormals,topcap,bottomcap,geometrytype,allocator%29.md)
- [init(coneWithExtent: vector_float3, segments: vector_uint2, inwardNormals: Bool, cap: Bool, geometryType: MDLGeometryType, allocator: (any MDLMeshBufferAllocator)?)](./mdlmesh/init%28conewithextent,segments,inwardnormals,cap,geometrytype,allocator%29.md)
- [init(planeWithExtent: vector_float3, segments: vector_uint2, geometryType: MDLGeometryType, allocator: (any MDLMeshBufferAllocator)?)](./mdlmesh/init%28planewithextent,segments,geometrytype,allocator%29.md)
- [init(icosahedronWithExtent: vector_float3, inwardNormals: Bool, geometryType: MDLGeometryType, allocator: (any MDLMeshBufferAllocator)?)](./mdlmesh/init%28icosahedronwithextent,inwardnormals,geometrytype,allocator%29.md)
- [init(capsuleWithExtent: vector_float3, cylinderSegments: vector_uint2, hemisphereSegments: Int32, inwardNormals: Bool, geometryType: MDLGeometryType, allocator: (any MDLMeshBufferAllocator)?)](./mdlmesh/init%28capsulewithextent,cylindersegments,hemispheresegments,inwardnormals,geometrytype,allocator%29.md)
- [init(hemisphereWithExtent: vector_float3, segments: vector_uint2, inwardNormals: Bool, cap: Bool, geometryType: MDLGeometryType, allocator: (any MDLMeshBufferAllocator)?)](./mdlmesh/init%28hemispherewithextent,segments,inwardnormals,cap,geometrytype,allocator%29.md)
### Instance Methods
- [func addOrthTanBasis(forTextureCoordinateAttributeNamed: String, normalAttributeNamed: String, tangentAttributeNamed: String)](./mdlmesh/addorthtanbasis%28fortexturecoordinateattributenamed,normalattributenamed,tangentattributenamed%29.md)
- [func flipTextureCoordinates(inAttributeNamed: String)](./mdlmesh/fliptexturecoordinates%28inattributenamed%29.md)
- [func makeVerticesUniqueAndReturnError() throws](./mdlmesh/makeverticesuniqueandreturnerror%28%29.md)
### Type Methods
- [+ meshWithSCNGeometry:](./mdlmesh/meshwithscngeometry_.md)
- [+ meshWithSCNGeometry:bufferAllocator:](./mdlmesh/meshwithscngeometry_bufferallocator_.md)

## Relationships

### Inherits From
- [MDLObject](./mdlobject.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [MDLNamed](./mdlnamed.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### 3D Asset Basics
- [class MDLAsset](./mdlasset.md)
  An indexed container for 3D objects and associated information, such as transform hierarchies, meshes, cameras, and lights.
- [class MDLObject](./mdlobject.md)
  The base class for objects that are part of a 3D asset, including meshes, cameras, and lights.
- [class MDLTransform](./mdltransform.md)
  A description of the local coordinate space transformations for a 3D object.
- [class MDLSubmesh](./mdlsubmesh.md)
  A container for index buffer data and material information to be used in rendering all or part of a 3D object.
- [class MDLSubmeshTopology](./mdlsubmeshtopology.md)
  A description of how a submesh’s index buffer data is arranged and how that arrangement should be used to produce the submesh’s intended 3D shape.
- [protocol MDLNamed](./mdlnamed.md)
  The common interface for Model I/O objects that expose a human-readable name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmesh)*