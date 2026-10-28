# buffer

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

The Metal buffer backing all vertex and index data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var buffer: any MTLBuffer { get }
```

```objc
@property (nonatomic, readonly, nonnull) id<MTLBuffer> buffer;
```

## Discussion

Many [`MTKMeshBuffer`](../mtkmeshbuffer.md) objects may reference the same [`MTLBuffer`](../../Metal/mtlbuffer.md) object, in which case each [`MTKMeshBuffer`](../mtkmeshbuffer.md) object will have its own unique [`offset`](./offset.md) value.

## See Also

### Metal Buffer Properties
- [var length: Int](./length.md)
  The logical size of the Metal buffer, in bytes.
- [var offset: Int](./offset.md)
  The byte offset of the data within the Metal buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmeshbuffer/buffer)*