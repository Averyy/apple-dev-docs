# moveOperation

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Move file to destination.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: Use -[NSFileManager moveItemAtURL:toURL:error:] instead.

## Declaration

```swift
static let moveOperation: NSWorkspace.FileOperationName
```

```c
extern NSWorkspaceFileOperationName NSWorkspaceMoveOperation;
```

#### Discussion

Behaves the same as [`moveItem(at:to:)`](../../../Foundation/filemanager/moveitem%28at,to%29.md).

## See Also

### Type Properties
- [static let compressOperation: NSWorkspace.FileOperationName](./compressoperation.md)
  Compress file. This operation always returns an error.
- [static let copyOperation: NSWorkspace.FileOperationName](./copyoperation.md)
  Copy file to destination.
- [static let decompressOperation: NSWorkspace.FileOperationName](./decompressoperation.md)
  Decompress file. This operation always returns an error.
- [static let decryptOperation: NSWorkspace.FileOperationName](./decryptoperation.md)
  Decrypt file. This operation always returns an error.
- [static let destroyOperation: NSWorkspace.FileOperationName](./destroyoperation.md)
  Destroy file.
- [static let duplicateOperation: NSWorkspace.FileOperationName](./duplicateoperation.md)
  Duplicate file in source directory.
- [static let encryptOperation: NSWorkspace.FileOperationName](./encryptoperation.md)
  Encrypt file. This operation always returns an error.
- [static let linkOperation: NSWorkspace.FileOperationName](./linkoperation.md)
  Create hard link to file in destination.
- [static let recycleOperation: NSWorkspace.FileOperationName](./recycleoperation.md)
  Move file to trash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/fileoperationname/moveoperation)*