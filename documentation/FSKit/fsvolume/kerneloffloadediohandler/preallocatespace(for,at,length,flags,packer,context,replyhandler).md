# preallocateSpace(for:at:length:flags:packer:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method

Preallocates and maps disk space for the given file.

**Availability**:
- macOS 27.0+

## Declaration

```swift
optional func preallocateSpace(for file: FSItem, at offset: off_t, length: Int, flags: FSVolume.PreallocateFlags, packer: FSExtentPacker, context: FSContext, replyHandler reply: @escaping @Sendable (FSPreallocateKOIOResult?, (any Error)?) -> Void)
```

```swift
optional func preallocateSpace(for file: FSItem, at offset: off_t, length: Int, flags: FSVolume.PreallocateFlags, packer: FSExtentPacker, context: FSContext) async throws -> FSPreallocateKOIOResult
```

```objc
- (void) preallocateSpaceForFile:(FSItem *) file atOffset:(off_t) offset length:(size_t) length flags:(FSPreallocateFlags) flags packer:(FSExtentPacker *) packer context:(FSContext *) context replyHandler:(void (^)(FSPreallocateKOIOResult *result, NSError *error)) reply;
```

## Discussion

This method allows the module to opportunistically supply extents, avoiding future calls to [`blockmapFile(_:offset:length:flags:operationID:packer:replyHandler:)`](./blockmapfile%28_,offset,length,flags,operationid,packer,replyhandler%29.md).

> ❗ **Important**: Only implement this method if your file system conforms to [`FSVolume.PreallocateHandler`](../preallocatehandler.md).

## Parameters

- `file`: The item for which to preallocate space.
- `offset`: The offset from which to allocate.
- `length`: The length of the space in bytes.
- `flags`: Flags that affect the preallocation behavior.
- `packer`: An extent packer you use to pack the file’s preallocated disk space.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If preallocation succeeds, pass an instance of [`FSPreallocateKOIOResult`](../../fspreallocatekoioresult.md) containing the amount of bytes allocated, the updated [`FSItem.Attributes`](../../fsitem/attributes.md) of the file, the volume’s update free space, along with a `nil` error. If preallocation fails, pass the relevant error as the second parameter; FSKit ignores the [`FSPreallocateKOIOResult`](../../fspreallocatekoioresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

### Working with items
- [func createFile(named: FSFileName, in: FSItem, attributes: FSItem.SetAttributesRequest, packer: FSExtentPacker, context: FSContext, replyHandler: (FSCreateFileKOIOResult?, (any Error)?) -> Void)](./createfile%28named,in,attributes,packer,context,replyhandler%29.md)
  Creates a new file item and map its disk space.
- [FSItem.SetAttributesRequest](../../fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [class FSCreateFileKOIOResult](../../fscreatefilekoioresult.md)
  The result of a kernel-offloaded create-file call.
- [func lookupItem(named: FSFileName, in: FSItem, packer: FSExtentPacker, context: FSContext, replyHandler: (FSLookupItemKOIOResult?, (any Error)?) -> Void)](./lookupitem%28named,in,packer,context,replyhandler%29.md)
  Looks up an item within a directory and maps its disk space.
- [class FSLookupItemKOIOResult](../../fslookupitemkoioresult.md)
  The result of a kernel-offloaded lookup-item call.
- [FSVolume.PreallocateFlags](../preallocateflags.md)
  Behavior flags for preallocation operations.
- [class FSPreallocateKOIOResult](../../fspreallocatekoioresult.md)
  The result of a kernel-offloaded preallocate call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/kerneloffloadediohandler/preallocatespace(for:at:length:flags:packer:context:replyhandler:))*