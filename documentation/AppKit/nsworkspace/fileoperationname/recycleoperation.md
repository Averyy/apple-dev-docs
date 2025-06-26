# recycleOperation

**Framework**: AppKit  
**Kind**: property

Move file to trash. The file is moved to the trash folder on the volume containing the file using the same semantics as `NSWorkspaceMoveOperation`. If a file with the same name currently exists in the trash folder, the new file is renamed. If no trash folder exists on the volume containing the file, the operation fails.

**Availability**:
- macOS 10.0+

## Declaration

```swift
static let recycleOperation: NSWorkspace.FileOperationName
```

## See Also

- [static let compressOperation: NSWorkspace.FileOperationName](nsworkspace/fileoperationname/compressoperation.md)
  Compress file. This operation always returns an error.
- [static let copyOperation: NSWorkspace.FileOperationName](nsworkspace/fileoperationname/copyoperation.md)
  Copy file to destination. Behaves the same as doc://com.apple.documentation/documentation/foundation/nsfilemanager/1557010-copypath.
- [static let decompressOperation: NSWorkspace.FileOperationName](nsworkspace/fileoperationname/decompressoperation.md)
  Decompress file. This operation always returns an error.
- [static let decryptOperation: NSWorkspace.FileOperationName](nsworkspace/fileoperationname/decryptoperation.md)
  Decrypt file. This operation always returns an error.
- [static let destroyOperation: NSWorkspace.FileOperationName](nsworkspace/fileoperationname/destroyoperation.md)
  Destroy file. Behaves the same as  doc://com.apple.documentation/documentation/foundation/nsfilemanager/1556998-removefileatpath.
- [static let duplicateOperation: NSWorkspace.FileOperationName](nsworkspace/fileoperationname/duplicateoperation.md)
  Duplicate file in source directory.
- [static let encryptOperation: NSWorkspace.FileOperationName](nsworkspace/fileoperationname/encryptoperation.md)
  Encrypt file. This operation always returns an error.
- [static let linkOperation: NSWorkspace.FileOperationName](nsworkspace/fileoperationname/linkoperation.md)
  Create hard link to file in destination. Behaves the same as doc://com.apple.documentation/documentation/foundation/nsfilemanager/1557003-linkpath.
- [static let moveOperation: NSWorkspace.FileOperationName](nsworkspace/fileoperationname/moveoperation.md)
  Move file to destination. Behaves the same as doc://com.apple.documentation/documentation/foundation/nsfilemanager/1556999-movepath.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/fileoperationname/recycleoperation)*