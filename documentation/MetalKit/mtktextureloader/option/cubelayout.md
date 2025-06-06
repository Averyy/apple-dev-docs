# cubeLayout

**Framework**: MetalKit  
**Kind**: property

A key used to specify how cube texture data is arranged in the source image.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
static let cubeLayout: MTKTextureLoader.Option
```

#### Discussion

The value for this key is one of the values listed for [`MTKTextureLoader.CubeLayout`](mtktextureloader/cubelayout.md). If this option is omitted, the texture loader does not create a cube texture.

This option cannot be used with PVR files, KTX files, or [`MDLTexture`](https://developer.apple.com/documentation/ModelIO/MDLTexture) objects, which support cube textures directly.

## See Also

- [MTKTextureLoader.CubeLayout](mtktextureloader/cubelayout.md)
  Options for specifying how cube texture data is arranged in the source image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/option/cubelayout)*