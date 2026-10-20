# openItem(_:modes:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Opens a file for access.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
func openItem(_ item: FSItem, modes: FSVolume.OpenModes, replyHandler reply: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func openItem(_ item: FSItem, modes: FSVolume.OpenModes) async throws
```

```objc
- (void) openItem:(FSItem *) item withModes:(FSVolumeOpenModes) modes replyHandler:(void (^)(NSError *error)) reply;
```

## Parameters

- `item`: The item to open.
- `modes`: The set of mode flags to open the item with.
- `reply`: A block or closure to indicate success or failure. If opening fails, pass an error as the one parameter to the reply handler. If opening succeeds, pass `nil`. For an `async` Swift implementation, there’s no reply handler; simply throw an error or return normally.

## See Also

### Opening and closing
- [func closeItem(FSItem, modes: FSVolume.OpenModes, replyHandler: ((any Error)?) -> Void)](./closeitem%28_,modes,replyhandler%29.md)
  Closes a file from further access.
- [FSVolume.OpenModes](../openmodes.md)
  Defined modes for opening a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/opencloseoperations/openitem(_:modes:replyhandler:))*