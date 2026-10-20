# FSVolume.AccessMask

**Framework**: FSKit  
**Kind**: struct  
**Role**: Structure

A bitmask of access rights.

**Availability**:
- macOS 15.4+

## Declaration

```swift
struct AccessMask
```

```c
enum FSAccessMask : NSUInteger;
```

## Topics

### Declaring read and write access
- [static var readData: FSVolume.AccessMask](./accessmask/readdata.md)
  The file system allows reading data.
- [static var writeData: FSVolume.AccessMask](./accessmask/writedata.md)
  The file system allows writing data.
### Declaring directory access
- [static var listDirectory: FSVolume.AccessMask](./accessmask/listdirectory.md)
  The file system allows listing directory contents.
- [static var addFile: FSVolume.AccessMask](./accessmask/addfile.md)
  The file system allows adding files.
- [static var addSubdirectory: FSVolume.AccessMask](./accessmask/addsubdirectory.md)
  The file system allows adding subdirectories.
- [static var deleteChild: FSVolume.AccessMask](./accessmask/deletechild.md)
  The file system allows deleting subdirectories.
- [static var search: FSVolume.AccessMask](./accessmask/search.md)
  The file system allows searching files.
### Declaring file maniulation access
- [static var execute: FSVolume.AccessMask](./accessmask/execute.md)
  The file system allows file execution.
- [static var delete: FSVolume.AccessMask](./accessmask/delete.md)
  The file system allows deleting a file.
- [static var appendData: FSVolume.AccessMask](./accessmask/appenddata.md)
  The file system allows appending data to a file.
### Declaring attribute access
- [static var readAttributes: FSVolume.AccessMask](./accessmask/readattributes.md)
  The file system allows reading file attributes.
- [static var writeAttributes: FSVolume.AccessMask](./accessmask/writeattributes.md)
  The file system allows writing file attributes.
- [static var readXattr: FSVolume.AccessMask](./accessmask/readxattr.md)
  The file system allows reading extended file attributes.
- [static var writeXattr: FSVolume.AccessMask](./accessmask/writexattr.md)
  The file system allows writing extended file attributes.
- [static var readSecurity: FSVolume.AccessMask](./accessmask/readsecurity.md)
  The file system allows reading a file’s security descriptors.
- [static var writeSecurity: FSVolume.AccessMask](./accessmask/writesecurity.md)
  The file system allows writing a file’s security descriptors.
### Ownership access
- [static var takeOwnership: FSVolume.AccessMask](./accessmask/takeownership.md)
  The file system allows taking ownership of a file.
### Working with raw values
- [init(rawValue: UInt)](./accessmask/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Checking access
- [func checkAccess(to: FSItem, requestedAccess: FSVolume.AccessMask, context: FSContext, replyHandler: (FSCheckAccessResult?, (any Error)?) -> Void)](./accesscheckhandler/checkaccess%28to,requestedaccess,context,replyhandler%29.md)
  Checks whether the file system allows access to the given item.
- [class FSCheckAccessResult](../fscheckaccessresult.md)
  The result of a check-access call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/accessmask)*