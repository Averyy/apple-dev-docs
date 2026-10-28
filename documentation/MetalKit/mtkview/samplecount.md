# sampleCount

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

The sample count used to generate the [`multisampleColorTexture`](./multisamplecolortexture.md) object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var sampleCount: Int { get set }
```

```objc
@property (nonatomic) NSUInteger sampleCount;
```

## Discussion

Support for different sample count values varies by device object. Call the [`supportsTextureSampleCount(_:)`](../../Metal/mtldevice/supportstexturesamplecount%28_%29.md) method to determine if the device object supports the sample count you want.

The default value is `1`. When you set a value greater than `1`, the view creates and configures an intermediate set of multisample textures. The pixel format is the same as the one specified for the drawable; see [`colorPixelFormat`](./colorpixelformat.md). When the view creates a render pass descriptor, the render pass uses those intermediate textures as the color render targets, with a store action to resolve these multisample textures into the drawable’s texture ([`MTLStoreAction.multisampleResolve`](../../Metal/mtlstoreaction/multisampleresolve.md)).

## See Also

### Configuring Multisampling
- [var multisampleColorAttachmentTextureUsage: MTLTextureUsage](./multisamplecolorattachmenttextureusage.md)
  The texture usage characteristics that the view uses when creating multisample textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/samplecount)*