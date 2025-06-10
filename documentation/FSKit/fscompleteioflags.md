# FSCompleteIOFlags

**Framework**: FSKit  
**Kind**: struct

Flags that describe the behavior of an I/O completion operation.

**Availability**:
- macOS 15.4+

## Declaration

```swift
struct FSCompleteIOFlags
```

#### Overview

This type is an option set in Swift. In Objective-C, the cases of this enumeration combine to create a bit field.

## Topics

### Declaring I/O completion behaviors
- [static var read: FSCompleteIOFlags](fscompleteioflags/read.md)
  A flag that describes a read operation.
- [static var write: FSCompleteIOFlags](fscompleteioflags/write.md)
  A flag that describes a write operation.
- [static var async: FSCompleteIOFlags](fscompleteioflags/async.md)
  A flag that requests that the file system module flush metadata I/O asynchronously.
### Working with raw values
- [init(rawValue: UInt)](fscompleteioflags/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](fscompleteioflags/equatable-implementations.md)
- [OptionSet Implementations](fscompleteioflags/optionset-implementations.md)
- [SetAlgebra Implementations](fscompleteioflags/setalgebra-implementations.md)

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

- [struct FSBlockmapFlags](fsblockmapflags.md)
  Flags that describe the behavior of a blockmap operation.
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

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscompleteioflags)*