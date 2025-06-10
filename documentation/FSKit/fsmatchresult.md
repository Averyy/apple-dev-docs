# FSMatchResult

**Framework**: FSKit  
**Kind**: enum

A type that represents the recognition and usability of a probed resource.

**Availability**:
- macOS 15.4+

## Declaration

```swift
enum FSMatchResult
```

## Topics

### Working with match results
- [FSMatchResult.usable](fsmatchresult/usable.md)
  The probe recognizes the resource and is ready to use it.
- [FSMatchResult.usableButLimited](fsmatchresult/usablebutlimited.md)
  The probe recognizes the resource and is ready to use it, but only in a limited capacity.
- [FSMatchResult.recognized](fsmatchresult/recognized.md)
  The probe recognizes the resource but can’t use it.
- [FSMatchResult.notRecognized](fsmatchresult/notrecognized.md)
  The probe doesn’t recognize the resource.
### Working with raw values
- [init?(rawValue: Int)](fsmatchresult/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](fsmatchresult/equatable-implementations.md)
- [RawRepresentable Implementations](fsmatchresult/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct FSBlockmapFlags](fsblockmapflags.md)
  Flags that describe the behavior of a blockmap operation.
- [struct FSCompleteIOFlags](fscompleteioflags.md)
  Flags that describe the behavior of an I/O completion operation.
- [class FSEntityIdentifier](fsentityidentifier.md)
  A base type that identifies containers and volumes.
- [class FSExtentPacker](fsextentpacker.md)
  A type that directs the kernel to map space on disk to a specific file managed by this file system.
- [enum FSExtentType](fsextenttype.md)
  An enumeration of types of extents.
- [class FSMetadataRange](fsmetadatarange.md)
  A range that describes contiguous metadata segments on disk.
- [class FSProbeResult](fsproberesult.md)
  An object that represents the results of a specific probe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsmatchresult)*