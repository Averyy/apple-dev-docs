# optimizeCommands(buffer:range:)

**Framework**: Metal  
**Kind**: method

Encode a command to attempt to improve the performance of a range of commands within an indirect command buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func optimizeCommands(buffer: any MTLIndirectCommandBuffer, range: Range<Int>)
```

## Parameters

- `buffer`: An   instance that this command optimizes.
- `range`: A range of commands within  .

## See Also

- [func optimizeContents(forCPUAccess: any MTLTexture)](mtl4computecommandencoder/optimizecontents(forcpuaccess:).md)
  Encodes a command that modifies the contents of a texture to improve the performance of CPU accesses to its contents.
- [func optimizeContents(forCPUAccess: any MTLTexture, slice: Int, level: Int)](mtl4computecommandencoder/optimizecontents(forcpuaccess:slice:level:).md)
  Encodes a command that modifies the contents of a texture to improve the performance of CPU accesses to its contents in a specific region.
- [func optimizeContents(forGPUAccess: any MTLTexture)](mtl4computecommandencoder/optimizecontents(forgpuaccess:).md)
  Encodes a command that modifies the contents of a texture to improve the performance of GPU accesses to its contents.
- [func optimizeContents(forGPUAccess: any MTLTexture, slice: Int, level: Int)](mtl4computecommandencoder/optimizecontents(forgpuaccess:slice:level:).md)
  Encodes a command that modifies the contents of a texture instance to improve the performance of GPU accesses to its contents in a specific region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/optimizecommands(buffer:range:))*