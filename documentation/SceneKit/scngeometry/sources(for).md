# sources(for:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Returns the geometry sources for a specified semantic.

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
func sources(for semantic: SCNGeometrySource.Semantic) -> [SCNGeometrySource]
```

```objc
- (NSArray<SCNGeometrySource *> *) geometrySourcesForSemantic:(SCNGeometrySourceSemantic) semantic;
```

## Return Value

An array of [`SCNGeometrySource`](../scngeometrysource.md) objects, or `nil` if the geometry has no source for the specified semantic.

## Discussion

Each [`SCNGeometrySource`](../scngeometrysource.md) object describes an attribute of all vertices in the geometry (such as vertex position, surface normal vector, color, or texture mapping coordinates) identified by the source’s [`semantic`](../scngeometrysource/semantic-swift.property.md) property. A geometry always has at least one source, for the [`vertex`](../scngeometrysource/semantic-swift.struct/vertex.md) semantic, typically has additional sources for use in lighting and shading, and may have other sources for skeletal animation or surface subdivision information.

The vertex, normal, and color semantics each refer to at most one source. A geometry may have multiple sources for the [`texcoord`](../scngeometrysource/semantic-swift.struct/texcoord.md) semantic—in this case, indices in the returned array correspond to values for the [`mappingChannel`](../scnmaterialproperty/mappingchannel.md) property used when attaching textures to materials.

## Parameters

- `semantic`: A constant identifying a semantic for which to return geometry sources. See Geometry Semantic Identifiers for possible values.

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
- [func element(at: Int) -> SCNGeometryElement](./element%28at%29.md)
  Returns the geometry element at a specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/sources(for:))*