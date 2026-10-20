# textureCPUCacheMode

**Framework**: MetalKit  
**Kind**: property  
**Role**: Type Property

A key used to specify the CPU cache mode for the texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let textureCPUCacheMode: MTKTextureLoader.Option
```

```c
extern MTKTextureLoaderOption const MTKTextureLoaderOptionTextureCPUCacheMode;
```

#### Discussion

The value for this key is an [`NSNumber`](../../../Foundation/nsnumber.md) object containing a [`MTLCPUCacheMode`](../../../Metal/mtlcpucachemode.md) value.

If this key is not specified, the default value is the value associated with [`MTLCPUCacheMode.defaultCache`](../../../Metal/mtlcpucachemode/defaultcache.md).

## See Also

### Specifying Resource Options
- [static let textureStorageMode: MTKTextureLoader.Option](./texturestoragemode.md)
  A key used to specify the storage mode for the texture.
- [static let textureUsage: MTKTextureLoader.Option](./textureusage.md)
  A key used to specify the intended usage of the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/option/texturecpucachemode)*