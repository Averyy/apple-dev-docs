# FSVolume.PathConfOperations

**Framework**: FSKit  
**Kind**: protocol  
**Role**: Protocol

Properties implemented by volumes that support providing the values of system limits or options.

**Availability**:
- macOS 15.4+

## Declaration

```swift
protocol PathConfOperations : NSObjectProtocol
```

```objc
@protocol FSVolumePathConfOperations <NSObject>
```

## Overview

This protocol gathers properties related to the `pathconf` and `fpathconf` system calls.

For a file, the value of a property applies to just that file; for a directory, the value applies to all items in the directory.

Properties that represent limits and have a numeric type use `-1` to represent no limit.

## Topics

### Checking limits and configurations
- [var maximumLinkCount: Int](./pathconfoperations/maximumlinkcount.md)
  A property that represents the maximum number of hard links to the object.
- [var maximumNameLength: Int](./pathconfoperations/maximumnamelength.md)
  A property that represents the maximum length of a component of a filename.
- [var restrictsOwnershipChanges: Bool](./pathconfoperations/restrictsownershipchanges.md)
  A Boolean property that indicates whether the volume restricts ownership changes based on authorization.
- [var truncatesLongNames: Bool](./pathconfoperations/truncateslongnames.md)
  A property that indicates whether the volume truncates files longer than its maximum supported length.
- [var maximumFileSize: UInt64](./pathconfoperations/maximumfilesize.md)
  The maximum size of a regular file allowed in the volume.
- [var maximumFileSizeInBits: Int](./pathconfoperations/maximumfilesizeinbits.md)
  The minimum number of bits needed to represent, as a signed integer value, the maximum size of a regular file allowed in the volume.
- [var maximumXattrSize: Int](./pathconfoperations/maximumxattrsize.md)
  The maximum extended attribute size in bytes.
- [var maximumXattrSizeInBits: Int](./pathconfoperations/maximumxattrsizeinbits.md)
  The maximum extended attribute size in bits.

## Relationships

### Inherits From
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [FSVolume.Handler](./handler.md)
- [FSVolume.Operations](./operations.md)

## See Also

### Implementing required handlers
- [FSVolume.Handler](./handler.md)
  Methods that all volumes implement to provide required capabilities.
- [class FSVolumeHandlerResult](../fsvolumehandlerresult.md)
  An abstract base class for all result objects in FSKit handler-style protocols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/pathconfoperations)*