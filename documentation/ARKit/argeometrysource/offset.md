# offset

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The offset, in bytes, from the beginning of the buffer.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+

## Declaration

```swift
var offset: Int { get }
```

```objc
@property (nonatomic, assign, readonly) NSInteger offset;
```

## See Also

### Getting Geometry Information
- [var componentsPerVector: Int](./componentspervector.md)
  The number of scalar components in each vector.
- [var count: Int](./count.md)
  The number of vectors in the buffer.
- [var format: MTLVertexFormat](./format.md)
  The type of vector data in the buffer.
- [var stride: Int](./stride.md)
  The length, in bytes, of the start of one vector in the buffer to the start of the next vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeometrysource/offset)*