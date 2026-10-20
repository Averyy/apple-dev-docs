# element(at:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Returns the geometry element at a specified index.

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
func element(at elementIndex: Int) -> SCNGeometryElement
```

```objc
- (SCNGeometryElement *) geometryElementAtIndex:(NSInteger) elementIndex;
```

#### Return Value

A geometry element.

#### Discussion

Each [`SCNGeometryElement`](../scngeometryelement.md) object describes how vertices from the geometry’s sources are combined into polygons to create the geometry’s shape. Visible geometries contain at least one element.

## Parameters

- `elementIndex`: The index of the geometry element.

## See Also

### Related Documentation
- [convenience init(sources: [SCNGeometrySource], elements: [SCNGeometryElement]?)](./init%28sources,elements%29.md)
  Creates a new geometry built from the specified geometry sources and elements.
### Managing Geometry Data
- [var elements: [SCNGeometryElement]](./elements.md)
  An array of geometry elements that describe the geometry’s shape.
- [var sources: [SCNGeometrySource]](./sources.md)
  An array of geometry sources that provide vertex data for the geometry.
- [var elementCount: Int](./elementcount.md)
  The number of geometry elements in the geometry.
- [func sources(for: SCNGeometrySource.Semantic) -> [SCNGeometrySource]](./sources%28for%29.md)
  Returns the geometry sources for a specified semantic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/element(at:))*