# lookupItem(name:in:packer:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Looks up an item within a directory and maps its disk space.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func lookupItem(name: FSFileName, in directory: FSItem, packer: FSExtentPacker) async throws -> (FSItem, FSFileName)
```

#### Discussion

This method allows the module to opportunistically supply extents, avoiding future calls to [`blockmapFile(_:offset:length:flags:operationID:packer:replyHandler:)`](fsvolumekerneloffloadediooperations/blockmapfile(_:offset:length:flags:operationid:packer:replyhandler:).md). Only perform this technique opportunistically. In particular, don’t perform additional I/O to fetch extent data.

## Parameters

- `name`: The name of the file to look up.
- `directory`: The directory in which to look up the file.
- `packer`: An extent packer you use to pack the file’s allocated disk space.
- `reply`: A block or closure to indicate success or failure. If lookup succeeds, pass the found   and its  , along with a   error. If lookup fails, pass the relevant error as the third parameter; FSKit ignores any   or   in this case. For an   Swift implementation, there’s no reply handler; instead, return a tuple of the   and its   or throw an error.

## See Also

- [func createFile(name: FSFileName, in: FSItem, attributes: FSItem.SetAttributesRequest, packer: FSExtentPacker, replyHandler: (FSItem?, FSFileName?, (any Error)?) -> Void)](fsvolumekerneloffloadediooperations/createfile(name:in:attributes:packer:replyhandler:).md)
  Creates a new file item and map its disk space.
- [FSItem.SetAttributesRequest](fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [func preallocateSpace(for: FSItem, at: off_t, length: Int, flags: FSVolume.PreallocateFlags, packer: FSExtentPacker, replyHandler: (Int, (any Error)?) -> Void)](fsvolumekerneloffloadediooperations/preallocatespace(for:at:length:flags:packer:replyhandler:).md)
  Preallocates and maps disk space for the given file.
- [FSVolume.PreallocateFlags](fsvolume/preallocateflags.md)
  Behavior flags for preallocation operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolumekerneloffloadediooperations/lookupitem(name:in:packer:replyhandler:))*