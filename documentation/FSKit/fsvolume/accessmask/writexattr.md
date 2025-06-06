# writeXattr

**Framework**: FSKit  
**Kind**: property

The file system allows writing extended file attributes.

**Availability**:
- macOS 15.4+

## Declaration

```swift
static var writeXattr: FSVolume.AccessMask { get }
```

## See Also

- [static var readAttributes: FSVolume.AccessMask](fsvolume/accessmask/readattributes.md)
  The file system allows reading file attributes.
- [static var writeAttributes: FSVolume.AccessMask](fsvolume/accessmask/writeattributes.md)
  The file system allows writing file attributes.
- [static var readXattr: FSVolume.AccessMask](fsvolume/accessmask/readxattr.md)
  The file system allows reading extended file attributes.
- [static var readSecurity: FSVolume.AccessMask](fsvolume/accessmask/readsecurity.md)
  The file system allows reading a file’s security descriptors.
- [static var writeSecurity: FSVolume.AccessMask](fsvolume/accessmask/writesecurity.md)
  The file system allows writing a file’s security descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/accessmask/writexattr)*