# origin

**Framework**: MetalKit  
**Kind**: property  
**Role**: Type Property

A key used to specify when to flip the pixel coordinates of the texture.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
static let origin: MTKTextureLoader.Option
```

```c
extern MTKTextureLoaderOption const MTKTextureLoaderOptionOrigin;
```

#### Discussion

The value for this key is one of the values listed for [`MTKTextureLoader.Origin`](../origin.md). If you omit this option, the texture loader doesn’t flip loaded textures.

This option cannot be used with block-compressed texture formats, and can be used only with 2D, 2D array, and cube map textures. Each mipmap level and slice of a texture are flipped.

## See Also

### Specifying Origin Information
- [MTKTextureLoader.Origin](../origin.md)
  Options for specifying when to flip the pixel coordinates of the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/option/origin)*