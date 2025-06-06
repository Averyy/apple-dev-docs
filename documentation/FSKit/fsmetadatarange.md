# FSMetadataRange

**Framework**: FSKit  
**Kind**: class

A range that describes contiguous metadata segments on disk.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSMetadataRange
```

#### Overview

This type represents a range that begins at `startOffset` and ends at `startOffset + segmentLength * segmentCount`. Each segment in the range represents a single block in the resource’s buffer cache.

For example, given an `FSMetadataRange` with the following properties:

- `startOffset = 0`
- `segmentLength = 512`
- `segmentCount = 8`

The range represents eight segments: from 0 to 511, then from 512 to 1023, and so on until a final segment of 3584 to 4095.

Ensure that each metadata segment represents a range that’s already present in the resource’s buffer cache. Similarly, ensure that each segment’s offset and length matches the offset and length of the corresponding block in the buffer cache.

## Topics

### Creating a metadata range
- [init(offset: off_t, segmentLength: UInt64, segmentCount: UInt64)](fsmetadatarange/init(offset:segmentlength:segmentcount:).md)
  Initializes a metadata range with the given properties.
### Accessing range properties
- [var startOffset: off_t](fsmetadatarange/startoffset.md)
  The start offset of the range in bytes.
- [var segmentLength: UInt64](fsmetadatarange/segmentlength.md)
  The segment length in bytes.
- [var segmentCount: UInt64](fsmetadatarange/segmentcount.md)
  The number of segments in the range.

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
- [class FSExtentPacker](fsextentpacker.md)
  A type that directs the kernel to map space on disk to a specific file managed by this file system.
- [enum FSExtentType](fsextenttype.md)
  An enumeration of types of extents.
- [enum FSMatchResult](fsmatchresult.md)
  A type that represents the recognition and usability of a probed resource.
- [class FSProbeResult](fsproberesult.md)
  An object that represents the results of a specific probe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsmetadatarange)*