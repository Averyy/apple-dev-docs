# restrictsOwnershipChanges

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean property that indicates whether the volume restricts ownership changes based on authorization.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var restrictsOwnershipChanges: Bool { get }
```

```objc
@property (readonly) BOOL restrictsOwnershipChanges;
```

## Discussion

If this value is true, the volume rejects a `chown(2)` from anyone other than the superuser.

## See Also

### Checking limits and configurations
- [var maximumLinkCount: Int](./maximumlinkcount.md)
  A property that represents the maximum number of hard links to the object.
- [var maximumNameLength: Int](./maximumnamelength.md)
  A property that represents the maximum length of a component of a filename.
- [var truncatesLongNames: Bool](./truncateslongnames.md)
  A property that indicates whether the volume truncates files longer than its maximum supported length.
- [var maximumFileSize: UInt64](./maximumfilesize.md)
  The maximum size of a regular file allowed in the volume.
- [var maximumFileSizeInBits: Int](./maximumfilesizeinbits.md)
  The minimum number of bits needed to represent, as a signed integer value, the maximum size of a regular file allowed in the volume.
- [var maximumXattrSize: Int](./maximumxattrsize.md)
  The maximum extended attribute size in bytes.
- [var maximumXattrSizeInBits: Int](./maximumxattrsizeinbits.md)
  The maximum extended attribute size in bits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/pathconfoperations/restrictsownershipchanges)*