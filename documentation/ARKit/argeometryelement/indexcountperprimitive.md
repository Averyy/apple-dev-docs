# indexCountPerPrimitive

**Framework**: ARKit  
**Kind**: property

The number of indices for each primitive.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
var indexCountPerPrimitive: Int { get }
```

#### Discussion

The value of this property relates to the [`primitiveType`](argeometryelement/primitivetype.md). For [`ARGeometryPrimitiveType.triangle`](argeometryprimitivetype/triangle.md), the value is 3. For more information, see [`ARGeometryPrimitiveType`](argeometryprimitivetype.md).

## See Also

- [var bytesPerIndex: Int](argeometryelement/bytesperindex.md)
  The number of bytes for each index.
- [var count: Int](argeometryelement/count.md)
  The number of primitives in the buffer.
- [var primitiveType: ARGeometryPrimitiveType](argeometryelement/primitivetype.md)
  The geometry’s type of data (triangle, or line).
- [enum ARGeometryPrimitiveType](argeometryprimitivetype.md)
  The kind of connection between vertices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeometryelement/indexcountperprimitive)*