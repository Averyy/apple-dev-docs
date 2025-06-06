# FSStatFSResult

**Framework**: Fskit  
**Kind**: class

A type used to report a volume’s statistics.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSStatFSResult
```

#### Overview

The names of this type’s properties match those in the `statfs` structure in `statfs(2)`, which reports these values for an FSKit file system. All numeric properties default to `0`. Override these values, unless a given property has no meaningful value to provide.

> **Note**: Available space, free space, total space, and used space have properties to express their values either as a number of blocks or a number of bytes. Your module may supply both of these values by setting both the relevant block or byte property. Alternatively, a module may set only one of the two properties. When you do this, FSKit calculates the matching value based on [`blockSize`](fsstatfsresult/blocksize.md).

For the read-only [`fileSystemTypeName`](fsstatfsresult/filesystemtypename.md), set this value with the designated initializer.

## Topics

### Initializers
- [init(fileSystemTypeName: String)](fsstatfsresult/init(filesystemtypename:).md)
  Creates an statistics result instance, using the given file system type name.
### Instance Properties
- [var availableBlocks: UInt64](fsstatfsresult/availableblocks.md)
  A property for the number of free blocks available to a non-superuser on the volume.
- [var availableBytes: UInt64](fsstatfsresult/availablebytes.md)
  A property for the amount of space available to users, in bytes, in the volume.
- [var blockSize: Int](fsstatfsresult/blocksize.md)
  A property for the volume’s block size, in bytes.
- [var fileSystemSubType: Int](fsstatfsresult/filesystemsubtype.md)
  A property for the file system’s subtype or flavor.
- [var fileSystemTypeName: String](fsstatfsresult/filesystemtypename.md)
  A property for the file system type name.
- [var freeBlocks: UInt64](fsstatfsresult/freeblocks.md)
  A property for the number of free blocks in the volume.
- [var freeBytes: UInt64](fsstatfsresult/freebytes.md)
  A property for the amount of free space, in bytes, in the volume.
- [var freeFiles: UInt64](fsstatfsresult/freefiles.md)
  A property for the total number of free file slots in the volume.
- [var ioSize: Int](fsstatfsresult/iosize.md)
  A property for the optimal block size with which to perform I/O.
- [var totalBlocks: UInt64](fsstatfsresult/totalblocks.md)
  A property for the volume’s total data block count.
- [var totalBytes: UInt64](fsstatfsresult/totalbytes.md)
  A property for the total size, in bytes, of the volume.
- [var totalFiles: UInt64](fsstatfsresult/totalfiles.md)
  A property for the total number of file slots in the volume,
- [var usedBlocks: UInt64](fsstatfsresult/usedblocks.md)
  A property for the number of used blocks in the volume.
- [var usedBytes: UInt64](fsstatfsresult/usedbytes.md)
  A property for the amount of used space, in bytes, in the volume.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [var supportedVolumeCapabilities: FSVolume.SupportedCapabilities](fsvolume/operations/supportedvolumecapabilities.md)
  A property that provides the supported capabilities of the volume.
- [FSVolume.SupportedCapabilities](fsvolume/supportedcapabilities.md)
  A type that represents capabillities supported by a volume, such as hard and symbolic links, journaling, and large file sizes.
- [var volumeStatistics: FSStatFSResult](fsvolume/operations/volumestatistics.md)
  A property that provides up-to-date statistics of the volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/FSKit/fsstatfsresult)*