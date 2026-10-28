# primitiveType

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The drawing primitive that connects vertices when rendering the geometry element.

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
var primitiveType: SCNGeometryPrimitiveType { get }
```

```objc
@property (nonatomic, readonly) SCNGeometryPrimitiveType primitiveType;
```

## Discussion

For possible values, see [`SCNGeometryPrimitiveType`](../scngeometryprimitivetype.md).

## See Also

### Working with Indexes
- [var data: Data](./data.md)
  The data describing the geometry element.
- [var bytesPerIndex: Int](./bytesperindex.md)
  The number of bytes that represent each index value in the element’s data.
- [enum SCNGeometryPrimitiveType](../scngeometryprimitivetype.md)
  The drawing primitive that connects vertices when rendering a geometry element, used by the [`primitiveType`](./primitivetype.md) property to specify how SceneKit interprets the geometry element’s data.
- [var primitiveCount: Int](./primitivecount.md)
  The number of primitives in the element.
- [var primitiveRange: NSRange](./primitiverange.md)
  The range of primitives from the geometry element to render.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometryelement/primitivetype)*