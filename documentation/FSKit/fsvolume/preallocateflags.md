# FSVolume.PreallocateFlags

**Framework**: FSKit  
**Kind**: struct  
**Role**: Structure

Behavior flags for preallocation operations.

**Availability**:
- macOS 15.4+

## Declaration

```swift
struct PreallocateFlags
```

```c
enum FSPreallocateFlags : NSUInteger;
```

## Topics

### Declaring preallocation behaviors
- [static var contiguous: FSVolume.PreallocateFlags](./preallocateflags/contiguous.md)
  Allocates contiguous space.
- [static var all: FSVolume.PreallocateFlags](./preallocateflags/all.md)
  Allocates all requested space or no space at all.
- [static var persist: FSVolume.PreallocateFlags](./preallocateflags/persist.md)
  Allocates space that isn’t freed when deleting the descriptor.
- [static var fromEOF: FSVolume.PreallocateFlags](./preallocateflags/fromeof.md)
  Allocates space from the physical end of file.
### Working with raw values
- [init(rawValue: UInt)](./preallocateflags/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Working with items
- [func createFile(named: FSFileName, in: FSItem, attributes: FSItem.SetAttributesRequest, packer: FSExtentPacker, context: FSContext, replyHandler: (FSCreateFileKOIOResult?, (any Error)?) -> Void)](./kerneloffloadediohandler/createfile%28named,in,attributes,packer,context,replyhandler%29.md)
  Creates a new file item and map its disk space.
- [FSItem.SetAttributesRequest](../fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [class FSCreateFileKOIOResult](../fscreatefilekoioresult.md)
  The result of a kernel-offloaded create-file call.
- [func lookupItem(named: FSFileName, in: FSItem, packer: FSExtentPacker, context: FSContext, replyHandler: (FSLookupItemKOIOResult?, (any Error)?) -> Void)](./kerneloffloadediohandler/lookupitem%28named,in,packer,context,replyhandler%29.md)
  Looks up an item within a directory and maps its disk space.
- [class FSLookupItemKOIOResult](../fslookupitemkoioresult.md)
  The result of a kernel-offloaded lookup-item call.
- [func preallocateSpace(for: FSItem, at: off_t, length: Int, flags: FSVolume.PreallocateFlags, packer: FSExtentPacker, context: FSContext, replyHandler: (FSPreallocateKOIOResult?, (any Error)?) -> Void)](./kerneloffloadediohandler/preallocatespace%28for,at,length,flags,packer,context,replyhandler%29.md)
  Preallocates and maps disk space for the given file.
- [class FSPreallocateKOIOResult](../fspreallocatekoioresult.md)
  The result of a kernel-offloaded preallocate call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/preallocateflags)*