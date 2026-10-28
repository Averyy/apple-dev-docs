# rootResource

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The resource that owns the storage for this texture.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.11+ - Deprecated in 10.12
- tvOS - Deprecated in 10.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`parent`](./parent.md) or [`buffer`](./buffer.md) instead.

## Declaration

```swift
var rootResource: (any MTLResource)? { get }
```

```objc
@property (readonly, nullable) id<MTLResource> rootResource;
```

## Discussion

If the value is `nil`, then this texture image owns its own data. Otherwise, this value is the [`MTLResource`](../mtlresource.md) instance used to create the texture. For example, it might be a texture that uses the contents of an [`MTLBuffer`](../mtlbuffer.md) object or a texture view that reinterprets the contents of another [`MTLTexture`](../mtltexture.md).

## See Also

### Getting information about ancestor resources
- [var parent: (any MTLTexture)?](./parent.md)
  The parent texture used to create this texture, if any.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/rootresource)*