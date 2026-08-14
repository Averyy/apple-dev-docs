# FSVolume.AccessMask

**Framework**: FSKit  
**Kind**: struct

A bitmask of access rights.

**Availability**:
- macOS 15.4+

## Declaration

```swift
struct AccessMask
```

## Topics

### Declaring read and write access
- [static var readData: FSVolume.AccessMask](fsvolume/accessmask/readdata.md)
  The file system allows reading data.
- [static var writeData: FSVolume.AccessMask](fsvolume/accessmask/writedata.md)
  The file system allows writing data.
### Declaring directory access
- [static var listDirectory: FSVolume.AccessMask](fsvolume/accessmask/listdirectory.md)
  The file system allows listing directory contents.
- [static var addFile: FSVolume.AccessMask](fsvolume/accessmask/addfile.md)
  The file system allows adding files.
- [static var addSubdirectory: FSVolume.AccessMask](fsvolume/accessmask/addsubdirectory.md)
  The file system allows adding subdirectories.
- [static var deleteChild: FSVolume.AccessMask](fsvolume/accessmask/deletechild.md)
  The file system allows deleting subdirectories.
- [static var search: FSVolume.AccessMask](fsvolume/accessmask/search.md)
  The file system allows searching files.
### Declaring file maniulation access
- [static var execute: FSVolume.AccessMask](fsvolume/accessmask/execute.md)
  The file system allows file execution.
- [static var delete: FSVolume.AccessMask](fsvolume/accessmask/delete.md)
  The file system allows deleting a file.
- [static var appendData: FSVolume.AccessMask](fsvolume/accessmask/appenddata.md)
  The file system allows appending data to a file.
### Declaring attribute access
- [static var readAttributes: FSVolume.AccessMask](fsvolume/accessmask/readattributes.md)
  The file system allows reading file attributes.
- [static var writeAttributes: FSVolume.AccessMask](fsvolume/accessmask/writeattributes.md)
  The file system allows writing file attributes.
- [static var readXattr: FSVolume.AccessMask](fsvolume/accessmask/readxattr.md)
  The file system allows reading extended file attributes.
- [static var writeXattr: FSVolume.AccessMask](fsvolume/accessmask/writexattr.md)
  The file system allows writing extended file attributes.
- [static var readSecurity: FSVolume.AccessMask](fsvolume/accessmask/readsecurity.md)
  The file system allows reading a file’s security descriptors.
- [static var writeSecurity: FSVolume.AccessMask](fsvolume/accessmask/writesecurity.md)
  The file system allows writing a file’s security descriptors.
### Ownership access
- [static var takeOwnership: FSVolume.AccessMask](fsvolume/accessmask/takeownership.md)
  The file system allows taking ownership of a file.
### Working with raw values
- [init(rawValue: UInt)](fsvolume/accessmask/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [func checkAccess(to: FSItem, requestedAccess: FSVolume.AccessMask, context: FSContext, replyHandler: (FSCheckAccessResult?, (any Error)?) -> Void)](fsvolume/accesscheckhandler/checkaccess(to:requestedaccess:context:replyhandler:).md)
  Checks whether the file system allows access to the given item.
- [class FSCheckAccessResult](fscheckaccessresult.md)
  The result of a check-access call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/accessmask)*