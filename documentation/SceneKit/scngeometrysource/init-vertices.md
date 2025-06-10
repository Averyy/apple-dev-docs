# init(vertices:)

**Framework**: SceneKit  
**Kind**: init

Creates a geometry source from an array of vertex positions.

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
convenience init(vertices: [SCNVector3])
```

#### Return Value

A new geometry source whose [`semantic`](scngeometrysource/semantic-swift.property.md) property is [`vertex`](scngeometrysource/semantic-swift.struct/vertex.md).

#### Discussion

SceneKit converts this data to its own format to optimize rendering performance. To read the converted data, examine the properties of the created [`SCNGeometrySource`](scngeometrysource.md) object.

To create a custom [`SCNGeometry`](scngeometry.md) object from the geometry source, use the [`init(sources:elements:)`](scngeometry/init(sources:elements:).md) method.

## Parameters

- `vertices`: An array of three-component vectors, each of which represents a vertex position for the geometry source.

## See Also

- [convenience init(data: Data, semantic: SCNGeometrySource.Semantic, vectorCount: Int, usesFloatComponents: Bool, componentsPerVector: Int, bytesPerComponent: Int, dataOffset: Int, dataStride: Int)](scngeometrysource/init(data:semantic:vectorcount:usesfloatcomponents:componentspervector:bytespercomponent:dataoffset:datastride:).md)
  Creates a geometry source from the specified data and options.
- [convenience init(normals: [SCNVector3])](scngeometrysource/init(normals:).md)
  Creates a geometry source from an array of normal vectors.
- [convenience init(textureCoordinates: [CGPoint])](scngeometrysource/init(texturecoordinates:).md)
  Creates a geometry source from an array of texture coordinate points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/init(vertices:))*