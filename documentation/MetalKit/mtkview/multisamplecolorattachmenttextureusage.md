# multisampleColorAttachmentTextureUsage

**Framework**: MetalKit  
**Kind**: property

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
@MainActor
var multisampleColorAttachmentTextureUsage: MTLTextureUsage { get set }
```

#### Discussion

The default value is [`renderTarget`](https://developer.apple.com/documentation/Metal/MTLTextureUsage/renderTarget).

## See Also

- [var sampleCount: Int](mtkview/samplecount.md)
  The sample count used to generate the [`multisampleColorTexture`](mtkview/multisamplecolortexture.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/multisamplecolorattachmenttextureusage)*