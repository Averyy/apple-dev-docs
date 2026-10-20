# parentRelativeSlice

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
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

```objc
@property (readonly) NSUInteger parentRelativeSlice;
```

#### Discussion

This property is only valid for textures created from a [`parent`](./parent.md) texture. The default value is `0`.

## See Also

### Getting information about ancestor resources
- [var parent: (any MTLTexture)?](./parent.md)
  The parent texture used to create this texture, if any.
- [var parentRelativeLevel: Int](./parentrelativelevel.md)
  The base level of the parent texture used to create this texture.
- [var buffer: (any MTLBuffer)?](./buffer.md)
  The source buffer used to create this texture, if any.
- [var bufferOffset: Int](./bufferoffset.md)
  The offset in the source buffer where the texture’s data comes from.
- [var bufferBytesPerRow: Int](./bufferbytesperrow.md)
  The number of bytes in each row of the texture’s source buffer.
- [var rootResource: (any MTLResource)?](./rootresource.md)
  The resource that owns the storage for this texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/parentrelativeslice)*