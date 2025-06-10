# primitiveRange

**Framework**: SceneKit  
**Kind**: property

The range of primitives from the geometry element to render.

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
var primitiveRange: NSRange { get set }
```

#### Discussion

The default value for this property is an [`NSRange`](https://developer.apple.com/documentation/Foundation/NSRange-c.struct) whose location is [`NSNotFound`](https://developer.apple.com/documentation/Foundation/NSNotFound-4qp9h) and length is zero, indicating that, by default, SceneKit renders the entire set of primitives specified by a geometry element’s data buffer.

You can change a geometry without redefining it by choosing to render only a subset of the primitives specified by a geometry element. To do so, set this property to a subrange of primitive indexes.

## See Also

- [var data: Data](scngeometryelement/data.md)
  The data describing the geometry element.
- [var bytesPerIndex: Int](scngeometryelement/bytesperindex.md)
  The number of bytes that represent each index value in the element’s data.
- [var primitiveType: SCNGeometryPrimitiveType](scngeometryelement/primitivetype.md)
  The drawing primitive that connects vertices when rendering the geometry element.
- [enum SCNGeometryPrimitiveType](scngeometryprimitivetype.md)
  The drawing primitive that connects vertices when rendering a geometry element, used by the [`primitiveType`](scngeometryelement/primitivetype.md) property to specify how SceneKit interprets the geometry element’s data.
- [var primitiveCount: Int](scngeometryelement/primitivecount.md)
  The number of primitives in the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometryelement/primitiverange)*