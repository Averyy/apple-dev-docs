# FSVolume.PreallocateFlags

**Framework**: FSKit  
**Kind**: struct

Behavior flags for preallocation operations.

**Availability**:
- macOS 15.4+

## Declaration

```swift
struct PreallocateFlags
```

## Topics

### Declaring preallocation behaviors
- [static var contiguous: FSVolume.PreallocateFlags](fsvolume/preallocateflags/contiguous.md)
  Allocates contiguous space.
- [static var all: FSVolume.PreallocateFlags](fsvolume/preallocateflags/all.md)
  Allocates all requested space or no space at all.
- [static var persist: FSVolume.PreallocateFlags](fsvolume/preallocateflags/persist.md)
  Allocates space that isn’t freed when deleting the descriptor.
- [static var fromEOF: FSVolume.PreallocateFlags](fsvolume/preallocateflags/fromeof.md)
  Allocates space from the physical end of file.
### Working with raw values
- [init(rawValue: UInt)](fsvolume/preallocateflags/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

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
- [func preallocateSpace(for: FSItem, at: off_t, length: Int, flags: FSVolume.PreallocateFlags, packer: FSExtentPacker, context: FSContext, replyHandler: (FSPreallocateKOIOResult?, (any Error)?) -> Void)](fsvolume/kerneloffloadediohandler/preallocatespace(for:at:length:flags:packer:context:replyhandler:).md)
  Preallocates and maps disk space for the given file.
- [class FSPreallocateKOIOResult](fspreallocatekoioresult.md)
  The result of a kernel-offloaded preallocate call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/preallocateflags)*