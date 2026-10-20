# openItem(_:modes:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Opens a file for access.

**Availability**:
- macOS 27.0+

## Declaration

```swift
func openItem(_ item: FSItem, modes: FSVolume.OpenModes, context: FSContext, replyHandler reply: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func openItem(_ item: FSItem, modes: FSVolume.OpenModes, context: FSContext) async throws
```

```objc
- (void) openItem:(FSItem *) item withModes:(FSVolumeOpenModes) modes context:(FSContext *) context replyHandler:(void (^)(NSError *error)) reply;
```

## Parameters

- `item`: The item to open.
- `modes`: The set of mode flags to open the item with.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If opening fails, pass an error as the one parameter to the reply handler. If opening succeeds, pass `nil`. For an `async` Swift implementation, there’s no reply handler; simply throw an error or return normally.

## See Also

### Opening and closing
- [func closeItem(FSItem, modes: FSVolume.OpenModes, context: FSContext, replyHandler: ((any Error)?) -> Void)](./closeitem%28_,modes,context,replyhandler%29.md)
  Closes a file from further access.
- [FSVolume.OpenModes](../openmodes.md)
  Defined modes for opening a file.
- [class FSContext](../../fscontext.md)
  A context object that provides information about the initiator of a file system operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/openclosehandler/openitem(_:modes:context:replyhandler:))*