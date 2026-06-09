# closeItem(_:modes:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Closes a file from further access.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func closeItem(_ item: FSItem, modes: FSVolume.OpenModes, context: FSContext) async throws
```

## Parameters

- `item`: The item to close.
- `modes`: The set of mode flags to keep after this close.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If closing fails, pass an error as the one parameter to the reply handler. If closing succeeds, pass `nil`. For an `async` Swift implementation, there’s no reply handler; simply throw an error or return normally.

## See Also

- [func openItem(FSItem, modes: FSVolume.OpenModes, context: FSContext, replyHandler: ((any Error)?) -> Void)](fsvolume/openclosehandler/openitem(_:modes:context:replyhandler:).md)
  Opens a file for access.
- [FSVolume.OpenModes](fsvolume/openmodes.md)
  Defined modes for opening a file.
- [class FSContext](fscontext.md)
  A context object that provides information about the initiator of a file system operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/openclosehandler/closeitem(_:modes:context:replyhandler:))*