# geometrySourceWithTextureCoordinates:count:

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates a geometry source from an array of texture coordinate points.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```objc
+ (instancetype) geometrySourceWithTextureCoordinates:(const CGPoint *) texcoord count:(NSInteger) count;
```

## Return Value

A new geometry source whose [`SCNGeometrySource`](../scngeometrysource.md) property is [`texcoord`](./semantic-swift.struct/texcoord.md).

## Discussion

SceneKit converts this data to its own format to optimize rendering performance. To read the converted data, examine the properties of the created [`SCNGeometrySource`](../scngeometrysource.md) object.

To create a custom [`SCNGeometry`](../scngeometry.md) object from the geometry source, use the [`init(sources:elements:)`](../scngeometry/init%28sources,elements%29.md) method.

## Parameters

- `texcoord`: An array of points, each of which represents a texture coordinate pair for the geometry source.
- `count`: The number of texture coordinate points.

## See Also

### Creating Geometry Sources
- [convenience init(data: Data, semantic: SCNGeometrySource.Semantic, vectorCount: Int, usesFloatComponents: Bool, componentsPerVector: Int, bytesPerComponent: Int, dataOffset: Int, dataStride: Int)](./init%28data,semantic,vectorcount,usesfloatcomponents,componentspervector,bytespercomponent,dataoffset,datastride%29.md)
  Creates a geometry source from the specified data and options.
- [+ geometrySourceWithVertices:count:](./geometrysourcewithvertices_count_.md)
  Creates a geometry source from an array of vertex positions.
- [+ geometrySourceWithNormals:count:](./geometrysourcewithnormals_count_.md)
  Creates a geometry source from an array of normal vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/geometrysourcewithtexturecoordinates:count:)*