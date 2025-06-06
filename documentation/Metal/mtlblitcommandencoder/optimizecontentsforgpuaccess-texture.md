# optimizeContentsForGPUAccess(texture:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that improves the performance of the GPU’s accesses to a texture.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func optimizeContentsForGPUAccess(texture: any MTLTexture)
```

## Mentions

- [Optimizing Texture Data](optimizing-texture-data.md)

#### Discussion

This command can reduce the time it takes the GPU to access a texture. Apps typically run the command for:

- Textures the GPU accesses for an extended period of time
- Textures with a [`storageMode`](mtlresource/storagemode.md) property that’s [`MTLStorageMode.shared`](mtlstoragemode/shared.md) or [`MTLStorageMode.managed`](mtlstoragemode/managed.md)

When a blit pass runs this command, the GPU only applies lossless changes to the texture’s underlying data.

> **Note**:  Optimizing a texture for the GPU may affect the performance of the CPU’s accesses, but the data the CPU retrieves from the texture remains consistent.

 Optimizing a texture for the GPU may affect the performance of the CPU’s accesses, but the data the CPU retrieves from the texture remains consistent.

## Parameters

- `texture`: A texture the command optimizes.

## See Also

- [func optimizeContentsForGPUAccess(texture: any MTLTexture, slice: Int, level: Int)](mtlblitcommandencoder/optimizecontentsforgpuaccess(texture:slice:level:).md)
  Encodes a command that improves the performance of the GPU’s accesses to a specific portion of a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/optimizecontentsforgpuaccess(texture:))*