# SCNGeometrySource

**Framework**: SceneKit  
**Kind**: class  
**Role**: Class

A container for vertex data forming part of the definition for a three-dimensional object, or geometry.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
class SCNGeometrySource
```

```objc
@interface SCNGeometrySource : NSObject
```

## Overview

You use geometry sources together with [`SCNGeometryElement`](./scngeometryelement.md) objects to define custom [`SCNGeometry`](./scngeometry.md) objects or to inspect the data that composes an existing geometry.

You create a custom geometry using a three-step process:

1. Create one or more [`SCNGeometrySource`](./scngeometrysource.md) objects containing vertex data. Each geometry source defines an attribute, or semantic, of the vertices it describes. You must provide at least one geometry source, using the [`vertex`](./scngeometrysource/semantic-swift.struct/vertex.md) semantic, to create a custom geometry; typically you also provide geometry sources for surface normals and texture coordinates.
2. Create at least one [`SCNGeometryElement`](./scngeometryelement.md) object, containing an array of indices identifying vertices in the geometry sources and describing the drawing primitive that SceneKit uses to connect the vertices when rendering the geometry.
3. Create an [`SCNGeometry`](./scngeometry.md) instance from the geometry sources and geometry elements.

### Interleaving Vertex Data

Because most geometries use more than one geometry source and the GPU typically uses data from multiple sources together, you can achieve better rendering performance for custom geometries by interleaving the vertex data for multiple semantics in the same array.

To do this, first create an array where each element contains values for multiple semantics for the same vertex. Next, create an [`NSData`](../Foundation/nsdata.md) object from that array, and create each geometry source from that data using the `offset` and `stride` parameters to specify where the values for each semantic can be found in the array. To make specifying the sizes and locations of vectors more convenient, you can define your own data structure for vertices and use the `sizeof` (and, in Objective-C, `offsetof`) functions, as shown in Listing 1.

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
- [convenience init(data: Data, semantic: SCNGeometrySource.Semantic, vectorCount: Int, usesFloatComponents: Bool, componentsPerVector: Int, bytesPerComponent: Int, dataOffset: Int, dataStride: Int)](./scngeometrysource/init%28data,semantic,vectorcount,usesfloatcomponents,componentspervector,bytespercomponent,dataoffset,datastride%29.md)
  Creates a geometry source from the specified data and options.
- [convenience init(vertices: [SCNVector3])](./scngeometrysource/init%28vertices%29.md)
  Creates a geometry source from an array of vertex positions.
- [convenience init(normals: [SCNVector3])](./scngeometrysource/init%28normals%29.md)
  Creates a geometry source from an array of normal vectors.
- [convenience init(textureCoordinates: [CGPoint])](./scngeometrysource/init%28texturecoordinates%29.md)
  Creates a geometry source from an array of texture coordinate points.
- [+ geometrySourceWithVertices:count:](./scngeometrysource/geometrysourcewithvertices_count_.md)
  Creates a geometry source from an array of vertex positions.
- [+ geometrySourceWithNormals:count:](./scngeometrysource/geometrysourcewithnormals_count_.md)
  Creates a geometry source from an array of normal vectors.
- [+ geometrySourceWithTextureCoordinates:count:](./scngeometrysource/geometrysourcewithtexturecoordinates_count_.md)
  Creates a geometry source from an array of texture coordinate points.
### Inspecting a Geometry Source
- [var data: Data](./scngeometrysource/data.md)
  The data for the geometry source.
- [var semantic: SCNGeometrySource.Semantic](./scngeometrysource/semantic-swift.property.md)
  The semantic value (or attribute) the geometry source describes for each vertex.
- [var vectorCount: Int](./scngeometrysource/vectorcount.md)
  The number of vectors in the data.
- [var usesFloatComponents: Bool](./scngeometrysource/usesfloatcomponents.md)
  A Boolean value that indicates whether vector components are floating-point values.
- [var componentsPerVector: Int](./scngeometrysource/componentspervector.md)
  The number of scalar components in each vector.
- [var bytesPerComponent: Int](./scngeometrysource/bytespercomponent.md)
  The size, in bytes, of each vector component.
- [var dataOffset: Int](./scngeometrysource/dataoffset.md)
  The offset, in bytes, from the beginning of the data to the first vector component to be used in the geometry source.
- [var dataStride: Int](./scngeometrysource/datastride.md)
  The number of bytes from a vector to the next one in the data.
### Creating GPU-Mutable Geometry Sources
- [convenience init(buffer: any MTLBuffer, vertexFormat: MTLVertexFormat, semantic: SCNGeometrySource.Semantic, vertexCount: Int, dataOffset: Int, dataStride: Int)](./scngeometrysource/init%28buffer,vertexformat,semantic,vertexcount,dataoffset,datastride%29.md)
  Creates a geometry source whose vertex data resides in the specified Metal buffer, allowing modification through a Metal compute shader.
### Geometry Source Semantics
- [SCNGeometrySource.Semantic](./scngeometrysource/semantic-swift.struct.md)
### Initializers
- [init?(coder: NSCoder)](./scngeometrysource/init%28coder%29.md)
- [convenience init(data: Data, semantic: SCNGeometrySource.Semantic, vectorCount: Int, floatComponents: Bool, componentsPerVector: Int, bytesPerComponent: Int, dataOffset: Int, dataStride: Int)](./scngeometrysource/init%28data,semantic,vectorcount,floatcomponents,componentspervector,bytespercomponent,dataoffset,datastride%29.md)

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

## See Also

### Geometry
- [class SCNGeometry](./scngeometry.md)
  A three-dimensional shape (also called a model or mesh) that can be displayed in a scene, with attached materials that define its appearance.
- [class SCNGeometryElement](./scngeometryelement.md)
  A container for index data describing how vertices connect to define a three-dimensional object, or geometry.
- [Built-in Geometry Types](./built-in-geometry-types.md)
  Basic shapes—such as spheres, boxes, and planes—and features for generating 3D objects from 2D text and Bézier curves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource)*