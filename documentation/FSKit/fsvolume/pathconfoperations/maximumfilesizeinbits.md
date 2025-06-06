# maximumFileSizeInBits

**Framework**: FSKit  
**Kind**: property

The minimum number of bits needed to represent, as a signed integer value, the maximum size of a regular file allowed in the volume.

**Availability**:
- macOS 15.4+

## Declaration

```swift
optional var maximumFileSizeInBits: Int { get }
```

#### Discussion

The maximum file size is `2^(maximumFileSizeInBits - 1)`.

| Maximum file size (bytes) | Maximum (in hex) | Unsigned bits | Signed bits |
| --- | --- | --- | --- |
| 65,535 | `0xFFFF` | 16 | 17 |
| 2,147,483,647 | `0x7FFFFFFF` | 31 | 32 |
| 4,294,967,295 | `0xFFFFFFFF` | 32 | 33 |
| 18,446,744,073,709,551,615 | `0xFFFFFFFFFFFFFFFF` | 64 | 65 |

Implement at least one of [`maximumFileSize`](fsvolume/pathconfoperations/maximumfilesize.md) or `maximumFileSizeInBits`. FSKit automatically converts from one to another if needed. If you implement both, FSKit uses only the `maximumFileSizeInBits` implementation.

## See Also

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
- [var maximumXattrSize: Int](fsvolume/pathconfoperations/maximumxattrsize.md)
  The maximum extended attribute size in bytes.
- [var maximumXattrSizeInBits: Int](fsvolume/pathconfoperations/maximumxattrsizeinbits.md)
  The maximum extended attribute size in bits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/pathconfoperations/maximumfilesizeinbits)*