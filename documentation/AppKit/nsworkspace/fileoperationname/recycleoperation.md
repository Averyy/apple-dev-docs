# recycleOperation

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Move file to trash.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: Use -[NSWorkspace recycleURLs:completionHandler:] instead.

## Declaration

```swift
static let recycleOperation: NSWorkspace.FileOperationName
```

```c
extern NSWorkspaceFileOperationName NSWorkspaceRecycleOperation;
```

#### Discussion

The file is moved to the trash folder on the volume containing the file using the same semantics as [`moveOperation`](./moveoperation.md). If a file with the same name currently exists in the trash folder, the new file is renamed. If no trash folder exists on the volume containing the file, the operation fails.

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
- [static let moveOperation: NSWorkspace.FileOperationName](./moveoperation.md)
  Move file to destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/fileoperationname/recycleoperation)*