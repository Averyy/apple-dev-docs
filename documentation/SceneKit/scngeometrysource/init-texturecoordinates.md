# init(textureCoordinates:)

**Framework**: SceneKit  
**Kind**: init

Creates a geometry source from an array of texture coordinate points.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@nonobjc
convenience init(textureCoordinates: [CGPoint])
```

#### Return Value

A new geometry source whose [`semantic`](scngeometrysource/semantic-swift.property.md) property is [`texcoord`](scngeometrysource/semantic-swift.struct/texcoord.md).

#### Discussion

SceneKit converts this data to its own format to optimize rendering performance. To read the converted data, examine the properties of the created [`SCNGeometrySource`](scngeometrysource.md) object.

To create a custom [`SCNGeometry`](scngeometry.md) object from the geometry source, use the [`init(sources:elements:)`](scngeometry/init(sources:elements:).md) method.

## Parameters

- `textureCoordinates`: An array of points, each of which represents a texture coordinate pair for the geometry source.

## See Also

- [convenience init(data: Data, semantic: SCNGeometrySource.Semantic, vectorCount: Int, usesFloatComponents: Bool, componentsPerVector: Int, bytesPerComponent: Int, dataOffset: Int, dataStride: Int)](scngeometrysource/init(data:semantic:vectorcount:usesfloatcomponents:componentspervector:bytespercomponent:dataoffset:datastride:).md)
  Creates a geometry source from the specified data and options.
- [convenience init(vertices: [SCNVector3])](scngeometrysource/init(vertices:).md)
  Creates a geometry source from an array of vertex positions.
- [convenience init(normals: [SCNVector3])](scngeometrysource/init(normals:).md)
  Creates a geometry source from an array of normal vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/init(texturecoordinates:))*