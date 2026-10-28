# preallocateSpace(for:at:length:flags:packer:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method

Preallocates and maps disk space for the given file.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
optional func preallocateSpace(for file: FSItem, at offset: off_t, length: Int, flags: FSVolume.PreallocateFlags, packer: FSExtentPacker, replyHandler reply: @escaping @Sendable (Int, (any Error)?) -> Void)
```

```swift
optional func preallocateSpace(for file: FSItem, at offset: off_t, length: Int, flags: FSVolume.PreallocateFlags, packer: FSExtentPacker) async throws -> Int
```

```objc
- (void) preallocateSpaceForFile:(FSItem *) file atOffset:(off_t) offset length:(size_t) length flags:(FSPreallocateFlags) flags packer:(FSExtentPacker *) packer replyHandler:(void (^)(size_t bytesAllocated, NSError *error)) reply;
```

## Discussion

This method allows the module to opportunistically supply extents, avoiding future calls to `blockmapFile(_:offset:length:flags:operationID:packer:)`.

> ❗ **Important**: Only implement this method if your file system conforms to [`FSVolume.PreallocateOperations`](../fsvolume/preallocateoperations.md).

## Parameters

- `file`: The item for which to preallocate space.
- `offset`: The offset from which to allocate.
- `length`: The length of the space in bytes.
- `flags`: Flags that affect the preallocation behavior.
- `packer`: An extent packer you use to pack the file’s preallocated disk space.
- `reply`: A block or closure to indicate success or failure. If preallocation succeeds, pass the amount of bytes allocated and a nil error. If preallocation fails, pass the relevant error as the second parameter; FSKit ignores any byte count in this case. For an `async` Swift implementation, there’s no reply handler; simply return the allocated byte count or throw an error.

## See Also

### Working with items
- [func createFile(name: FSFileName, in: FSItem, attributes: FSItem.SetAttributesRequest, packer: FSExtentPacker, replyHandler: (FSItem?, FSFileName?, (any Error)?) -> Void)](./createfile%28name,in,attributes,packer,replyhandler%29.md)
  Creates a new file item and map its disk space.
- [FSItem.SetAttributesRequest](../fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [func lookupItem(name: FSFileName, in: FSItem, packer: FSExtentPacker, replyHandler: (FSItem?, FSFileName?, (any Error)?) -> Void)](./lookupitem%28name,in,packer,replyhandler%29.md)
  Looks up an item within a directory and maps its disk space.
- [FSVolume.PreallocateFlags](../fsvolume/preallocateflags.md)
  Behavior flags for preallocation operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolumekerneloffloadediooperations/preallocatespace(for:at:length:flags:packer:replyhandler:))*