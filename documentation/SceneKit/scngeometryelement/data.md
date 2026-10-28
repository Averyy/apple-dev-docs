# data

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The data describing the geometry element.

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
var data: Data { get }
```

```objc
@property (nonatomic, readonly) NSData * data;
```

## Discussion

An element’s data is an array of index values identifying vertices in a geometry source. SceneKit interprets the data as an array of unsigned integers, whose size is specified by the [`bytesPerIndex`](./bytesperindex.md) property.

## See Also

### Working with Indexes
- [var bytesPerIndex: Int](./bytesperindex.md)
  The number of bytes that represent each index value in the element’s data.
- [var primitiveType: SCNGeometryPrimitiveType](./primitivetype.md)
  The drawing primitive that connects vertices when rendering the geometry element.
- [enum SCNGeometryPrimitiveType](../scngeometryprimitivetype.md)
  The drawing primitive that connects vertices when rendering a geometry element, used by the [`primitiveType`](./primitivetype.md) property to specify how SceneKit interprets the geometry element’s data.
- [var primitiveCount: Int](./primitivecount.md)
  The number of primitives in the element.
- [var primitiveRange: NSRange](./primitiverange.md)
  The range of primitives from the geometry element to render.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometryelement/data)*