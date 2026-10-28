# init(normals:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Creates a geometry source from an array of normal vectors.

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
@nonobjc
convenience init(normals: [SCNVector3])
```

## Return Value

A new geometry source whose [`semantic`](./semantic-swift.property.md) property is [`normal`](./semantic-swift.struct/normal.md).

## Discussion

SceneKit converts this data to its own format to optimize rendering performance. To read the converted data, examine the properties of the created [`SCNGeometrySource`](../scngeometrysource.md) object.

To create a custom [`SCNGeometry`](../scngeometry.md) object from the geometry source, use the [`init(sources:elements:)`](../scngeometry/init%28sources,elements%29.md) method.

## Parameters

- `normals`: An array of three-component vectors, each of which represents a surface normal for the geometry source.

## See Also

### Creating Geometry Sources
- [convenience init(data: Data, semantic: SCNGeometrySource.Semantic, vectorCount: Int, usesFloatComponents: Bool, componentsPerVector: Int, bytesPerComponent: Int, dataOffset: Int, dataStride: Int)](./init%28data,semantic,vectorcount,usesfloatcomponents,componentspervector,bytespercomponent,dataoffset,datastride%29.md)
  Creates a geometry source from the specified data and options.
- [convenience init(vertices: [SCNVector3])](./init%28vertices%29.md)
  Creates a geometry source from an array of vertex positions.
- [convenience init(textureCoordinates: [CGPoint])](./init%28texturecoordinates%29.md)
  Creates a geometry source from an array of texture coordinate points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/init(normals:))*