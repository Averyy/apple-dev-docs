# optimizeContents(forCPUAccess:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that modifies the contents of a texture to improve the performance of CPU accesses to its contents.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func optimizeContents(forCPUAccess texture: any MTLTexture)
```

#### Discussion

Optimizing a texture for CPU access may affect the performance of GPU accesses, however, the data the GPU retrieves from the texture remains consistent.

You typically use this command for:

- Textures the CPU accesses for an extended period of time.
- Textures with a [`storageMode`](mtltexturedescriptor/storagemode.md) property that’s [`MTLStorageMode.shared`](mtlstoragemode/shared.md) or [`MTLStorageMode.managed`](mtlstoragemode/managed.md).

## Parameters

- `texture`: A   instance the command optimizes for CPU access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/optimizecontents(forcpuaccess:))*