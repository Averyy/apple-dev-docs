# primitiveCount

**Framework**: SceneKit  
**Kind**: property

The number of primitives in the element.

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
var primitiveCount: Int { get }
```

## See Also

- [var data: Data](scngeometryelement/data.md)
  The data describing the geometry element.
- [var bytesPerIndex: Int](scngeometryelement/bytesperindex.md)
  The number of bytes that represent each index value in the element’s data.
- [var primitiveType: SCNGeometryPrimitiveType](scngeometryelement/primitivetype.md)
  The drawing primitive that connects vertices when rendering the geometry element.
- [enum SCNGeometryPrimitiveType](scngeometryprimitivetype.md)
  The drawing primitive that connects vertices when rendering a geometry element, used by the [`primitiveType`](scngeometryelement/primitivetype.md) property to specify how SceneKit interprets the geometry element’s data.
- [var primitiveRange: NSRange](scngeometryelement/primitiverange.md)
  The range of primitives from the geometry element to render.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometryelement/primitivecount)*