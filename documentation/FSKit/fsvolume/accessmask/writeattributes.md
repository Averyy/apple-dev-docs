# writeAttributes

**Framework**: FSKit  
**Kind**: property  
**Role**: Type Property

The file system allows writing file attributes.

**Availability**:
- macOS 15.4+

## Declaration

```swift
static var writeAttributes: FSVolume.AccessMask { get }
```

```c
FSAccessWriteAttributes
```

## See Also

### Declaring attribute access
- [static var readAttributes: FSVolume.AccessMask](./readattributes.md)
  The file system allows reading file attributes.
- [static var readXattr: FSVolume.AccessMask](./readxattr.md)
  The file system allows reading extended file attributes.
- [static var writeXattr: FSVolume.AccessMask](./writexattr.md)
  The file system allows writing extended file attributes.
- [static var readSecurity: FSVolume.AccessMask](./readsecurity.md)
  The file system allows reading a file’s security descriptors.
- [static var writeSecurity: FSVolume.AccessMask](./writesecurity.md)
  The file system allows writing a file’s security descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/accessmask/writeattributes)*