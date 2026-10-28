# lookupItem(named:in:packer:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Looks up an item within a directory and maps its disk space.

**Availability**:
- macOS 27.0+

## Declaration

```swift
func lookupItem(named name: FSFileName, in directory: FSItem, packer: FSExtentPacker, context: FSContext, replyHandler reply: @escaping @Sendable (FSLookupItemKOIOResult?, (any Error)?) -> Void)
```

```swift
func lookupItem(named name: FSFileName, in directory: FSItem, packer: FSExtentPacker, context: FSContext) async throws -> FSLookupItemKOIOResult
```

```objc
- (void) lookupItemNamed:(FSFileName *) name inDirectory:(FSItem *) directory packer:(FSExtentPacker *) packer context:(FSContext *) context replyHandler:(void (^)(FSLookupItemKOIOResult *result, NSError *error)) reply;
```

## Discussion

This method allows the module to opportunistically supply extents, avoiding future calls to [`blockmapFile(_:offset:length:flags:operationID:packer:replyHandler:)`](./blockmapfile%28_,offset,length,flags,operationid,packer,replyhandler%29.md). Only perform this technique opportunistically. In particular, don’t perform additional I/O to fetch extent data.

## Parameters

- `name`: The name of the file to look up.
- `directory`: The directory in which to look up the file.
- `packer`: An extent packer you use to pack the file’s allocated disk space.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If lookup succeeds, pass an instance of [`FSLookupItemKOIOResult`](../../fslookupitemkoioresult.md) containing the found [`FSItem`](../../fsitem.md) together with its [`FSFileName`](../../fsfilename.md) (as saved within the file system) and its [`FSItem.Attributes`](../../fsitem/attributes.md), along with a `nil` error. If lookup fails, pass the relevant error as the second parameter; FSKit ignores the [`FSLookupItemKOIOResult`](../../fslookupitemkoioresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

### Working with items
- [func createFile(named: FSFileName, in: FSItem, attributes: FSItem.SetAttributesRequest, packer: FSExtentPacker, context: FSContext, replyHandler: (FSCreateFileKOIOResult?, (any Error)?) -> Void)](./createfile%28named,in,attributes,packer,context,replyhandler%29.md)
  Creates a new file item and map its disk space.
- [FSItem.SetAttributesRequest](../../fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [class FSCreateFileKOIOResult](../../fscreatefilekoioresult.md)
  The result of a kernel-offloaded create-file call.
- [class FSLookupItemKOIOResult](../../fslookupitemkoioresult.md)
  The result of a kernel-offloaded lookup-item call.
- [func preallocateSpace(for: FSItem, at: off_t, length: Int, flags: FSVolume.PreallocateFlags, packer: FSExtentPacker, context: FSContext, replyHandler: (FSPreallocateKOIOResult?, (any Error)?) -> Void)](./preallocatespace%28for,at,length,flags,packer,context,replyhandler%29.md)
  Preallocates and maps disk space for the given file.
- [FSVolume.PreallocateFlags](../preallocateflags.md)
  Behavior flags for preallocation operations.
- [class FSPreallocateKOIOResult](../../fspreallocatekoioresult.md)
  The result of a kernel-offloaded preallocate call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/kerneloffloadediohandler/lookupitem(named:in:packer:context:replyhandler:))*