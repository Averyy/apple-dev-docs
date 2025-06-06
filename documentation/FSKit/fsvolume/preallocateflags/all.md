# all

**Framework**: FSKit  
**Kind**: property

Allocates all requested space or no space at all.

**Availability**:
- macOS 15.4+

## Declaration

```swift
static var all: FSVolume.PreallocateFlags { get }
```

## See Also

- [static var contiguous: FSVolume.PreallocateFlags](fsvolume/preallocateflags/contiguous.md)
  Allocates contiguous space.
- [static var persist: FSVolume.PreallocateFlags](fsvolume/preallocateflags/persist.md)
  Allocates space that isn’t freed when deleting the descriptor.
- [static var fromEOF: FSVolume.PreallocateFlags](fsvolume/preallocateflags/fromeof.md)
  Allocates space from the physical end of file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/preallocateflags/all)*