# MTKTextureLoader.Option

**Framework**: MetalKit  
**Kind**: struct  
**Role**: Structure

Keys and values used to specify loading options.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct Option
```

```c
typedef NSString * MTKTextureLoaderOption;
```

## Topics

### Creating Texture Loading Options
- [init(rawValue: String)](./option/init%28rawvalue%29.md)
  Creates a texture loader option from a raw string value.
### Specifying Mipmap Options
- [static let allocateMipmaps: MTKTextureLoader.Option](./option/allocatemipmaps.md)
  A key used to specify whether the texture loader should allocate memory for mipmaps in the texture.
- [static let generateMipmaps: MTKTextureLoader.Option](./option/generatemipmaps.md)
  A key used to specify whether the texture loader should generate mipmaps for the texture.
### Specifying Resource Options
- [static let textureCPUCacheMode: MTKTextureLoader.Option](./option/texturecpucachemode.md)
  A key used to specify the CPU cache mode for the texture.
- [static let textureStorageMode: MTKTextureLoader.Option](./option/texturestoragemode.md)
  A key used to specify the storage mode for the texture.
- [static let textureUsage: MTKTextureLoader.Option](./option/textureusage.md)
  A key used to specify the intended usage of the texture.
### Specifying Origin Information
- [static let origin: MTKTextureLoader.Option](./option/origin.md)
  A key used to specify when to flip the pixel coordinates of the texture.
- [MTKTextureLoader.Origin](./origin.md)
  Options for specifying when to flip the pixel coordinates of the texture.
### Specifying Cube Layout
- [static let cubeLayout: MTKTextureLoader.Option](./option/cubelayout.md)
  A key used to specify how cube texture data is arranged in the source image.
- [MTKTextureLoader.CubeLayout](./cubelayout.md)
  Options for specifying how cube texture data is arranged in the source image.
### Specifying sRGB Options
- [static let SRGB: MTKTextureLoader.Option](./option/srgb.md)
  A key used to specify whether the texture data is stored as sRGB image data.
### Type Properties
- [static let loadAsArray: MTKTextureLoader.Option](./option/loadasarray.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/option)*