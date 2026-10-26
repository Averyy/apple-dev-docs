# optimizeIndirectCommandBuffer:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes a command that can improve the performance of a range of commands within an indirect command buffer.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```objc
- (void) optimizeIndirectCommandBuffer:(id<MTLIndirectCommandBuffer>) indirectCommandBuffer withRange:(NSRange) range;
```

#### Discussion

This command can reduce the time it takes the GPU to run the commands within an indirect command buffer by removing its redundancies. For example, an indirect command buffer may have empty commands or commands that duplicate identical state. Redundancies like these can come from multiple compute functions that encode commands in parallel, which can sometimes reset commands or configure identical states multiple times.

> ❗ **Important**:  You can only run optimized commands by using the entire range. Otherwise, starting or ending within an optimized range may result in unexpected behavior.

You can’t run any commands that start or end at an index within that range, or that cross into another optimized range. However, you can reuse the range you optimize by resetting it and then encoding new commands to it.

## Parameters

- `indirectCommandBuffer`: An indirect command buffer the command optimizes.
- `range`: A range of commands within `indirectCommandBuffer`.

## See Also

### Managing indirect command buffers
- [- copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:](./copyindirectcommandbuffer_sourcerange_destination_destinationindex_.md)
  Encodes a command that copies commands from one indirect command buffer into another.
- [- resetCommandsInBuffer:withRange:](./resetcommandsinbuffer_withrange_.md)
  Encodes a command that resets a range of commands in an indirect command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/optimizeindirectcommandbuffer:withrange:)*