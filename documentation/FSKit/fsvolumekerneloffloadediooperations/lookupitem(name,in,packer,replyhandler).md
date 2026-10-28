# lookupItem(name:in:packer:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Looks up an item within a directory and maps its disk space.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
func lookupItem(name: FSFileName, in directory: FSItem, packer: FSExtentPacker, replyHandler reply: @escaping @Sendable (FSItem?, FSFileName?, (any Error)?) -> Void)
```

```swift
func lookupItem(name: FSFileName, in directory: FSItem, packer: FSExtentPacker) async throws -> (FSItem, FSFileName)
```

```objc
- (void) lookupItemNamed:(FSFileName *) name inDirectory:(FSItem *) directory packer:(FSExtentPacker *) packer replyHandler:(void (^)(FSItem *theItem, FSFileName *itemName, NSError *error)) reply;
```

## Discussion

This method allows the module to opportunistically supply extents, avoiding future calls to `blockmapFile(_:offset:length:flags:operationID:packer:)`. Only perform this technique opportunistically. In particular, don’t perform additional I/O to fetch extent data.

## Parameters

- `name`: The name of the file to look up.
- `directory`: The directory in which to look up the file.
- `packer`: An extent packer you use to pack the file’s allocated disk space.
- `reply`: A block or closure to indicate success or failure. If lookup succeeds, pass the found [`FSItem`](../fsitem.md) and its [`FSFileName`](../fsfilename.md), along with a `nil` error. If lookup fails, pass the relevant error as the third parameter; FSKit ignores any [`FSItem`](../fsitem.md) or [`FSFileName`](../fsfilename.md) in this case. For an `async` Swift implementation, there’s no reply handler; instead, return a tuple of the [`FSItem`](../fsitem.md) and its [`FSFileName`](../fsfilename.md) or throw an error.

## See Also

### Working with items
- [func createFile(name: FSFileName, in: FSItem, attributes: FSItem.SetAttributesRequest, packer: FSExtentPacker, replyHandler: (FSItem?, FSFileName?, (any Error)?) -> Void)](./createfile%28name,in,attributes,packer,replyhandler%29.md)
  Creates a new file item and map its disk space.
- [FSItem.SetAttributesRequest](../fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [func preallocateSpace(for: FSItem, at: off_t, length: Int, flags: FSVolume.PreallocateFlags, packer: FSExtentPacker, replyHandler: (Int, (any Error)?) -> Void)](./preallocatespace%28for,at,length,flags,packer,replyhandler%29.md)
  Preallocates and maps disk space for the given file.
- [FSVolume.PreallocateFlags](../fsvolume/preallocateflags.md)
  Behavior flags for preallocation operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolumekerneloffloadediooperations/lookupitem(name:in:packer:replyhandler:))*