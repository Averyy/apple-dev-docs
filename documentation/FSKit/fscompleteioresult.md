# FSCompleteIOResult

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

The result of a complete-I/O call.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class FSCompleteIOResult
```

```objc
@interface FSCompleteIOResult : FSVolumeHandlerResult
```

#### Overview

Use this type in your implementation of  [`completeIO(for:offset:length:status:flags:operationID:replyHandler:)`](./fsvolume/kerneloffloadediohandler/completeio%28for,offset,length,status,flags,operationid,replyhandler%29.md)

## Topics

### Creating a complete-IO result
- [init?(itemAttributes: FSItem.Attributes)](./fscompleteioresult/init%28itemattributes%29.md)
  Creates a result for an I/O-completion operation.
- [FSItem.Attributes](./fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.
### Initializers
- [init?(attributes: FSItem.Attributes)](./fscompleteioresult/init%28attributes%29.md)

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
- [class FSBlockmapResult](./fsblockmapresult.md)
  The result of a blockmap call.
- [func completeIO(for: FSItem, offset: off_t, length: Int, status: any Error, flags: FSCompleteIOFlags, operationID: FSOperationID, replyHandler: (FSCompleteIOResult?, (any Error)?) -> Void)](./fsvolume/kerneloffloadediohandler/completeio%28for,offset,length,status,flags,operationid,replyhandler%29.md)
  Completes an I/O operation for a given file.
- [struct FSCompleteIOFlags](./fscompleteioflags.md)
  Flags that describe the behavior of an I/O completion operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscompleteioresult)*