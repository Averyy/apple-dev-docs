# init(indices:primitiveType:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Creates a geometry element from the specified array of index values.

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
convenience init<IndexType>(indices: [IndexType], primitiveType: SCNGeometryPrimitiveType) where IndexType : FixedWidthInteger
```

#### Discussion

SceneKit connects the vertices in the order specified by the `indices` array, arranged according to the `primitiveType` parameter.This initializer is equivalent to the [`init(data:primitiveType:primitiveCount:bytesPerIndex:)`](./init%28data,primitivetype,primitivecount,bytesperindex%29.md) initializer, but does not require an intermediary [`Data`](../../Foundation/data.md) object; instead, it automatically infers the necessary allocation size and [`bytesPerIndex`](./bytesperindex.md) values based on the contents of the `indices` array.

To create a custom [`SCNGeometry`](../scngeometry.md) object from the geometry element, use the [`init(sources:elements:)`](../scngeometry/init%28sources,elements%29.md) initializer.

## Parameters

- `indices`: An array of index values, each of which identifies a vertex in a geometry source.
- `primitiveType`: The drawing primitive that connects vertices when rendering the geometry element. For possible values, see [`SCNGeometryPrimitiveType`](../scngeometryprimitivetype.md).

## See Also

### Creating a Geometry Element
- [convenience init(data: Data?, primitiveType: SCNGeometryPrimitiveType, primitiveCount: Int, bytesPerIndex: Int)](./init%28data,primitivetype,primitivecount,bytesperindex%29.md)
  Creates a geometry element from the specified data and options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometryelement/init(indices:primitivetype:))*