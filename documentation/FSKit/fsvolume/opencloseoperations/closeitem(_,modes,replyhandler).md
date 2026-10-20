# closeItem(_:modes:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Closes a file from further access.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
func closeItem(_ item: FSItem, modes: FSVolume.OpenModes, replyHandler reply: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func closeItem(_ item: FSItem, modes: FSVolume.OpenModes) async throws
```

```objc
- (void) closeItem:(FSItem *) item keepingModes:(FSVolumeOpenModes) modes replyHandler:(void (^)(NSError *error)) reply;
```

## Parameters

- `item`: The item to close.
- `modes`: The set of mode flags to keep after this close.
- `reply`: A block or closure to indicate success or failure. If closing fails, pass an error as the one parameter to the reply handler. If closing succeeds, pass `nil`. For an `async` Swift implementation, there’s no reply handler; simply throw an error or return normally.

## See Also

### Opening and closing
- [func openItem(FSItem, modes: FSVolume.OpenModes, replyHandler: ((any Error)?) -> Void)](./openitem%28_,modes,replyhandler%29.md)
  Opens a file for access.
- [FSVolume.OpenModes](../openmodes.md)
  Defined modes for opening a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/opencloseoperations/closeitem(_:modes:replyhandler:))*