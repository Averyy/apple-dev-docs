# openItem(_:modes:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Opens a file for access.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func openItem(_ item: FSItem, modes: FSVolume.OpenModes) async throws
```

## Parameters

- `item`: The item to open.
- `modes`: The set of mode flags to open the item with.
- `reply`: A block or closure to indicate success or failure. If opening fails, pass an error as the one parameter to the reply handler. If opening succeeds, pass  . For an   Swift implementation, there’s no reply handler; simply throw an error or return normally.

## See Also

- [func closeItem(FSItem, modes: FSVolume.OpenModes, replyHandler: ((any Error)?) -> Void)](fsvolume/opencloseoperations/closeitem(_:modes:replyhandler:).md)
  Closes a file from further access.
- [FSVolume.OpenModes](fsvolume/openmodes.md)
  Defined modes for opening a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/opencloseoperations/openitem(_:modes:replyhandler:))*