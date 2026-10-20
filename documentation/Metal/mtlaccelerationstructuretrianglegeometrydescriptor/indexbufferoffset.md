# indexBufferOffset

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The offset, in bytes, to the first index in the buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var indexBufferOffset: Int { get set }
```

```objc
@property (nonatomic) NSUInteger indexBufferOffset;
```

#### Discussion

The offset needs to be a multiple of the index data type size and aligned to the index data type’s alignment. Check the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for potential alignment restrictions.

## See Also

### Configuring index data
- [var indexType: MTLIndexType](./indextype.md)
  The data type of indices in the index buffer.
- [var indexBuffer: (any MTLBuffer)?](./indexbuffer.md)
  A buffer that contains indices for the vertices that compose the triangle list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/indexbufferoffset)*