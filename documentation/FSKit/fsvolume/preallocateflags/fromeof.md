# fromEOF

**Framework**: FSKit  
**Kind**: property  
**Role**: Type Property

Allocates space from the physical end of file.

**Availability**:
- macOS 15.4+

## Declaration

```swift
static var fromEOF: FSVolume.PreallocateFlags { get }
```

```c
FSPreallocateFlagsFromEOF
```

#### Discussion

When implementing this behavior, ignore any offset in the preallocate call. This flag is currently set for all [`preallocateSpace(for:at:length:flags:context:replyHandler:)`](../preallocatehandler/preallocatespace%28for,at,length,flags,context,replyhandler%29.md) calls.

## See Also

### Declaring preallocation behaviors
- [static var contiguous: FSVolume.PreallocateFlags](./contiguous.md)
  Allocates contiguous space.
- [static var all: FSVolume.PreallocateFlags](./all.md)
  Allocates all requested space or no space at all.
- [static var persist: FSVolume.PreallocateFlags](./persist.md)
  Allocates space that isn’t freed when deleting the descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/preallocateflags/fromeof)*