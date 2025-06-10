# FSBlockmapFlags

**Framework**: FSKit  
**Kind**: struct

Flags that describe the behavior of a blockmap operation.

**Availability**:
- macOS 15.4+

## Declaration

```swift
struct FSBlockmapFlags
```

#### Overview

This type is an option set in Swift. In Objective-C, you use the cases of this enumeration to create a bit field.

## Topics

### Declaring block map behaviors
- [static var read: FSBlockmapFlags](fsblockmapflags/read.md)
  A flag that describes a read operation.
- [static var write: FSBlockmapFlags](fsblockmapflags/write.md)
  A flag that describes a write operation.
### Working with raw values
- [init(rawValue: UInt)](fsblockmapflags/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](fsblockmapflags/equatable-implementations.md)
- [OptionSet Implementations](fsblockmapflags/optionset-implementations.md)
- [SetAlgebra Implementations](fsblockmapflags/setalgebra-implementations.md)

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

- [struct FSCompleteIOFlags](fscompleteioflags.md)
  Flags that describe the behavior of an I/O completion operation.
- [class FSEntityIdentifier](fsentityidentifier.md)
  A base type that identifies containers and volumes.
- [class FSExtentPacker](fsextentpacker.md)
  A type that directs the kernel to map space on disk to a specific file managed by this file system.
- [enum FSExtentType](fsextenttype.md)
  An enumeration of types of extents.
- [enum FSMatchResult](fsmatchresult.md)
  A type that represents the recognition and usability of a probed resource.
- [class FSMetadataRange](fsmetadatarange.md)
  A range that describes contiguous metadata segments on disk.
- [class FSProbeResult](fsproberesult.md)
  An object that represents the results of a specific probe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockmapflags)*