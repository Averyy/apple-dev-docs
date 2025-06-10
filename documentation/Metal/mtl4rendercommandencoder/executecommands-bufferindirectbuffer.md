# executeCommands(buffer:indirectBuffer:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that runs an indirect range of commands from an indirect command buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func executeCommands(buffer indirectCommandBuffer: any MTLIndirectCommandBuffer, indirectBuffer indirectRangeBuffer: UInt64)
```

#### Discussion

Use this method to indicate to Metal the span of indices in the command buffer to execute indirectly via an [`MTLBuffer`](mtlbuffer.md) instance you provide in the `indirectRangeBuffer` parameter. This allows you to calculate the span of commands Metal executes in the GPU timeline, enabling GPU-driven workflows.

Metal requires that the contents of this buffer match the layout of struct [`MTLIndirectCommandBufferExecutionRange`](mtlindirectcommandbufferexecutionrange.md), which specifies a location and a length within the indirect command buffer. You are responsible for ensuring the address of this buffer has 4-byte alignment, and that the length member in the buffer contents doesn’t exceed `16,384`.

Use an instance of [`MTLResidencySet`](mtlresidencyset.md) to mark residency of the indirect buffer that the `indirectRangeBuffer` parameter references.

## Parameters

- `indirectCommandBuffer`: A   instance that contains other commands   the current command runs.
- `indirectRangeBuffer`: GPUAddress of a   instance with data that matches the layout of the    structure. You are responsible for ensuring the   length property of the structure in the contents of this buffer is less than or equal to   16,384. Additionally, this address requires 4-byte alignment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/executecommands(buffer:indirectbuffer:))*