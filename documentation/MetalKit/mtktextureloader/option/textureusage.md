# textureUsage

**Framework**: MetalKit  
**Kind**: property

A key used to specify the intended usage of the texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let textureUsage: MTKTextureLoader.Option
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a [`MTLTextureUsage`](https://developer.apple.com/documentation/Metal/MTLTextureUsage) value.

If this key is not specified, the default value is determined by the default [`usage`](https://developer.apple.com/documentation/Metal/MTLTextureDescriptor/usage) value of the [`MTLTextureDescriptor`](https://developer.apple.com/documentation/Metal/MTLTextureDescriptor) class. When you create a texture, determine the specific ways in which it will be used, and set the texture usage to contain just those options. Do not set usage options that you don’t intend to use. Metal uses these flags to determine how the texture is allocated and configured; setting them correctly can significantly improve your app’s performance..

## See Also

- [static let textureCPUCacheMode: MTKTextureLoader.Option](mtktextureloader/option/texturecpucachemode.md)
  A key used to specify the CPU cache mode for the texture.
- [static let textureStorageMode: MTKTextureLoader.Option](mtktextureloader/option/texturestoragemode.md)
  A key used to specify the storage mode for the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/option/textureusage)*