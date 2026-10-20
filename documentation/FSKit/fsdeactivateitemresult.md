# FSDeactivateItemResult

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

The result of a deactivate-item call.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class FSDeactivateItemResult
```

```objc
@interface FSDeactivateItemResult : FSVolumeHandlerResult
```

#### Overview

Use this type in your implementation of [`deactivateItem(_:context:replyHandler:)`](./fsvolume/itemdeactivationhandler/deactivateitem%28_,context,replyhandler%29.md)

## Topics

### Creating a deactive-item result
- [init?(freeSpace: FSFreeSpace?)](./fsdeactivateitemresult/init%28freespace%29.md)
  Creates a result for an item-deactivation operation.
- [class FSFreeSpace](./fsfreespace.md)
  A free space object that pairs free space values with atomic sequence numbers.

## Relationships

### Inherits From
- [FSVolumeHandlerResult](./fsvolumehandlerresult.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Deactivating an item
- [func deactivateItem(FSItem, context: FSContext, replyHandler: (FSDeactivateItemResult?, (any Error)?) -> Void)](./fsvolume/itemdeactivationhandler/deactivateitem%28_,context,replyhandler%29.md)
  Notifies the file system that the kernel is no longer making immediate use of the given item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsdeactivateitemresult)*