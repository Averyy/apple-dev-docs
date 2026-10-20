# parent

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The parent texture used to create this texture, if any.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var parent: (any MTLTexture)? { get }
```

```objc
@property (readonly, nullable) id<MTLTexture> parentTexture;
```

#### Discussion

When this value is `nil`, an [`MTLBuffer`](../mtlbuffer.md) instance provides texture data.

## See Also

### Getting information about ancestor resources
- [var parentRelativeLevel: Int](./parentrelativelevel.md)
  The base level of the parent texture used to create this texture.
- [var parentRelativeSlice: Int](./parentrelativeslice.md)
  The base slice of the parent texture used to create this texture.
- [var buffer: (any MTLBuffer)?](./buffer.md)
  The source buffer used to create this texture, if any.
- [var bufferOffset: Int](./bufferoffset.md)
  The offset in the source buffer where the texture’s data comes from.
- [var bufferBytesPerRow: Int](./bufferbytesperrow.md)
  The number of bytes in each row of the texture’s source buffer.
- [var rootResource: (any MTLResource)?](./rootresource.md)
  The resource that owns the storage for this texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/parent)*