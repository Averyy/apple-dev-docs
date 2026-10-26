# executeCommandsInBuffer:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes a command that runs a range of commands from an indirect command buffer.

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

#### Discussion

Use this method to encode the execution of a range of Metal render commands in the GPU timeline.

> **Note**: If the `indirectCommandBuffer` parameter references any pipeline state objects, you are responsible for adding them to a [`MTLResidencySet`](../mtlresidencyset.md) instance in use when you commit the command buffer.
>
> An indirect render command references a pipeline state when you pass it as an argument to the command’s [`setRenderPipelineState(_:)`](../mtlindirectrendercommand/setrenderpipelinestate%28_%29.md) method during CPU encoding, or `set_render_pipeline_state()` during GPU encoding.

## Parameters

- `indirectCommandBuffer`: A [`MTLIndirectCommandBuffer`](../mtlindirectcommandbuffer.md) instance containing other commands that the current command runs.
- `executionRange`: A span of integers that represent the command entries in the buffer that the current command runs.

## See Also

### Running commands from indirect command buffers
- [func executeCommands(buffer: any MTLIndirectCommandBuffer, indirectBuffer: MTLGPUAddress)](./executecommands%28buffer,indirectbuffer%29.md)
  Encodes a command that runs an indirect range of commands from an indirect command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/executecommandsinbuffer:withrange:)*