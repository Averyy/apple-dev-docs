# componentsPerVector

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The number of scalar components in each vector.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+

## Declaration

```swift
var componentsPerVector: Int { get }
```

```objc
@property (nonatomic, assign, readonly) NSInteger componentsPerVector;
```

## Discussion

In the case that [`componentsPerVector`](./componentspervector.md) is greater than 1, the element type of the geometry-source array is itself, a sequence.

## See Also

### Getting Geometry Information
- [var count: Int](./count.md)
  The number of vectors in the buffer.
- [var format: MTLVertexFormat](./format.md)
  The type of vector data in the buffer.
- [var offset: Int](./offset.md)
  The offset, in bytes, from the beginning of the buffer.
- [var stride: Int](./stride.md)
  The length, in bytes, of the start of one vector in the buffer to the start of the next vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeometrysource/componentspervector)*