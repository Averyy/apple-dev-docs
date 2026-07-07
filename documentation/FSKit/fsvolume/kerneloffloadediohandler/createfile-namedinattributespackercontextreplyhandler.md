# createFile(named:in:attributes:packer:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Creates a new file item and map its disk space.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func createFile(named name: FSFileName, in directory: FSItem, attributes newAttributes: FSItem.SetAttributesRequest, packer: FSExtentPacker, context: FSContext) async throws -> FSCreateFileKOIOResult
```

#### Discussion

This method allows the module to opportunistically supply extents, avoiding future calls to [`blockmapFile(_:offset:length:flags:operationID:packer:replyHandler:)`](fsvolume/kerneloffloadediohandler/blockmapfile(_:offset:length:flags:operationid:packer:replyhandler:).md). Only perform this technique opportunistically. In particular, don’t perform additional I/O to fetch extent data.

Packing extents in this method requires that `attributes` defines a size greater than 0.

An implementation that doesn’t supply the extents can ignore the packer and call the corresponding method in the [`FSVolume.Handler`](fsvolume/handler.md) protocol, [`createItem(named:type:in:attributes:context:replyHandler:)`](fsvolume/handler/createitem(named:type:in:attributes:context:replyhandler:).md).

## Parameters

- `name`: The new file’s name.
- `directory`: The directory in which to create the file.
- `newAttributes`: Attributes to apply to the new file.
- `packer`: An extent packer you use to pack the file’s allocated disk space.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If creation succeeds, pass an instance of [`FSCreateFileKOIOResult`](fscreatefilekoioresult.md) containing the newly-created [`FSItem`](fsitem.md), its [`FSFileName`](fsfilename.md), its [`FSItem.Attributes`](fsitem/attributes.md), the updated [`FSItem.Attributes`](fsitem/attributes.md) of the parent directory, the volume’s update free space, along with a `nil` error. If creation fails, pass the relevant error as the second parameter; FSKit ignores the [`FSCreateFileKOIOResult`](fscreatefilekoioresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

- [FSItem.SetAttributesRequest](fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [class FSCreateFileKOIOResult](fscreatefilekoioresult.md)
  The result of a kernel-offloaded create-file call.
- [func lookupItem(named: FSFileName, in: FSItem, packer: FSExtentPacker, context: FSContext, replyHandler: (FSLookupItemKOIOResult?, (any Error)?) -> Void)](fsvolume/kerneloffloadediohandler/lookupitem(named:in:packer:context:replyhandler:).md)
  Looks up an item within a directory and maps its disk space.
- [class FSLookupItemKOIOResult](fslookupitemkoioresult.md)
  The result of a kernel-offloaded lookup-item call.
- [func preallocateSpace(for: FSItem, at: off_t, length: Int, flags: FSVolume.PreallocateFlags, packer: FSExtentPacker, context: FSContext, replyHandler: (FSPreallocateKOIOResult?, (any Error)?) -> Void)](fsvolume/kerneloffloadediohandler/preallocatespace(for:at:length:flags:packer:context:replyhandler:).md)
  Preallocates and maps disk space for the given file.
- [FSVolume.PreallocateFlags](fsvolume/preallocateflags.md)
  Behavior flags for preallocation operations.
- [class FSPreallocateKOIOResult](fspreallocatekoioresult.md)
  The result of a kernel-offloaded preallocate call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/kerneloffloadediohandler/createfile(named:in:attributes:packer:context:replyhandler:))*