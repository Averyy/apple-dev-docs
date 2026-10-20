# NSWorkspace.FileOperationName

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that define types of file operations.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: Use [`FileManager`](../../Foundation/filemanager.md) methods instead.

## Declaration

```swift
struct FileOperationName
```

```c
typedef NSString * NSWorkspaceFileOperationName;
```

#### Overview

These constants specify different types of file operations used by [`performFileOperation(_:source:destination:files:tag:)`](./performfileoperation%28_,source,destination,files,tag%29.md).

## Topics

### Type Properties
- [static let compressOperation: NSWorkspace.FileOperationName](./fileoperationname/compressoperation.md)
  Compress file. This operation always returns an error.
- [static let copyOperation: NSWorkspace.FileOperationName](./fileoperationname/copyoperation.md)
  Copy file to destination.
- [static let decompressOperation: NSWorkspace.FileOperationName](./fileoperationname/decompressoperation.md)
  Decompress file. This operation always returns an error.
- [static let decryptOperation: NSWorkspace.FileOperationName](./fileoperationname/decryptoperation.md)
  Decrypt file. This operation always returns an error.
- [static let destroyOperation: NSWorkspace.FileOperationName](./fileoperationname/destroyoperation.md)
  Destroy file.
- [static let duplicateOperation: NSWorkspace.FileOperationName](./fileoperationname/duplicateoperation.md)
  Duplicate file in source directory.
- [static let encryptOperation: NSWorkspace.FileOperationName](./fileoperationname/encryptoperation.md)
  Encrypt file. This operation always returns an error.
- [static let linkOperation: NSWorkspace.FileOperationName](./fileoperationname/linkoperation.md)
  Create hard link to file in destination.
- [static let moveOperation: NSWorkspace.FileOperationName](./fileoperationname/moveoperation.md)
  Move file to destination.
- [static let recycleOperation: NSWorkspace.FileOperationName](./fileoperationname/recycleoperation.md)
  Move file to trash.
### Initializers
- [init(rawValue: String)](./fileoperationname/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Deprecated types
- [NSWorkspace.LaunchOptions](./launchoptions.md)
  Constants specifying how you want to launch an app
- [NSWorkspace.LaunchConfigurationKey](./launchconfigurationkey.md)
  The following keys can be used in the configuration dictionary of the [`launchApplication(at:options:configuration:)`](./launchapplication%28at,options,configuration%29.md) method.  Each key is optional, and if omitted, default behavior is applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/fileoperationname)*