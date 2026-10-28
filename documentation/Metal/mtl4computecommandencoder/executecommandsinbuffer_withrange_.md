# executeCommandsInBuffer:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes a command to execute a series of commands from an indirect command buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) executeCommandsInBuffer:(id<MTLIndirectCommandBuffer>) indirectCommandBuffer withRange:(NSRange) executionRange;
```

## Discussion

Use this method to encode the execution of a range of Metal compute commands in the GPU timeline.

> **Note**: If the `indirectCommandBuffer` parameter references any pipeline state objects, you are responsible for adding them to a [`MTLResidencySet`](../mtlresidencyset.md) instance in use when you commit the command buffer.
>
> An indirect compute command references a pipeline state when you pass it as an argument to the command’s [`setComputePipelineState(_:)`](../mtlindirectcomputecommand/setcomputepipelinestate%28_%29.md) method during CPU encoding, or `set_compute_pipeline_state()` during GPU encoding.

## Parameters

- `indirectCommandBuffer`: [`MTLIndirectCommandBuffer`](../mtlindirectcommandbuffer.md) instance containing the commands to execute.
- `executionRange`: The range of commands to execute.

## See Also

### Encoding indirect command buffers
- [func executeCommands(buffer: any MTLIndirectCommandBuffer, indirectBuffer: MTLGPUAddress)](./executecommands%28buffer,indirectbuffer%29.md)
  Encodes an instruction to execute commands from an indirect command buffer, using an indirect buffer for arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/executecommandsinbuffer:withrange:)*