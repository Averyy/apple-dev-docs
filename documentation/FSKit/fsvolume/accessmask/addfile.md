# addFile

**Framework**: FSKit  
**Kind**: property  
**Role**: Type Property

The file system allows adding files.

**Availability**:
- macOS 15.4+

## Declaration

```swift
static var addFile: FSVolume.AccessMask { get }
```

```c
FSAccessAddFile
```

## See Also

### Declaring directory access
- [static var listDirectory: FSVolume.AccessMask](./listdirectory.md)
  The file system allows listing directory contents.
- [static var addSubdirectory: FSVolume.AccessMask](./addsubdirectory.md)
  The file system allows adding subdirectories.
- [static var deleteChild: FSVolume.AccessMask](./deletechild.md)
  The file system allows deleting subdirectories.
- [static var search: FSVolume.AccessMask](./search.md)
  The file system allows searching files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/accessmask/addfile)*