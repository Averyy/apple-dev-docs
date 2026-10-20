# FSBlockmapResult

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

The result of a blockmap call.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class FSBlockmapResult
```

```objc
@interface FSBlockmapResult : FSVolumeHandlerResult
```

#### Overview

Use this type in your implementation of [`blockmapFile(_:offset:length:flags:operationID:packer:replyHandler:)`](./fsvolume/kerneloffloadediohandler/blockmapfile%28_,offset,length,flags,operationid,packer,replyhandler%29.md).

## Topics

### Creating a blockmap result
- [init?(freeSpace: FSFreeSpace?)](./fsblockmapresult/init%28freespace%29.md)
  Creates a result for a blockmap operation.
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

### Performing mapped I/O
- [func blockmapFile(FSItem, offset: off_t, length: Int, flags: FSBlockmapFlags, operationID: FSOperationID, packer: FSExtentPacker, replyHandler: (FSBlockmapResult?, (any Error)?) -> Void)](./fsvolume/kerneloffloadediohandler/blockmapfile%28_,offset,length,flags,operationid,packer,replyhandler%29.md)
  Maps a file’s disk space into extents, allowing the kernel to perform I/O with that space.
- [struct FSBlockmapFlags](./fsblockmapflags.md)
  Flags that describe the behavior of a blockmap operation.
- [func completeIO(for: FSItem, offset: off_t, length: Int, status: any Error, flags: FSCompleteIOFlags, operationID: FSOperationID, replyHandler: (FSCompleteIOResult?, (any Error)?) -> Void)](./fsvolume/kerneloffloadediohandler/completeio%28for,offset,length,status,flags,operationid,replyhandler%29.md)
  Completes an I/O operation for a given file.
- [struct FSCompleteIOFlags](./fscompleteioflags.md)
  Flags that describe the behavior of an I/O completion operation.
- [class FSCompleteIOResult](./fscompleteioresult.md)
  The result of a complete-I/O call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockmapresult)*