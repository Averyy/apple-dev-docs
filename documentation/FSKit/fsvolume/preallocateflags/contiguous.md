# contiguous

**Framework**: FSKit  
**Kind**: property

Allocates contiguous space.

**Availability**:
- macOS 15.4+

## Declaration

```swift
static var contiguous: FSVolume.PreallocateFlags { get }
```

## See Also

- [static var all: FSVolume.PreallocateFlags](fsvolume/preallocateflags/all.md)
  Allocates all requested space or no space at all.
- [static var persist: FSVolume.PreallocateFlags](fsvolume/preallocateflags/persist.md)
  Allocates space that isn’t freed when deleting the descriptor.
- [static var fromEOF: FSVolume.PreallocateFlags](fsvolume/preallocateflags/fromeof.md)
  Allocates space from the physical end of file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/preallocateflags/contiguous)*