# delete

**Framework**: FSKit  
**Kind**: property  
**Role**: Type Property

The file system allows deleting a file.

**Availability**:
- macOS 15.4+

## Declaration

```swift
static var delete: FSVolume.AccessMask { get }
```

```c
FSAccessDelete
```

## See Also

### Declaring file maniulation access
- [static var execute: FSVolume.AccessMask](./execute.md)
  The file system allows file execution.
- [static var appendData: FSVolume.AccessMask](./appenddata.md)
  The file system allows appending data to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/accessmask/delete)*