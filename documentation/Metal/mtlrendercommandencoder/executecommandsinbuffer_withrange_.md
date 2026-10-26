# executeCommandsInBuffer:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes a command that runs a range of commands from an indirect command buffer (ICB).

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```objc
- (void) executeCommandsInBuffer:(id<MTLIndirectCommandBuffer>) indirectCommandBuffer withRange:(NSRange) executionRange;
```

## Parameters

- `indirectCommandBuffer`: An [`MTLIndirectCommandBuffer`](../mtlindirectcommandbuffer.md) instance that contains other commands the current command runs.
- `executionRange`: A span of integers that represent the command entries in `buffer` the current command runs. The number of commands needs to be less than or equal to `0x4000` (`16,384`).

## See Also

### Running commands from indirect command buffers
- [- executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:](./executecommandsinbuffer_indirectbuffer_indirectbufferoffset_.md)
  Encodes a command that runs an indirect range of commands from an indirect command buffer (ICB).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/executecommandsinbuffer:withrange:)*