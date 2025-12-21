# executeCommands(buffer:indirectBuffer:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes an instruction to execute commands from an indirect command buffer, using an indirect buffer for arguments.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func executeCommands(buffer indirectCommandbuffer: any MTLIndirectCommandBuffer, indirectBuffer indirectRangeBuffer: MTLGPUAddress)
```

#### Discussion

Use an instance of [`MTLResidencySet`](mtlresidencyset.md) to mark residency of the indirect buffer that the `indirectRangeBuffer` parameter references.

## Parameters

- `indirectCommandbuffer`:   instance containing the commands to execute.
- `indirectRangeBuffer`: GPUAddress of a   containing the execution range. Lay out the data   in this buffer as described in the    structure. This address requires 4-byte alignment.

## See Also

- [func executeCommands(buffer: any MTLIndirectCommandBuffer, range: Range<Int>)](mtl4computecommandencoder/executecommands(buffer:range:).md)
  Encodes a command to execute commands from an indirect command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/executecommands(buffer:indirectbuffer:))*