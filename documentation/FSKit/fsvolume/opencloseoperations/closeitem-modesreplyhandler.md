# closeItem(_:modes:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Closes a file from further access.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func closeItem(_ item: FSItem, modes: FSVolume.OpenModes) async throws
```

## Parameters

- `item`: The item to close.
- `modes`: The set of mode flags to keep after this close.
- `reply`: A block or closure to indicate success or failure. If closing fails, pass an error as the one parameter to the reply handler. If closing succeeds, pass `nil`. For an `async` Swift implementation, there’s no reply handler; simply throw an error or return normally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/opencloseoperations/closeitem(_:modes:replyhandler:))*