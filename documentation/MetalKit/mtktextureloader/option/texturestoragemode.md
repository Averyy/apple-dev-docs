# textureStorageMode

**Framework**: MetalKit  
**Kind**: property

A key used to specify the storage mode for the texture.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
static let textureStorageMode: MTKTextureLoader.Option
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a [`MTLStorageMode`](https://developer.apple.com/documentation/Metal/MTLStorageMode) value.

If this option is omitted, the texture is created with the default storage mode for Metal textures: [`MTLStorageMode.shared`](https://developer.apple.com/documentation/Metal/MTLStorageMode/shared) on iOS and tvOS, and [`MTLStorageMode.managed`](https://developer.apple.com/documentation/Metal/MTLStorageMode/managed) in macOS. Specifying the [`MTLStorageMode.private`](https://developer.apple.com/documentation/Metal/MTLStorageMode/private) option causes the [`MTKTextureLoader`](mtktextureloader.md) object to submit work to the GPU on your behalf.

## See Also

- [static let textureCPUCacheMode: MTKTextureLoader.Option](mtktextureloader/option/texturecpucachemode.md)
  A key used to specify the CPU cache mode for the texture.
- [static let textureUsage: MTKTextureLoader.Option](mtktextureloader/option/textureusage.md)
  A key used to specify the intended usage of the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/option/texturestoragemode)*