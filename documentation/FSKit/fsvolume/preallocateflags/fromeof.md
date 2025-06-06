# fromEOF

**Framework**: FSKit  
**Kind**: property

Allocates space from the physical end of file.

**Availability**:
- macOS 15.4+

## Declaration

```swift
static var fromEOF: FSVolume.PreallocateFlags { get }
```

#### Discussion

When implementing this behavior, ignore any offset in the preallocate call. This flag is currently set for all [`preallocateSpace(for:at:length:flags:replyHandler:)`](fsvolume/preallocateoperations/preallocatespace(for:at:length:flags:replyhandler:).md) calls.

## See Also

- [static var contiguous: FSVolume.PreallocateFlags](fsvolume/preallocateflags/contiguous.md)
  Allocates contiguous space.
- [static var all: FSVolume.PreallocateFlags](fsvolume/preallocateflags/all.md)
  Allocates all requested space or no space at all.
- [static var persist: FSVolume.PreallocateFlags](fsvolume/preallocateflags/persist.md)
  Allocates space that isn’t freed when deleting the descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/preallocateflags/fromeof)*