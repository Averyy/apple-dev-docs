# FSDeactivateItemResult

**Framework**: FSKit  
**Kind**: class

The result of a deactivate-item call.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class FSDeactivateItemResult
```

#### Overview

Use this type in your implementation of [`deactivateItem(_:context:replyHandler:)`](fsvolume/itemdeactivationhandler/deactivateitem(_:context:replyhandler:).md)

## Topics

### Creating a deactive-item result
- [init?(freeSpace: FSFreeSpace?)](fsdeactivateitemresult/init(freespace:).md)
  Creates a result for an item-deactivation operation.
- [class FSFreeSpace](fsfreespace.md)
  A free space object that pairs free space values with atomic sequence numbers.

## Relationships

### Inherits From
- [FSVolumeHandlerResult](fsvolumehandlerresult.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func deactivateItem(FSItem, context: FSContext, replyHandler: (FSDeactivateItemResult?, (any Error)?) -> Void)](fsvolume/itemdeactivationhandler/deactivateitem(_:context:replyhandler:).md)
  Notifies the file system that the kernel is no longer making immediate use of the given item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsdeactivateitemresult)*