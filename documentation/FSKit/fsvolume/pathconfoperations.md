# FSVolume.PathConfOperations

**Framework**: FSKit  
**Kind**: protocol

Properties implemented by volumes that support providing the values of system limits or options.

**Availability**:
- macOS 15.4+

## Declaration

```swift
protocol PathConfOperations : NSObjectProtocol
```

#### Overview

This protocol gathers properties related to the `pathconf` and `fpathconf` system calls.

For a file, the value of a property applies to just that file; for a directory, the value applies to all items in the directory.

Properties that represent limits and have a numeric type use `-1` to represent no limit.

## Topics

### Checking limits and configurations
- [var maximumLinkCount: Int](fsvolume/pathconfoperations/maximumlinkcount.md)
  A property that represents the maximum number of hard links to the object.
- [var maximumNameLength: Int](fsvolume/pathconfoperations/maximumnamelength.md)
  A property that represents the maximum length of a component of a filename.
- [var restrictsOwnershipChanges: Bool](fsvolume/pathconfoperations/restrictsownershipchanges.md)
  A Boolean property that indicates whether the volume restricts ownership changes based on authorization.
- [var truncatesLongNames: Bool](fsvolume/pathconfoperations/truncateslongnames.md)
  A property that indicates whether the volume truncates files longer than its maximum supported length.
- [var maximumFileSize: UInt64](fsvolume/pathconfoperations/maximumfilesize.md)
  The maximum size of a regular file allowed in the volume.
- [var maximumFileSizeInBits: Int](fsvolume/pathconfoperations/maximumfilesizeinbits.md)
  The minimum number of bits needed to represent, as a signed integer value, the maximum size of a regular file allowed in the volume.
- [var maximumXattrSize: Int](fsvolume/pathconfoperations/maximumxattrsize.md)
  The maximum extended attribute size in bytes.
- [var maximumXattrSizeInBits: Int](fsvolume/pathconfoperations/maximumxattrsizeinbits.md)
  The maximum extended attribute size in bits.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [FSVolume.Operations](fsvolume/operations.md)

## See Also

- [FSVolume.Operations](fsvolume/operations.md)
  Methods that all volumes implement to provide required capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/pathconfoperations)*