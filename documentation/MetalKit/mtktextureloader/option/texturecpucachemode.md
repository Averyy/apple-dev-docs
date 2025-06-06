# textureCPUCacheMode

**Framework**: MetalKit  
**Kind**: property

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

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a [`MTLCPUCacheMode`](https://developer.apple.com/documentation/Metal/MTLCPUCacheMode) value.

If this key is not specified, the default value is the value associated with [`MTLCPUCacheMode.defaultCache`](https://developer.apple.com/documentation/Metal/MTLCPUCacheMode/defaultCache).

## See Also

- [static let textureStorageMode: MTKTextureLoader.Option](mtktextureloader/option/texturestoragemode.md)
  A key used to specify the storage mode for the texture.
- [static let textureUsage: MTKTextureLoader.Option](mtktextureloader/option/textureusage.md)
  A key used to specify the intended usage of the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/option/texturecpucachemode)*