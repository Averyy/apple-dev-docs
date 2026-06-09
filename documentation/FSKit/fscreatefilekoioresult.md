# FSCreateFileKOIOResult

**Framework**: FSKit  
**Kind**: class

The result of a kernel-offloaded create-file call.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class FSCreateFileKOIOResult
```

#### Overview

Use this type in your implementation of [`createFile(named:in:attributes:packer:context:replyHandler:)`](fsvolume/kerneloffloadediohandler/createfile(named:in:attributes:packer:context:replyhandler:).md).

## Relationships

### Inherits From
- [FSCreateItemResult](fscreateitemresult.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func createFile(named: FSFileName, in: FSItem, attributes: FSItem.SetAttributesRequest, packer: FSExtentPacker, context: FSContext, replyHandler: (FSCreateFileKOIOResult?, (any Error)?) -> Void)](fsvolume/kerneloffloadediohandler/createfile(named:in:attributes:packer:context:replyhandler:).md)
  Creates a new file item and map its disk space.
- [FSItem.SetAttributesRequest](fsitem/setattributesrequest.md)
  A request to set attributes on an item.
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

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscreatefilekoioresult)*