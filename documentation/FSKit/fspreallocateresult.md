# FSPreallocateResult

**Framework**: FSKit  
**Kind**: class

The result of a preallocate call.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class FSPreallocateResult
```

#### Overview

Use this type in your implementation of  [`preallocateSpace(for:at:length:flags:context:replyHandler:)`](fsvolume/preallocatehandler/preallocatespace(for:at:length:flags:context:replyhandler:).md)

## Topics

### Creating a preallocate result
- [init?(bytesAllocated: Int, itemAttributes: FSItem.Attributes, freeSpace: FSFreeSpace?)](fspreallocateresult/init(bytesallocated:itemattributes:freespace:).md)
  Creates a result for a preallocate operation.
- [FSItem.Attributes](fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.
- [class FSFreeSpace](fsfreespace.md)
  A free space object that pairs free space values with atomic sequence numbers.

## Relationships

### Inherits From
- [FSVolumeHandlerResult](fsvolumehandlerresult.md)
### Inherited By
- [FSPreallocateKOIOResult](fspreallocatekoioresult.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func preallocateSpace(for: FSItem, at: off_t, length: Int, flags: FSVolume.PreallocateFlags, context: FSContext, replyHandler: (FSPreallocateResult?, (any Error)?) -> Void)](fsvolume/preallocatehandler/preallocatespace(for:at:length:flags:context:replyhandler:).md)
  Preallocates disk space for the given item.
- [FSVolume.PreallocateFlags](fsvolume/preallocateflags.md)
  Behavior flags for preallocation operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fspreallocateresult)*