# subscript(_:)

**Framework**: ARKit  
**Kind**: subscript

Provides an array of vertex indices that respresents the geometric primitive at the subscripted index.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
@nonobjc
subscript(index: Int) -> [Int32] { get }
```

#### Discussion

This subscript operates on geometry elements of type [`Int32`](https://developer.apple.com/documentation/Swift/Int32) with `4` [`bytesPerIndex`](argeometryelement/bytesperindex.md). In the case of the [`faces`](armeshgeometry/faces.md) property, this operator returns an array of size `3`. The contents of the array are vertex indices that compose a triangle primitive, which represents the face identified by the argument face index.

## See Also

- [var buffer: any MTLBuffer](argeometryelement/buffer.md)
  A Metal buffer containing primitive data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeometryelement/subscript(_:))*