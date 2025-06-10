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
### Default Implementations
- [Equatable Implementations](fsvolume/preallocateflags/equatable-implementations.md)
- [OptionSet Implementations](fsvolume/preallocateflags/optionset-implementations.md)
- [SetAlgebra Implementations](fsvolume/preallocateflags/setalgebra-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func preallocateSpace(for: FSItem, at: off_t, length: Int, flags: FSVolume.PreallocateFlags, replyHandler: (Int, (any Error)?) -> Void)](fsvolume/preallocateoperations/preallocatespace(for:at:length:flags:replyhandler:).md)
  Prealocates disk space for the given item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/preallocateflags)*