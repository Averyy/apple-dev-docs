# executeCommands(buffer:indirectBuffer:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes an instruction to execute commands from an indirect command buffer, using an indirect buffer for arguments.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func executeCommands(buffer indirectCommandbuffer: any MTLIndirectCommandBuffer, indirectBuffer indirectRangeBuffer: UInt64)
```

#### Discussion

Use an instance of [`MTLResidencySet`](mtlresidencyset.md) to mark residency of the indirect buffer that the `indirectRangeBuffer` parameter references.

## Parameters

- `indirectCommandbuffer`:   instance containing the commands to execute.
- `indirectRangeBuffer`: GPUAddress of a   containing the execution range. Lay out the data   in this buffer as described in the    structure. The maximum length of the range is 16384 commands. This address   requires 4-byte alignment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/executecommands(buffer:indirectbuffer:))*