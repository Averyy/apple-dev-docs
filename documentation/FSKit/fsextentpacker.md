# FSExtentPacker

**Framework**: FSKit  
**Kind**: class

A type that directs the kernel to map space on disk to a specific file managed by this file system.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSExtentPacker
```

#### Overview

 provide the kernel the logical-to-physical mapping of a given file. An extent describes a physical offset on disk, and a length and a logical offset within the file. Rather than working with extents directly, you use this type’s methods to provide or “pack” extent information, which FSKit then passes to the kernel.

## Topics

### Packing extents
- [func packExtent(resource: FSBlockDeviceResource, type: FSExtentType, logicalOffset: off_t, physicalOffset: off_t, length: Int) -> Bool](fsextentpacker/packextent(resource:type:logicaloffset:physicaloffset:length:).md)
  Packs a single extent to send to the kernel.
- [enum FSExtentType](fsextenttype.md)
  An enumeration of types of extents.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [struct FSBlockmapFlags](fsblockmapflags.md)
  Flags that describe the behavior of a blockmap operation.
- [struct FSCompleteIOFlags](fscompleteioflags.md)
  Flags that describe the behavior of an I/O completion operation.
- [class FSEntityIdentifier](fsentityidentifier.md)
  A base type that identifies containers and volumes.
- [enum FSExtentType](fsextenttype.md)
  An enumeration of types of extents.
- [enum FSMatchResult](fsmatchresult.md)
  A type that represents the recognition and usability of a probed resource.
- [class FSMetadataRange](fsmetadatarange.md)
  A range that describes contiguous metadata segments on disk.
- [class FSProbeResult](fsproberesult.md)
  An object that represents the results of a specific probe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsextentpacker)*