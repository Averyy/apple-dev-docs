# maximumFileSize

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

The maximum size of a regular file allowed in the volume.

**Availability**:
- macOS 15.4+

## Declaration

```swift
optional var maximumFileSize: UInt64 { get }
```

```objc
@property (readonly) uint64_t maximumFileSize;
```

## Discussion

Implement at least one of `maximumFileSize` or [`maximumFileSizeInBits`](./maximumfilesizeinbits.md). FSKit automatically converts from one to another if needed. If you implement both, FSKit uses only the `maximumFileSizeInBits` implementation.

## See Also

### Checking limits and configurations
- [var maximumLinkCount: Int](./maximumlinkcount.md)
  A property that represents the maximum number of hard links to the object.
- [var maximumNameLength: Int](./maximumnamelength.md)
  A property that represents the maximum length of a component of a filename.
- [var restrictsOwnershipChanges: Bool](./restrictsownershipchanges.md)
  A Boolean property that indicates whether the volume restricts ownership changes based on authorization.
- [var truncatesLongNames: Bool](./truncateslongnames.md)
  A property that indicates whether the volume truncates files longer than its maximum supported length.
- [var maximumFileSizeInBits: Int](./maximumfilesizeinbits.md)
  The minimum number of bits needed to represent, as a signed integer value, the maximum size of a regular file allowed in the volume.
- [var maximumXattrSize: Int](./maximumxattrsize.md)
  The maximum extended attribute size in bytes.
- [var maximumXattrSizeInBits: Int](./maximumxattrsizeinbits.md)
  The maximum extended attribute size in bits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/pathconfoperations/maximumfilesize)*