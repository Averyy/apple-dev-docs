# destroyOperation

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Destroy file.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: Use -[NSFileManager removeItemAtURL:error:] instead.

## Declaration

```swift
static let destroyOperation: NSWorkspace.FileOperationName
```

```c
extern NSWorkspaceFileOperationName NSWorkspaceDestroyOperation;
```

## Discussion

Behaves the same as  [`removeItem(at:)`](../../../Foundation/filemanager/removeitem%28at%29.md).

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
- [static let duplicateOperation: NSWorkspace.FileOperationName](./duplicateoperation.md)
  Duplicate file in source directory.
- [static let encryptOperation: NSWorkspace.FileOperationName](./encryptoperation.md)
  Encrypt file. This operation always returns an error.
- [static let linkOperation: NSWorkspace.FileOperationName](./linkoperation.md)
  Create hard link to file in destination.
- [static let moveOperation: NSWorkspace.FileOperationName](./moveoperation.md)
  Move file to destination.
- [static let recycleOperation: NSWorkspace.FileOperationName](./recycleoperation.md)
  Move file to trash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/fileoperationname/destroyoperation)*