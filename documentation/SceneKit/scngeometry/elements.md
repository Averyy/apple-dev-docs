# elements

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

An array of geometry elements that describe the geometry’s shape.

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
var elements: [SCNGeometryElement] { get }
```

```objc
@property (nonatomic, readonly) NSArray<SCNGeometryElement *> * geometryElements;
```

## Discussion

Each [`SCNGeometryElement`](../scngeometryelement.md) object describes how vertices from the geometry’s sources are combined into polygons to create the geometry’s shape. Visible geometries contain at least one element.

For geometries with multiple elements, you can use the [`materials`](./materials.md) property to attach different materials to each element.

## See Also

### Managing Geometry Data
- [var sources: [SCNGeometrySource]](./sources.md)
  An array of geometry sources that provide vertex data for the geometry.
- [var elementCount: Int](./elementcount.md)
  The number of geometry elements in the geometry.
- [func element(at: Int) -> SCNGeometryElement](./element%28at%29.md)
  Returns the geometry element at a specified index.
- [func sources(for: SCNGeometrySource.Semantic) -> [SCNGeometrySource]](./sources%28for%29.md)
  Returns the geometry sources for a specified semantic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/elements)*