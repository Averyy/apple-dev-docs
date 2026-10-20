# uploading

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The progress is tracking a file upload operation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let uploading: Progress.FileOperationKind
```

```c
extern NSProgressFileOperationKind const NSProgressFileOperationKindUploading;
```

## See Also

### Recognizing Kinds of File Operations
- [static let copying: Progress.FileOperationKind](./copying.md)
  The progress is tracking the copying of a file from source to destination.
- [static let decompressingAfterDownloading: Progress.FileOperationKind](./decompressingafterdownloading.md)
  The progress is tracking file decompression after a download.
- [static let downloading: Progress.FileOperationKind](./downloading.md)
  The progress is tracking a file download operation.
- [static let receiving: Progress.FileOperationKind](./receiving.md)
  The progress is tracking the receipt of a file from another source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/fileoperationkind-swift.struct/uploading)*