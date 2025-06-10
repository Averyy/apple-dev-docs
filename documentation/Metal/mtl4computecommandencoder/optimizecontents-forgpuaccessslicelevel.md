# optimizeContents(forGPUAccess:slice:level:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that modifies the contents of a texture instance to improve the performance of GPU accesses to its contents in a specific region.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func optimizeContents(forGPUAccess texture: any MTLTexture, slice: Int, level: Int)
```

#### Discussion

Optimizing a texture for GPU access may affect the performance of CPU accesses, however, the data the CPU retrieves from the texture remains consistent.

You typically run this command for:

- Textures the GPU accesses for an extended period of time.
- Textures with a [`storageMode`](mtltexturedescriptor/storagemode.md) property that’s [`MTLStorageMode.shared`](mtlstoragemode/shared.md) or [`MTLStorageMode.managed`](mtlstoragemode/managed.md).

## Parameters

- `texture`: A   the command optimizes for GPU access.
- `slice`: A slice within  .
- `level`: A mipmap level within  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/optimizecontents(forgpuaccess:slice:level:))*