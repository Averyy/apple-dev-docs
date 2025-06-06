# Progress.FileOperationKind

**Framework**: Foundation  
**Kind**: struct

The kind of file operation.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct FileOperationKind
```

#### Discussion

When tracking file operations with the progress [`kind`](progress/kind.md) set to [`file`](progresskind/file.md), provide a value for the [`fileOperationKindKey`](progressuserinfokey/fileoperationkindkey.md) in the user info dictionary.

To specify the kind of file operation, provide one of the following values:

- [`copying`](progress/fileoperationkind-swift.struct/copying.md)
- [`decompressingAfterDownloading`](progress/fileoperationkind-swift.struct/decompressingafterdownloading.md)
- [`downloading`](progress/fileoperationkind-swift.struct/downloading.md)
- [`uploading`](progress/fileoperationkind-swift.struct/uploading.md)
- [`receiving`](progress/fileoperationkind-swift.struct/receiving.md)

## Topics

### Creating Kinds of File Operation
- [init(String)](progress/fileoperationkind-swift.struct/init(_:).md)
  Creates a new kind of file operation using the specified string.
- [init(rawValue: String)](progress/fileoperationkind-swift.struct/init(rawvalue:).md)
  Creates a new kind of file operation using the raw value of a string you specify.
### Recognizing Kinds of File Operations
- [static let copying: Progress.FileOperationKind](progress/fileoperationkind-swift.struct/copying.md)
  The progress is tracking the copying of a file from source to destination.
- [static let decompressingAfterDownloading: Progress.FileOperationKind](progress/fileoperationkind-swift.struct/decompressingafterdownloading.md)
  The progress is tracking file decompression after a download.
- [static let downloading: Progress.FileOperationKind](progress/fileoperationkind-swift.struct/downloading.md)
  The progress is tracking a file download operation.
- [static let uploading: Progress.FileOperationKind](progress/fileoperationkind-swift.struct/uploading.md)
  The progress is tracking a file upload operation.
- [static let receiving: Progress.FileOperationKind](progress/fileoperationkind-swift.struct/receiving.md)
  The progress is tracking the receipt of a file from another source.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var fileOperationKind: Progress.FileOperationKind?](progress/fileoperationkind-swift.property.md)
  The kind of file operation for the progress object.
- [var fileURL: URL?](progress/fileurl.md)
  A URL that represents the file for the current progress object.
- [var fileTotalCount: Int?](progress/filetotalcount.md)
  The total number of files for a file progress object.
- [var fileCompletedCount: Int?](progress/filecompletedcount.md)
  The number of completed files for a file progress object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/fileoperationkind-swift.struct)*