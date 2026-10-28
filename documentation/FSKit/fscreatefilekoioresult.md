# FSCreateFileKOIOResult

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

The result of a kernel-offloaded create-file call.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class FSCreateFileKOIOResult
```

```objc
@interface FSCreateFileKOIOResult : FSCreateItemResult
```

## Overview

Use this type in your implementation of [`createFile(named:in:attributes:packer:context:replyHandler:)`](./fsvolume/kerneloffloadediohandler/createfile%28named,in,attributes,packer,context,replyhandler%29.md).

## Relationships

### Inherits From
- [FSCreateItemResult](./fscreateitemresult.md)
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
- [func lookupItem(named: FSFileName, in: FSItem, packer: FSExtentPacker, context: FSContext, replyHandler: (FSLookupItemKOIOResult?, (any Error)?) -> Void)](./fsvolume/kerneloffloadediohandler/lookupitem%28named,in,packer,context,replyhandler%29.md)
  Looks up an item within a directory and maps its disk space.
- [class FSLookupItemKOIOResult](./fslookupitemkoioresult.md)
  The result of a kernel-offloaded lookup-item call.
- [func preallocateSpace(for: FSItem, at: off_t, length: Int, flags: FSVolume.PreallocateFlags, packer: FSExtentPacker, context: FSContext, replyHandler: (FSPreallocateKOIOResult?, (any Error)?) -> Void)](./fsvolume/kerneloffloadediohandler/preallocatespace%28for,at,length,flags,packer,context,replyhandler%29.md)
  Preallocates and maps disk space for the given file.
- [FSVolume.PreallocateFlags](./fsvolume/preallocateflags.md)
  Behavior flags for preallocation operations.
- [class FSPreallocateKOIOResult](./fspreallocatekoioresult.md)
  The result of a kernel-offloaded preallocate call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscreatefilekoioresult)*