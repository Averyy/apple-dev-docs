# optimizeContents(forGPUAccess:slice:level:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) optimizeContentsForGPUAccess:(id<MTLTexture>) texture slice:(NSUInteger) slice level:(NSUInteger) level;
```

#### Discussion

Optimizing a texture for GPU access may affect the performance of CPU accesses, however, the data the CPU retrieves from the texture remains consistent.

You typically run this command for:

- Textures the GPU accesses for an extended period of time.
- Textures with a [`storageMode`](../mtltexturedescriptor/storagemode.md) property that’s [`MTLStorageMode.shared`](../mtlstoragemode/shared.md) or [`MTLStorageMode.managed`](../mtlstoragemode/managed.md).

## Parameters

- `texture`: A [`MTLTexture`](../mtltexture.md) the command optimizes for GPU access.
- `slice`: A slice within `texture`.
- `level`: A mipmap level within `texture`.

## See Also

### Encoding optimization commands
- [func optimizeCommands(buffer: any MTLIndirectCommandBuffer, range: Range<Int>)](./optimizecommands%28buffer,range%29.md)
  Encode a command to attempt to improve the performance of a range of commands within an indirect command buffer.
- [func optimizeContents(forCPUAccess: any MTLTexture)](./optimizecontents%28forcpuaccess%29.md)
  Encodes a command that modifies the contents of a texture to improve the performance of CPU accesses to its contents.
- [func optimizeContents(forCPUAccess: any MTLTexture, slice: Int, level: Int)](./optimizecontents%28forcpuaccess,slice,level%29.md)
  Encodes a command that modifies the contents of a texture to improve the performance of CPU accesses to its contents in a specific region.
- [func optimizeContents(forGPUAccess: any MTLTexture)](./optimizecontents%28forgpuaccess%29.md)
  Encodes a command that modifies the contents of a texture to improve the performance of GPU accesses to its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/optimizecontents(forgpuaccess:slice:level:))*