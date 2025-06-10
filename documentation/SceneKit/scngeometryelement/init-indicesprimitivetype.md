# init(indices:primitiveType:)

**Framework**: SceneKit  
**Kind**: init

Creates a geometry element from the specified array of index values.

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
convenience init<IndexType>(indices: [IndexType], primitiveType: SCNGeometryPrimitiveType) where IndexType : FixedWidthInteger
```

#### Discussion

SceneKit connects the vertices in the order specified by the `indices` array, arranged according to the `primitiveType` parameter.This initializer is equivalent to the [`init(data:primitiveType:primitiveCount:bytesPerIndex:)`](scngeometryelement/init(data:primitivetype:primitivecount:bytesperindex:).md) initializer, but does not require an intermediary [`Data`](https://developer.apple.com/documentation/Foundation/Data) object; instead, it automatically infers the necessary allocation size and [`bytesPerIndex`](scngeometryelement/bytesperindex.md) values based on the contents of the `indices` array.

To create a custom [`SCNGeometry`](scngeometry.md) object from the geometry element, use the [`init(sources:elements:)`](scngeometry/init(sources:elements:).md) initializer.

## Parameters

- `indices`: An array of index values, each of which identifies a vertex in a geometry source.
- `primitiveType`: The drawing primitive that connects vertices when rendering the geometry element. For possible values, see  .

## See Also

- [convenience init(data: Data?, primitiveType: SCNGeometryPrimitiveType, primitiveCount: Int, bytesPerIndex: Int)](scngeometryelement/init(data:primitivetype:primitivecount:bytesperindex:).md)
  Creates a geometry element from the specified data and options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometryelement/init(indices:primitivetype:))*