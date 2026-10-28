# textureStorageMode

**Framework**: MetalKit  
**Kind**: property  
**Role**: Type Property

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

```c
extern MTKTextureLoaderOption const MTKTextureLoaderOptionTextureStorageMode;
```

## Discussion

The value for this key is an [`NSNumber`](../../../Foundation/nsnumber.md) object containing a [`MTLStorageMode`](../../../Metal/mtlstoragemode.md) value.

If this option is omitted, the texture is created with the default storage mode for Metal textures: [`MTLStorageMode.shared`](../../../Metal/mtlstoragemode/shared.md) on iOS and tvOS, and [`MTLStorageMode.managed`](../../../Metal/mtlstoragemode/managed.md) in macOS. Specifying the [`MTLStorageMode.private`](../../../Metal/mtlstoragemode/private.md) option causes the [`MTKTextureLoader`](../../mtktextureloader.md) object to submit work to the GPU on your behalf.

## See Also

### Specifying Resource Options
- [static let textureCPUCacheMode: MTKTextureLoader.Option](./texturecpucachemode.md)
  A key used to specify the CPU cache mode for the texture.
- [static let textureUsage: MTKTextureLoader.Option](./textureusage.md)
  A key used to specify the intended usage of the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/option/texturestoragemode)*