# NSWorkspace.FileOperationName

**Framework**: AppKit  
**Kind**: struct

Constants that define types of file operations.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct FileOperationName
```

#### Overview

These constants specify different types of file operations used by [`performFileOperation(_:source:destination:files:tag:)`](nsworkspace/performfileoperation(_:source:destination:files:tag:).md).

## Topics

### Type Properties
- [static let compressOperation: NSWorkspace.FileOperationName](nsworkspace/fileoperationname/compressoperation.md)
  Compress file. This operation always returns an error.
- [static let copyOperation: NSWorkspace.FileOperationName](nsworkspace/fileoperationname/copyoperation.md)
  Copy file to destination.
- [static let decompressOperation: NSWorkspace.FileOperationName](nsworkspace/fileoperationname/decompressoperation.md)
  Decompress file. This operation always returns an error.
- [static let decryptOperation: NSWorkspace.FileOperationName](nsworkspace/fileoperationname/decryptoperation.md)
  Decrypt file. This operation always returns an error.
- [static let destroyOperation: NSWorkspace.FileOperationName](nsworkspace/fileoperationname/destroyoperation.md)
  Destroy file.
- [static let duplicateOperation: NSWorkspace.FileOperationName](nsworkspace/fileoperationname/duplicateoperation.md)
  Duplicate file in source directory.
- [static let encryptOperation: NSWorkspace.FileOperationName](nsworkspace/fileoperationname/encryptoperation.md)
  Encrypt file. This operation always returns an error.
- [static let linkOperation: NSWorkspace.FileOperationName](nsworkspace/fileoperationname/linkoperation.md)
  Create hard link to file in destination.
- [static let moveOperation: NSWorkspace.FileOperationName](nsworkspace/fileoperationname/moveoperation.md)
  Move file to destination.
- [static let recycleOperation: NSWorkspace.FileOperationName](nsworkspace/fileoperationname/recycleoperation.md)
  Move file to trash.
### Initializers
- [init(rawValue: String)](nsworkspace/fileoperationname/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NSWorkspace.LaunchOptions](nsworkspace/launchoptions.md)
  Constants specifying how you want to launch an app
- [NSWorkspace.LaunchConfigurationKey](nsworkspace/launchconfigurationkey.md)
  The following keys can be used in the configuration dictionary of the [`launchApplication(at:options:configuration:)`](nsworkspace/launchapplication(at:options:configuration:).md) method.  Each key is optional, and if omitted, default behavior is applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/fileoperationname)*