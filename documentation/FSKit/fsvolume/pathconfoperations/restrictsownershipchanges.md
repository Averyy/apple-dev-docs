# restrictsOwnershipChanges

**Framework**: FSKit  
**Kind**: property  
**Required**: Yes

A Boolean property that indicates whether the volume restricts ownership changes based on authorization.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var restrictsOwnershipChanges: Bool { get }
```

#### Discussion

If this value is true, the volume rejects a `chown(2)` from anyone other than the superuser.

## See Also

- [var maximumLinkCount: Int](fsvolume/pathconfoperations/maximumlinkcount.md)
  A property that represents the maximum number of hard links to the object.
- [var maximumNameLength: Int](fsvolume/pathconfoperations/maximumnamelength.md)
  A property that represents the maximum length of a component of a filename.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/pathconfoperations/restrictsownershipchanges)*