# FSCompleteIOResult

**Framework**: FSKit  
**Kind**: class

The result of a complete-I/O call.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class FSCompleteIOResult
```

#### Overview

Use this type in your implementation of  [`completeIO(for:offset:length:status:flags:operationID:replyHandler:)`](fsvolume/kerneloffloadediohandler/completeio(for:offset:length:status:flags:operationid:replyhandler:).md)

## Topics

### Creating a complete-IO result
- [init?(itemAttributes: FSItem.Attributes)](fscompleteioresult/init(itemattributes:).md)
  Creates a result for an I/O-completion operation.
- [FSItem.Attributes](fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.
### Initializers
- [init?(attributes: FSItem.Attributes)](fscompleteioresult/init(attributes:).md)

## Relationships

### Inherits From
- [FSVolumeHandlerResult](fsvolumehandlerresult.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [func blockmapFile(FSItem, offset: off_t, length: Int, flags: FSBlockmapFlags, operationID: FSOperationID, packer: FSExtentPacker, replyHandler: (FSBlockmapResult?, (any Error)?) -> Void)](fsvolume/kerneloffloadediohandler/blockmapfile(_:offset:length:flags:operationid:packer:replyhandler:).md)
  Maps a file’s disk space into extents, allowing the kernel to perform I/O with that space.
- [struct FSBlockmapFlags](fsblockmapflags.md)
  Flags that describe the behavior of a blockmap operation.
- [class FSBlockmapResult](fsblockmapresult.md)
  The result of a blockmap call.
- [func completeIO(for: FSItem, offset: off_t, length: Int, status: any Error, flags: FSCompleteIOFlags, operationID: FSOperationID, replyHandler: (FSCompleteIOResult?, (any Error)?) -> Void)](fsvolume/kerneloffloadediohandler/completeio(for:offset:length:status:flags:operationid:replyhandler:).md)
  Completes an I/O operation for a given file.
- [struct FSCompleteIOFlags](fscompleteioflags.md)
  Flags that describe the behavior of an I/O completion operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscompleteioresult)*