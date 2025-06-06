# bytesPerIndex

**Framework**: SceneKit  
**Kind**: property

The number of bytes that represent each index value in the element’s data.

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
var bytesPerIndex: Int { get }
```

#### Discussion

An element’s [`data`](scngeometryelement/data.md) property holds an array of index values identifying vertices in a geometry source. SceneKit interprets the data as an array of unsigned integers, whose size is specified by the [`bytesPerIndex`](scngeometryelement/bytesperindex.md) property.

## See Also

- [var data: Data](scngeometryelement/data.md)
  The data describing the geometry element.
- [var primitiveType: SCNGeometryPrimitiveType](scngeometryelement/primitivetype.md)
  The drawing primitive that connects vertices when rendering the geometry element.
- [enum SCNGeometryPrimitiveType](scngeometryprimitivetype.md)
  The drawing primitive that connects vertices when rendering a geometry element, used by the [`primitiveType`](scngeometryelement/primitivetype.md) property to specify how SceneKit interprets the geometry element’s data.
- [var primitiveCount: Int](scngeometryelement/primitivecount.md)
  The number of primitives in the element.
- [var primitiveRange: NSRange](scngeometryelement/primitiverange.md)
  The range of primitives from the geometry element to render.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometryelement/bytesperindex)*