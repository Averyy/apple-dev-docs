# SCNGeometrySource

**Framework**: SceneKit  
**Kind**: class

A container for vertex data forming part of the definition for a three-dimensional object, or geometry.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class SCNGeometrySource
```

#### Overview

You use geometry sources together with [`SCNGeometryElement`](scngeometryelement.md) objects to define custom [`SCNGeometry`](scngeometry.md) objects or to inspect the data that composes an existing geometry.

You create a custom geometry using a three-step process:

1. Create one or more [`SCNGeometrySource`](scngeometrysource.md) objects containing vertex data. Each geometry source defines an attribute, or semantic, of the vertices it describes. You must provide at least one geometry source, using the [`vertex`](scngeometrysource/semantic-swift.struct/vertex.md) semantic, to create a custom geometry; typically you also provide geometry sources for surface normals and texture coordinates.
2. Create at least one [`SCNGeometryElement`](scngeometryelement.md) object, containing an array of indices identifying vertices in the geometry sources and describing the drawing primitive that SceneKit uses to connect the vertices when rendering the geometry.
3. Create an [`SCNGeometry`](scngeometry.md) instance from the geometry sources and geometry elements.

##### Interleaving Vertex Data

Because most geometries use more than one geometry source and the GPU typically uses data from multiple sources together, you can achieve better rendering performance for custom geometries by interleaving the vertex data for multiple semantics in the same array.

To do this, first create an array where each element contains values for multiple semantics for the same vertex. Next, create an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object from that array, and create each geometry source from that data using the `offset` and `stride` parameters to specify where the values for each semantic can be found in the array. To make specifying the sizes and locations of vectors more convenient, you can define your own data structure for vertices and use the `sizeof` (and, in Objective-C, `offsetof`) functions, as shown in Listing 1.

Listing 1. Creating multiple geometry sources from interleaved data

```objc
typedef struct {
    float x, y, z;    // position
    float nx, ny, nz; // normal
    float s, t;       // texture coordinates
} MyVertex;
 
MyVertex vertices[VERTEX_COUNT] = { /* ... vertex data ... */ };
NSData *data = [NSData dataWithBytes:vertices length:sizeof(vertices)];
SCNGeometrySource *vertexSource, *normalSource, *tcoordSource;
 
vertexSource = [SCNGeometrySource geometrySourceWithData:data
                                                semantic:SCNGeometrySourceSemanticVertex
                                             vectorCount:VERTEX_COUNT
                                         floatComponents:YES
                                     componentsPerVector:3 // x, y, z
                                       bytesPerComponent:sizeof(float)
                                              dataOffset:offsetof(MyVertex, x)
                                              dataStride:sizeof(MyVertex)];
 
normalSource = [SCNGeometrySource geometrySourceWithData:data
                                                semantic:SCNGeometrySourceSemanticNormal
                                             vectorCount:VERTEX_COUNT
                                         floatComponents:YES
                                     componentsPerVector:3 // nx, ny, nz
                                       bytesPerComponent:sizeof(float)
                                              dataOffset:offsetof(MyVertex, nx)
                                              dataStride:sizeof(MyVertex)];
 
tcoordSource = [SCNGeometrySource geometrySourceWithData:data
                                                semantic:SCNGeometrySourceSemanticTexcoord
                                             vectorCount:VERTEX_COUNT
                                         floatComponents:YES
                                     componentsPerVector:2 // s, t
                                       bytesPerComponent:sizeof(float)
                                              dataOffset:offsetof(MyVertex, s)
                                              dataStride:sizeof(MyVertex)];
```

## Topics

### Creating Geometry Sources
- [convenience init(data: Data, semantic: SCNGeometrySource.Semantic, vectorCount: Int, usesFloatComponents: Bool, componentsPerVector: Int, bytesPerComponent: Int, dataOffset: Int, dataStride: Int)](scngeometrysource/init(data:semantic:vectorcount:usesfloatcomponents:componentspervector:bytespercomponent:dataoffset:datastride:).md)
  Creates a geometry source from the specified data and options.
- [convenience init(vertices: [SCNVector3])](scngeometrysource/init(vertices:).md)
  Creates a geometry source from an array of vertex positions.
- [convenience init(normals: [SCNVector3])](scngeometrysource/init(normals:).md)
  Creates a geometry source from an array of normal vectors.
- [convenience init(textureCoordinates: [CGPoint])](scngeometrysource/init(texturecoordinates:).md)
  Creates a geometry source from an array of texture coordinate points.
### Inspecting a Geometry Source
- [var data: Data](scngeometrysource/data.md)
  The data for the geometry source.
- [var semantic: SCNGeometrySource.Semantic](scngeometrysource/semantic-swift.property.md)
  The semantic value (or attribute) the geometry source describes for each vertex.
- [var vectorCount: Int](scngeometrysource/vectorcount.md)
  The number of vectors in the data.
- [var usesFloatComponents: Bool](scngeometrysource/usesfloatcomponents.md)
  A Boolean value that indicates whether vector components are floating-point values.
- [var componentsPerVector: Int](scngeometrysource/componentspervector.md)
  The number of scalar components in each vector.
- [var bytesPerComponent: Int](scngeometrysource/bytespercomponent.md)
  The size, in bytes, of each vector component.
- [var dataOffset: Int](scngeometrysource/dataoffset.md)
  The offset, in bytes, from the beginning of the data to the first vector component to be used in the geometry source.
- [var dataStride: Int](scngeometrysource/datastride.md)
  The number of bytes from a vector to the next one in the data.
### Creating GPU-Mutable Geometry Sources
- [convenience init(buffer: any MTLBuffer, vertexFormat: MTLVertexFormat, semantic: SCNGeometrySource.Semantic, vertexCount: Int, dataOffset: Int, dataStride: Int)](scngeometrysource/init(buffer:vertexformat:semantic:vertexcount:dataoffset:datastride:).md)
  Creates a geometry source whose vertex data resides in the specified Metal buffer, allowing modification through a Metal compute shader.
### Geometry Source Semantics
- [SCNGeometrySource.Semantic](scngeometrysource/semantic-swift.struct.md)

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

## See Also

- [class SCNGeometry](scngeometry.md)
  A three-dimensional shape (also called a model or mesh) that can be displayed in a scene, with attached materials that define its appearance.
- [class SCNGeometryElement](scngeometryelement.md)
  A container for index data describing how vertices connect to define a three-dimensional object, or geometry.
- [Built-in Geometry Types](built-in-geometry-types.md)
  Basic shapes—such as spheres, boxes, and planes—and features for generating 3D objects from 2D text and Bézier curves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource)*