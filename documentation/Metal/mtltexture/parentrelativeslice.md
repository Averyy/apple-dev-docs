# parentRelativeSlice

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The base slice of the parent texture used to create this texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var parentRelativeSlice: Int { get }
```

#### Discussion

This property is only valid for textures created from a [`parent`](mtltexture/parent.md) texture. The default value is `0`.

## See Also

- [var parent: (any MTLTexture)?](mtltexture/parent.md)
  The parent texture used to create this texture, if any.
- [var parentRelativeLevel: Int](mtltexture/parentrelativelevel.md)
  The base level of the parent texture used to create this texture.
- [var buffer: (any MTLBuffer)?](mtltexture/buffer.md)
  The source buffer used to create this texture, if any.
- [var bufferOffset: Int](mtltexture/bufferoffset.md)
  The offset in the source buffer where the texture’s data comes from.
- [var bufferBytesPerRow: Int](mtltexture/bufferbytesperrow.md)
  The number of bytes in each row of the texture’s source buffer.
- [var rootResource: (any MTLResource)?](mtltexture/rootresource.md)
  The resource that owns the storage for this texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/parentrelativeslice)*