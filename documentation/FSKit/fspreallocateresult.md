# FSPreallocateResult

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

The result of a preallocate call.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class FSPreallocateResult
```

```objc
@interface FSPreallocateResult : FSVolumeHandlerResult
```

#### Overview

Use this type in your implementation of  [`preallocateSpace(for:at:length:flags:context:replyHandler:)`](./fsvolume/preallocatehandler/preallocatespace%28for,at,length,flags,context,replyhandler%29.md)

## Topics

### Creating a preallocate result
- [init?(bytesAllocated: Int, itemAttributes: FSItem.Attributes, freeSpace: FSFreeSpace?)](./fspreallocateresult/init%28bytesallocated,itemattributes,freespace%29.md)
  Creates a result for a preallocate operation.
- [FSItem.Attributes](./fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.
- [class FSFreeSpace](./fsfreespace.md)
  A free space object that pairs free space values with atomic sequence numbers.

## Relationships

### Inherits From
- [FSVolumeHandlerResult](./fsvolumehandlerresult.md)
### Inherited By
- [FSPreallocateKOIOResult](./fspreallocatekoioresult.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Preallocating space
- [func preallocateSpace(for: FSItem, at: off_t, length: Int, flags: FSVolume.PreallocateFlags, context: FSContext, replyHandler: (FSPreallocateResult?, (any Error)?) -> Void)](./fsvolume/preallocatehandler/preallocatespace%28for,at,length,flags,context,replyhandler%29.md)
  Preallocates disk space for the given item.
- [FSVolume.PreallocateFlags](./fsvolume/preallocateflags.md)
  Behavior flags for preallocation operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fspreallocateresult)*