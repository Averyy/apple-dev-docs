# primitiveType

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The geometry’s type of data (triangle, or line).

**Availability**:
- iOS 13.4+
- iPadOS 13.4+

## Declaration

```swift
var primitiveType: ARGeometryPrimitiveType { get }
```

```objc
@property (nonatomic, assign, readonly) ARGeometryPrimitiveType primitiveType;
```

## See Also

### Getting Index Information
- [var bytesPerIndex: Int](./bytesperindex.md)
  The number of bytes for each index.
- [var count: Int](./count.md)
  The number of primitives in the buffer.
- [var indexCountPerPrimitive: Int](./indexcountperprimitive.md)
  The number of indices for each primitive.
- [enum ARGeometryPrimitiveType](../argeometryprimitivetype.md)
  The kind of connection between vertices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeometryelement/primitivetype)*