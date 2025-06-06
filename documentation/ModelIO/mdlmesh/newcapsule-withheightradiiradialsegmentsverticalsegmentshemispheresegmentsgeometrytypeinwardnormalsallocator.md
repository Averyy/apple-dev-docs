# newCapsule(withHeight:radii:radialSegments:verticalSegments:hemisphereSegments:geometryType:inwardNormals:allocator:)

**Framework**: Model I/O  
**Kind**: method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class func newCapsule(withHeight height: Float, radii: vector_float2, radialSegments: Int, verticalSegments: Int, hemisphereSegments: Int, geometryType: MDLGeometryType, inwardNormals: Bool, allocator: (any MDLMeshBufferAllocator)?) -> Self
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmesh/newcapsule(withheight:radii:radialsegments:verticalsegments:hemispheresegments:geometrytype:inwardnormals:allocator:))*