# executeCommandsInBuffer(_:range:)

**Framework**: Metal  
**Kind**: method

Encodes a command that runs a range of commands from an indirect command buffer (ICB).

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst ?+
- macOS 10.14+
- tvOS 12.0+
- visionOS ?+

## Declaration

```swift
func executeCommandsInBuffer(_ buffer: any MTLIndirectCommandBuffer, range: Range<Int>)
```

## Parameters

- `buffer`: An   instance that contains other commands the current command runs.
- `range`: A span of integers that represent the command entries in   the current command runs.   When running on Metal devices that belong to the   GPU family, the number of commands needs to be less than or equal to 0x4000 (16,384).   Metal devices that belong to an Apple silicon family, such as  , don’t have this limitation.

## See Also

- [func executeCommandsInBuffer(any MTLIndirectCommandBuffer, indirectBuffer: any MTLBuffer, offset: Int)](mtlrendercommandencoder/executecommandsinbuffer(_:indirectbuffer:offset:).md)
  Encodes a command that runs an indirect range of commands from an indirect command buffer (ICB).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/executecommandsinbuffer(_:range:))*