# persist

**Framework**: FSKit  
**Kind**: property

Allocates space that isn’t freed when deleting the descriptor.

**Availability**:
- macOS 15.4+

## Declaration

```swift
static var persist: FSVolume.PreallocateFlags { get }
```

#### Discussion

This space remains allocated even after calling `close(2)`.

## See Also

- [static var contiguous: FSVolume.PreallocateFlags](fsvolume/preallocateflags/contiguous.md)
  Allocates contiguous space.
- [static var all: FSVolume.PreallocateFlags](fsvolume/preallocateflags/all.md)
  Allocates all requested space or no space at all.
- [static var fromEOF: FSVolume.PreallocateFlags](fsvolume/preallocateflags/fromeof.md)
  Allocates space from the physical end of file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/preallocateflags/persist)*