# createFile(name:in:attributes:packer:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Creates a new file item and map its disk space.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func createFile(name: FSFileName, in directory: FSItem, attributes: FSItem.SetAttributesRequest, packer: FSExtentPacker) async throws -> (FSItem, FSFileName)
```

#### Discussion

This method allows the module to opportunistically supply extents, avoiding future calls to `blockmapFile(_:offset:length:flags:operationID:packer:)`. Only perform this technique opportunistically. In particular, don’t perform additional I/O to fetch extent data.

Packing extents in this method requires that `attributes` defines a size greater than 0.

An implementation that doesn’t supply the extents can ignore the packer and call the corresponding method in the [`FSVolume.Operations`](fsvolume/operations.md) protocol, `FSVolume/Operations/createItem(named:type:inDirectory:attributes:)`.

## Parameters

- `name`: The new file’s name.
- `directory`: The directory in which to create the file.
- `attributes`: Attributes to apply to the new file.
- `packer`: An extent packer you use to pack the file’s allocated disk space.
- `reply`: A block or closure to indicate success or failure. If creation succeeds, pass the newly created [`FSItem`](fsitem.md) and its [`FSFileName`](fsfilename.md), along with a `nil` error. If creation fails, pass the relevant error as the third parameter; FSKit ignores any [`FSItem`](fsitem.md) or [`FSFileName`](fsfilename.md) in this case. For an `async` Swift implementation, there’s no reply handler; instead, return a tuple of the [`FSItem`](fsitem.md) and its [`FSFileName`](fsfilename.md) or throw an error.

## See Also

- [FSItem.SetAttributesRequest](fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [func lookupItem(name: FSFileName, in: FSItem, packer: FSExtentPacker, replyHandler: (FSItem?, FSFileName?, (any Error)?) -> Void)](fsvolumekerneloffloadediooperations/lookupitem(name:in:packer:replyhandler:).md)
  Looks up an item within a directory and maps its disk space.
- [func preallocateSpace(for: FSItem, at: off_t, length: Int, flags: FSVolume.PreallocateFlags, packer: FSExtentPacker, replyHandler: (Int, (any Error)?) -> Void)](fsvolumekerneloffloadediooperations/preallocatespace(for:at:length:flags:packer:replyhandler:).md)
  Preallocates and maps disk space for the given file.
- [FSVolume.PreallocateFlags](fsvolume/preallocateflags.md)
  Behavior flags for preallocation operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolumekerneloffloadediooperations/createfile(name:in:attributes:packer:replyhandler:))*