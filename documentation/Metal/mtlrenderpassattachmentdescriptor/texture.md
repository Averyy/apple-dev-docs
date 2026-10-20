# texture

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The texture object associated with this attachment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var texture: (any MTLTexture)? { get set }
```

```objc
@property (nonatomic, strong, nullable) id<MTLTexture> texture;
```

## Mentions

- [Setting load and store actions](../setting-load-and-store-actions.md)
- [Choosing a resource storage mode for Apple GPUs](../choosing-a-resource-storage-mode-for-apple-gpus.md)

#### Discussion

You need to set the attachment’s `texture` property, choosing an appropriate pixel format for the texture.

- To store color values in an attachment, use a texture with a color-renderable pixel format.
- To store depth values, use a texture with a depth-renderable pixel format, such as [`MTLPixelFormat.depth32Float`](../mtlpixelformat/depth32float.md).
- To store stencil values, use a texture with a stencil-renderable pixel format, such as [`MTLPixelFormat.stencil8`](../mtlpixelformat/stencil8.md).

## See Also

### Related Documentation
- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
### Specifying the texture for the attachment
- [var level: Int](./level.md)
  The mipmap level of the texture used for rendering to the attachment.
- [var slice: Int](./slice.md)
  The slice of the texture used for rendering to the attachment.
- [var depthPlane: Int](./depthplane.md)
  The depth plane of the texture used for rendering to the attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/texture)*