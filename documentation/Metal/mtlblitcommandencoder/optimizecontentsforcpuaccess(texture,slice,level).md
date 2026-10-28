# optimizeContentsForCPUAccess(texture:slice:level:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes a command that improves the performance of CPU memory operations with a specific portion of a texture.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func optimizeContentsForCPUAccess(texture: any MTLTexture, slice: Int, level: Int)
```

```objc
- (void) optimizeContentsForCPUAccess:(id<MTLTexture>) texture slice:(NSUInteger) slice level:(NSUInteger) level;
```

## Mentions

- [Optimizing texture data](../optimizing-texture-data.md)

## Discussion

This command can reduce the time it takes the CPU to access a texture. Apps typically run the command for:

- Textures the CPU accesses for an extended period of time
- Textures with a [`storageMode`](../mtlresource/storagemode.md) property that’s [`MTLStorageMode.shared`](../mtlstoragemode/shared.md) or [`MTLStorageMode.managed`](../mtlstoragemode/managed.md)

When a blit pass runs this command, the GPU only applies lossless changes to the texture’s underlying data.

> **Note**:  Optimizing a texture for the CPU may affect the performance of GPU memory operations, but the data the GPU retrieves from the texture remains consistent.

## Parameters

- `texture`: A texture the command optimizes.
- `slice`: A slice within `texture`.
- `level`: A mipmap level within `texture`.

## See Also

### Optimizing textures for CPU access
- [func optimizeContentsForCPUAccess(texture: any MTLTexture)](./optimizecontentsforcpuaccess%28texture%29.md)
  Encodes a command that improves the performance of CPU memory operations with a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/optimizecontentsforcpuaccess(texture:slice:level:))*