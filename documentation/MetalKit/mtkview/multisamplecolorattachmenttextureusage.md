# multisampleColorAttachmentTextureUsage

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

The texture usage characteristics that the view uses when creating multisample textures.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var multisampleColorAttachmentTextureUsage: MTLTextureUsage { get set }
```

```objc
@property (nonatomic) MTLTextureUsage multisampleColorAttachmentTextureUsage;
```

## Discussion

The default value is [`renderTarget`](../../Metal/mtltextureusage/rendertarget.md).

## See Also

### Configuring Multisampling
- [var sampleCount: Int](./samplecount.md)
  The sample count used to generate the [`multisampleColorTexture`](./multisamplecolortexture.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/multisamplecolorattachmenttextureusage)*