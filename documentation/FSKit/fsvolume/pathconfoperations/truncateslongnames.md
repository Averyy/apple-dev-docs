# truncatesLongNames

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A property that indicates whether the volume truncates files longer than its maximum supported length.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var truncatesLongNames: Bool { get }
```

```objc
@property (readonly) BOOL truncatesLongNames;
```

#### Discussion

If this value is `true`, the volume truncates the filename to [`maximumNameLength`](./maximumnamelength.md) if the filename is longer than that. If this value is false, the file system responds with the error code `ENAMETOOLONG` if the filename is longer than [`maximumNameLength`](./maximumnamelength.md).

## See Also

### Checking limits and configurations
- [var maximumLinkCount: Int](./maximumlinkcount.md)
  A property that represents the maximum number of hard links to the object.
- [var maximumNameLength: Int](./maximumnamelength.md)
  A property that represents the maximum length of a component of a filename.
- [var restrictsOwnershipChanges: Bool](./restrictsownershipchanges.md)
  A Boolean property that indicates whether the volume restricts ownership changes based on authorization.
- [var maximumFileSize: UInt64](./maximumfilesize.md)
  The maximum size of a regular file allowed in the volume.
- [var maximumFileSizeInBits: Int](./maximumfilesizeinbits.md)
  The minimum number of bits needed to represent, as a signed integer value, the maximum size of a regular file allowed in the volume.
- [var maximumXattrSize: Int](./maximumxattrsize.md)
  The maximum extended attribute size in bytes.
- [var maximumXattrSizeInBits: Int](./maximumxattrsizeinbits.md)
  The maximum extended attribute size in bits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/pathconfoperations/truncateslongnames)*