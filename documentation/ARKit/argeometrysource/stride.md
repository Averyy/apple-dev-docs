# stride

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The length, in bytes, of the start of one vector in the buffer to the start of the next vector.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+

## Declaration

```swift
var stride: Int { get }
```

```objc
@property (nonatomic, assign, readonly) NSInteger stride;
```

## Discussion

Stride may contain padding, so it’s not always equal to the vector-format’s total size in bytes.

## See Also

### Getting Geometry Information
- [var componentsPerVector: Int](./componentspervector.md)
  The number of scalar components in each vector.
- [var count: Int](./count.md)
  The number of vectors in the buffer.
- [var format: MTLVertexFormat](./format.md)
  The type of vector data in the buffer.
- [var offset: Int](./offset.md)
  The offset, in bytes, from the beginning of the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeometrysource/stride)*