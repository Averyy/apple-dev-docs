# executeCommandsInBuffer(_:indirectBuffer:offset:)

**Framework**: Metal  
**Kind**: method

Encodes a command that runs an indirect range of commands from an indirect command buffer (ICB).

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.14+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
func executeCommandsInBuffer(_ buffer: any MTLIndirectCommandBuffer, indirectBuffer indirectRangeBuffer: any MTLBuffer, offset: Int)
```

## Parameters

- `buffer`: An   instance that contains other commands the current command runs.
- `indirectRangeBuffer`: When running on Metal devices that belong to the   GPU family, the maximum value for the   property of that structure is 0x4000 (16,384).   Metal devices that belong to an Apple silicon family, such as  , don’t have this limitation.
- `offset`: See the   to check for offset alignment requirements for buffers in   and   address space.

## See Also

- [func executeCommandsInBuffer(any MTLIndirectCommandBuffer, range: Range<Int>)](mtlrendercommandencoder/executecommandsinbuffer(_:range:).md)
  Encodes a command that runs a range of commands from an indirect command buffer (ICB).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/executecommandsinbuffer(_:indirectbuffer:offset:))*