# preallocateSpace(for:at:length:flags:packer:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method

Preallocates and maps disk space for the given file.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
optional func preallocateSpace(for file: FSItem, at offset: off_t, length: Int, flags: FSVolume.PreallocateFlags, packer: FSExtentPacker, context: FSContext) async throws -> FSPreallocateKOIOResult
```

#### Discussion

This method allows the module to opportunistically supply extents, avoiding future calls to [`blockmapFile(_:offset:length:flags:operationID:packer:replyHandler:)`](fsvolume/kerneloffloadediohandler/blockmapfile(_:offset:length:flags:operationid:packer:replyhandler:).md).

> ❗ **Important**: Only implement this method if your file system conforms to [`FSVolume.PreallocateHandler`](fsvolume/preallocatehandler.md).

## Parameters

- `file`: The item for which to preallocate space.
- `offset`: The offset from which to allocate.
- `length`: The length of the space in bytes.
- `flags`: Flags that affect the preallocation behavior.
- `packer`: An extent packer you use to pack the file’s preallocated disk space.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If preallocation succeeds, pass an instance of [`FSPreallocateKOIOResult`](fspreallocatekoioresult.md) containing the amount of bytes allocated, the updated [`FSItem.Attributes`](fsitem/attributes.md) of the file, the volume’s update free space, along with a `nil` error. If preallocation fails, pass the relevant error as the second parameter; FSKit ignores the [`FSPreallocateKOIOResult`](fspreallocatekoioresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

- [func createFile(named: FSFileName, in: FSItem, attributes: FSItem.SetAttributesRequest, packer: FSExtentPacker, context: FSContext, replyHandler: (FSCreateFileKOIOResult?, (any Error)?) -> Void)](fsvolume/kerneloffloadediohandler/createfile(named:in:attributes:packer:context:replyhandler:).md)
  Creates a new file item and map its disk space.
- [FSItem.SetAttributesRequest](fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [class FSCreateFileKOIOResult](fscreatefilekoioresult.md)
  The result of a kernel-offloaded create-file call.
- [func lookupItem(named: FSFileName, in: FSItem, packer: FSExtentPacker, context: FSContext, replyHandler: (FSLookupItemKOIOResult?, (any Error)?) -> Void)](fsvolume/kerneloffloadediohandler/lookupitem(named:in:packer:context:replyhandler:).md)
  Looks up an item within a directory and maps its disk space.
- [class FSLookupItemKOIOResult](fslookupitemkoioresult.md)
  The result of a kernel-offloaded lookup-item call.
- [FSVolume.PreallocateFlags](fsvolume/preallocateflags.md)
  Behavior flags for preallocation operations.
- [class FSPreallocateKOIOResult](fspreallocatekoioresult.md)
  The result of a kernel-offloaded preallocate call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/kerneloffloadediohandler/preallocatespace(for:at:length:flags:packer:context:replyhandler:))*