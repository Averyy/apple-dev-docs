# FSPreallocateKOIOResult

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

The result of a kernel-offloaded preallocate call.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class FSPreallocateKOIOResult
```

```objc
@interface FSPreallocateKOIOResult : FSPreallocateResult
```

#### Overview

Use this type in your implementation of [`preallocateSpace(for:at:length:flags:packer:context:replyHandler:)`](./fsvolume/kerneloffloadediohandler/preallocatespace%28for,at,length,flags,packer,context,replyhandler%29.md)

## Relationships

### Inherits From
- [FSPreallocateResult](./fspreallocateresult.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Working with items
- [func createFile(named: FSFileName, in: FSItem, attributes: FSItem.SetAttributesRequest, packer: FSExtentPacker, context: FSContext, replyHandler: (FSCreateFileKOIOResult?, (any Error)?) -> Void)](./fsvolume/kerneloffloadediohandler/createfile%28named,in,attributes,packer,context,replyhandler%29.md)
  Creates a new file item and map its disk space.
- [FSItem.SetAttributesRequest](./fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [class FSCreateFileKOIOResult](./fscreatefilekoioresult.md)
  The result of a kernel-offloaded create-file call.
- [func lookupItem(named: FSFileName, in: FSItem, packer: FSExtentPacker, context: FSContext, replyHandler: (FSLookupItemKOIOResult?, (any Error)?) -> Void)](./fsvolume/kerneloffloadediohandler/lookupitem%28named,in,packer,context,replyhandler%29.md)
  Looks up an item within a directory and maps its disk space.
- [class FSLookupItemKOIOResult](./fslookupitemkoioresult.md)
  The result of a kernel-offloaded lookup-item call.
- [func preallocateSpace(for: FSItem, at: off_t, length: Int, flags: FSVolume.PreallocateFlags, packer: FSExtentPacker, context: FSContext, replyHandler: (FSPreallocateKOIOResult?, (any Error)?) -> Void)](./fsvolume/kerneloffloadediohandler/preallocatespace%28for,at,length,flags,packer,context,replyhandler%29.md)
  Preallocates and maps disk space for the given file.
- [FSVolume.PreallocateFlags](./fsvolume/preallocateflags.md)
  Behavior flags for preallocation operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fspreallocatekoioresult)*