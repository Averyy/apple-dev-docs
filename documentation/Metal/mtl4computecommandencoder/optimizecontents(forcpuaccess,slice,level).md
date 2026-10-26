# optimizeContents(forCPUAccess:slice:level:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes a command that modifies the contents of a texture to improve the performance of CPU accesses to its contents in a specific region.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func optimizeContents(forCPUAccess texture: any MTLTexture, slice: Int, level: Int)
```

```objc
- (void) optimizeContentsForCPUAccess:(id<MTLTexture>) texture slice:(NSUInteger) slice level:(NSUInteger) level;
```

#### Discussion

Optimizing a texture for CPU access may affect the performance of GPU accesses, however, the data the GPU retrieves from the texture remains consistent.

You typically use this command for:

- Textures the CPU accesses for an extended period of time.
- Textures with a [`storageMode`](../mtltexturedescriptor/storagemode.md) property that’s [`MTLStorageMode.shared`](../mtlstoragemode/shared.md) or [`MTLStorageMode.managed`](../mtlstoragemode/managed.md).

## Parameters

- `texture`: A [`MTLTexture`](../mtltexture.md) the command optimizes for CPU access.
- `slice`: A slice within `texture`.
- `level`: A mipmap level within `texture`.

## See Also

### Encoding optimization commands
- [func optimizeCommands(buffer: any MTLIndirectCommandBuffer, range: Range<Int>)](./optimizecommands%28buffer,range%29.md)
  Encode a command to attempt to improve the performance of a range of commands within an indirect command buffer.
- [func optimizeContents(forCPUAccess: any MTLTexture)](./optimizecontents%28forcpuaccess%29.md)
  Encodes a command that modifies the contents of a texture to improve the performance of CPU accesses to its contents.
- [func optimizeContents(forGPUAccess: any MTLTexture)](./optimizecontents%28forgpuaccess%29.md)
  Encodes a command that modifies the contents of a texture to improve the performance of GPU accesses to its contents.
- [func optimizeContents(forGPUAccess: any MTLTexture, slice: Int, level: Int)](./optimizecontents%28forgpuaccess,slice,level%29.md)
  Encodes a command that modifies the contents of a texture instance to improve the performance of GPU accesses to its contents in a specific region.
- [- optimizeIndirectCommandBuffer:withRange:](./optimizeindirectcommandbuffer_withrange_.md)
  Encode a command to attempt to improve the performance of a range of commands within an indirect command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/optimizecontents(forcpuaccess:slice:level:))*