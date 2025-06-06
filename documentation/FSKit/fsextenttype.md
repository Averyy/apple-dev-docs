# FSExtentType

**Framework**: FSKit  
**Kind**: enum

An enumeration of types of extents.

**Availability**:
- macOS 15.4+

## Declaration

```swift
enum FSExtentType
```

## Topics

### Working with extent types
- [FSExtentType.data](fsextenttype/data.md)
  An extent type to indicate valid data.
- [FSExtentType.zeroFill](fsextenttype/zerofill.md)
  An extent type to indicate uninitialized data.
### Working with raw values
- [init?(rawValue: Int)](fsextenttype/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](fsextenttype/equatable-implementations.md)
- [RawRepresentable Implementations](fsextenttype/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct FSBlockmapFlags](fsblockmapflags.md)
  Flags that describe the behavior of a blockmap operation.
- [struct FSCompleteIOFlags](fscompleteioflags.md)
  Flags that describe the behavior of an I/O completion operation.
- [class FSEntityIdentifier](fsentityidentifier.md)
  A base type that identifies containers and volumes.
- [class FSExtentPacker](fsextentpacker.md)
  A type that directs the kernel to map space on disk to a specific file managed by this file system.
- [enum FSMatchResult](fsmatchresult.md)
  A type that represents the recognition and usability of a probed resource.
- [class FSMetadataRange](fsmetadatarange.md)
  A range that describes contiguous metadata segments on disk.
- [class FSProbeResult](fsproberesult.md)
  An object that represents the results of a specific probe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsextenttype)*