# optimizeContents(forGPUAccess:slice:level:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that modifies the contents of a texture instance to improve the performance of GPU accesses to its contents in a specific region.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

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

## See Also

- [func optimizeCommands(buffer: any MTLIndirectCommandBuffer, range: Range<Int>)](mtl4computecommandencoder/optimizecommands(buffer:range:).md)
  Encode a command to attempt to improve the performance of a range of commands within an indirect command buffer.
- [func optimizeContents(forCPUAccess: any MTLTexture)](mtl4computecommandencoder/optimizecontents(forcpuaccess:).md)
  Encodes a command that modifies the contents of a texture to improve the performance of CPU accesses to its contents.
- [func optimizeContents(forCPUAccess: any MTLTexture, slice: Int, level: Int)](mtl4computecommandencoder/optimizecontents(forcpuaccess:slice:level:).md)
  Encodes a command that modifies the contents of a texture to improve the performance of CPU accesses to its contents in a specific region.
- [func optimizeContents(forGPUAccess: any MTLTexture)](mtl4computecommandencoder/optimizecontents(forgpuaccess:).md)
  Encodes a command that modifies the contents of a texture to improve the performance of GPU accesses to its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/optimizecontents(forgpuaccess:slice:level:))*