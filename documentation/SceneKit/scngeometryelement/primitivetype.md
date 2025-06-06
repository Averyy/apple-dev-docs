# primitiveType

**Framework**: SceneKit  
**Kind**: property

The drawing primitive that connects vertices when rendering the geometry element.

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
var primitiveType: SCNGeometryPrimitiveType { get }
```

#### Discussion

For possible values, see [`SCNGeometryPrimitiveType`](scngeometryprimitivetype.md).

## See Also

- [var data: Data](scngeometryelement/data.md)
  The data describing the geometry element.
- [var bytesPerIndex: Int](scngeometryelement/bytesperindex.md)
  The number of bytes that represent each index value in the element’s data.
- [enum SCNGeometryPrimitiveType](scngeometryprimitivetype.md)
  The drawing primitive that connects vertices when rendering a geometry element, used by the [`primitiveType`](scngeometryelement/primitivetype.md) property to specify how SceneKit interprets the geometry element’s data.
- [var primitiveCount: Int](scngeometryelement/primitivecount.md)
  The number of primitives in the element.
- [var primitiveRange: NSRange](scngeometryelement/primitiverange.md)
  The range of primitives from the geometry element to render.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometryelement/primitivetype)*