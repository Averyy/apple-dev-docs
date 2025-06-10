# preallocateSpace(for:at:length:flags:packer:replyHandler:)

**Framework**: FSKit  
**Kind**: method

Preallocates and maps disk space for the given file.

**Availability**:
- macOS 15.4+

## Declaration

```swift
optional func preallocateSpace(for file: FSItem, at offset: off_t, length: Int, flags: FSVolume.PreallocateFlags, packer: FSExtentPacker) async throws -> Int
```

#### Discussion

This method allows the module to opportunistically supply extents, avoiding future calls to [`blockmapFile(_:offset:length:flags:operationID:packer:replyHandler:)`](fsvolumekerneloffloadediooperations/blockmapfile(_:offset:length:flags:operationid:packer:replyhandler:).md).

> ❗ **Important**: Only implement this method if your file system conforms to [`FSVolume.PreallocateOperations`](fsvolume/preallocateoperations.md).

## Parameters

- `file`: The item for which to preallocate space.
- `offset`: The offset from which to allocate.
- `length`: The length of the space in bytes.
- `flags`: Flags that affect the preallocation behavior.
- `packer`: An extent packer you use to pack the file’s preallocated disk space.
- `reply`: A block or closure to indicate success or failure. If preallocation succeeds, pass the amount of bytes allocated and a nil error. If preallocation fails, pass the relevant error as the second parameter; FSKit ignores any byte count in this case. For an   Swift implementation, there’s no reply handler; simply return the allocated byte count or throw an error.

## See Also

- [func createFile(name: FSFileName, in: FSItem, attributes: FSItem.SetAttributesRequest, packer: FSExtentPacker, replyHandler: (FSItem?, FSFileName?, (any Error)?) -> Void)](fsvolumekerneloffloadediooperations/createfile(name:in:attributes:packer:replyhandler:).md)
  Creates a new file item and map its disk space.
- [FSItem.SetAttributesRequest](fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [func lookupItem(name: FSFileName, in: FSItem, packer: FSExtentPacker, replyHandler: (FSItem?, FSFileName?, (any Error)?) -> Void)](fsvolumekerneloffloadediooperations/lookupitem(name:in:packer:replyhandler:).md)
  Looks up an item within a directory and maps its disk space.
- [FSVolume.PreallocateFlags](fsvolume/preallocateflags.md)
  Behavior flags for preallocation operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolumekerneloffloadediooperations/preallocatespace(for:at:length:flags:packer:replyhandler:))*