# init(data:primitiveType:primitiveCount:bytesPerIndex:)

**Framework**: SceneKit  
**Kind**: init

Creates a geometry element from the specified data and options.

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
convenience init(data: Data?, primitiveType: SCNGeometryPrimitiveType, primitiveCount: Int, bytesPerIndex: Int)
```

#### Return Value

A new geometry element object.

#### Discussion

An element’s data is an array of index values identifying vertices in a geometry source. SceneKit interprets the data as an array of unsigned integers (whose size is specified by the `bytesPerIndex` parameter), and then connects the vertices in the order specified by this array, arranged according to the `primitiveType` parameter.

To create a custom [`SCNGeometry`](scngeometry.md) object from the geometry element, use the [`init(sources:elements:)`](scngeometry/init(sources:elements:).md) method.

## Parameters

- `data`: The data describing the element.
- `primitiveType`: The drawing primitive that connects vertices when rendering the geometry element. For possible values, see  .
- `primitiveCount`: The number of primitives in the element.
- `bytesPerIndex`: The number of bytes that represent a single index value in the data.

## See Also

- [convenience init<IndexType>(indices: [IndexType], primitiveType: SCNGeometryPrimitiveType)](scngeometryelement/init(indices:primitivetype:).md)
  Creates a geometry element from the specified array of index values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometryelement/init(data:primitivetype:primitivecount:bytesperindex:))*