# all

**Framework**: FSKit  
**Kind**: property  
**Role**: Type Property

Allocates all requested space or no space at all.

**Availability**:
- macOS 15.4+

## Declaration

```swift
static var all: FSVolume.PreallocateFlags { get }
```

```c
FSPreallocateFlagsAll
```

## See Also

### Declaring preallocation behaviors
- [static var contiguous: FSVolume.PreallocateFlags](./contiguous.md)
  Allocates contiguous space.
- [static var persist: FSVolume.PreallocateFlags](./persist.md)
  Allocates space that isn’t freed when deleting the descriptor.
- [static var fromEOF: FSVolume.PreallocateFlags](./fromeof.md)
  Allocates space from the physical end of file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/preallocateflags/all)*