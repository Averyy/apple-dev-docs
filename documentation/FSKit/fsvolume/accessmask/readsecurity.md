# readSecurity

**Framework**: FSKit  
**Kind**: property  
**Role**: Type Property

The file system allows reading a file’s security descriptors.

**Availability**:
- macOS 15.4+

## Declaration

```swift
static var readSecurity: FSVolume.AccessMask { get }
```

```c
FSAccessReadSecurity
```

## See Also

### Declaring attribute access
- [static var readAttributes: FSVolume.AccessMask](./readattributes.md)
  The file system allows reading file attributes.
- [static var writeAttributes: FSVolume.AccessMask](./writeattributes.md)
  The file system allows writing file attributes.
- [static var readXattr: FSVolume.AccessMask](./readxattr.md)
  The file system allows reading extended file attributes.
- [static var writeXattr: FSVolume.AccessMask](./writexattr.md)
  The file system allows writing extended file attributes.
- [static var writeSecurity: FSVolume.AccessMask](./writesecurity.md)
  The file system allows writing a file’s security descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/accessmask/readsecurity)*