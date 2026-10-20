# closeItem(_:modes:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Closes a file from further access.

**Availability**:
- macOS 27.0+

## Declaration

```swift
func closeItem(_ item: FSItem, modes: FSVolume.OpenModes, context: FSContext, replyHandler reply: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func closeItem(_ item: FSItem, modes: FSVolume.OpenModes, context: FSContext) async throws
```

```objc
- (void) closeItem:(FSItem *) item keepingModes:(FSVolumeOpenModes) modes context:(FSContext *) context replyHandler:(void (^)(NSError *error)) reply;
```

## Parameters

- `item`: The item to close.
- `modes`: The set of mode flags to keep after this close.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If closing fails, pass an error as the one parameter to the reply handler. If closing succeeds, pass `nil`. For an `async` Swift implementation, there’s no reply handler; simply throw an error or return normally.

## See Also

### Opening and closing
- [func openItem(FSItem, modes: FSVolume.OpenModes, context: FSContext, replyHandler: ((any Error)?) -> Void)](./openitem%28_,modes,context,replyhandler%29.md)
  Opens a file for access.
- [FSVolume.OpenModes](../openmodes.md)
  Defined modes for opening a file.
- [class FSContext](../../fscontext.md)
  A context object that provides information about the initiator of a file system operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/openclosehandler/closeitem(_:modes:context:replyhandler:))*