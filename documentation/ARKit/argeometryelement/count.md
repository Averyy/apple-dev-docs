# count

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The number of primitives in the buffer.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+

## Declaration

```swift
var count: Int { get }
```

```objc
@property (nonatomic, assign, readonly) NSInteger count;
```

## See Also

### Getting Index Information
- [var bytesPerIndex: Int](./bytesperindex.md)
  The number of bytes for each index.
- [var indexCountPerPrimitive: Int](./indexcountperprimitive.md)
  The number of indices for each primitive.
- [var primitiveType: ARGeometryPrimitiveType](./primitivetype.md)
  The geometry’s type of data (triangle, or line).
- [enum ARGeometryPrimitiveType](../argeometryprimitivetype.md)
  The kind of connection between vertices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeometryelement/count)*