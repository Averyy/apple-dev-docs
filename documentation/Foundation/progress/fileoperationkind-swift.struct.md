# Progress.FileOperationKind

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * NSProgressFileOperationKind;
```

## Discussion

When tracking file operations with the progress [`kind`](./kind.md) set to [`file`](../progresskind/file.md), provide a value for the [`fileOperationKindKey`](../progressuserinfokey/fileoperationkindkey.md) in the user info dictionary.

To specify the kind of file operation, provide one of the following values:

- [`copying`](./fileoperationkind-swift.struct/copying.md)
- [`decompressingAfterDownloading`](./fileoperationkind-swift.struct/decompressingafterdownloading.md)
- [`downloading`](./fileoperationkind-swift.struct/downloading.md)
- [`uploading`](./fileoperationkind-swift.struct/uploading.md)
- [`receiving`](./fileoperationkind-swift.struct/receiving.md)

## Topics

### Creating Kinds of File Operation
- [init(String)](./fileoperationkind-swift.struct/init%28_%29.md)
  Creates a new kind of file operation using the specified string.
- [init(rawValue: String)](./fileoperationkind-swift.struct/init%28rawvalue%29.md)
  Creates a new kind of file operation using the raw value of a string you specify.
### Recognizing Kinds of File Operations
- [static let copying: Progress.FileOperationKind](./fileoperationkind-swift.struct/copying.md)
  The progress is tracking the copying of a file from source to destination.
- [static let decompressingAfterDownloading: Progress.FileOperationKind](./fileoperationkind-swift.struct/decompressingafterdownloading.md)
  The progress is tracking file decompression after a download.
- [static let downloading: Progress.FileOperationKind](./fileoperationkind-swift.struct/downloading.md)
  The progress is tracking a file download operation.
- [static let uploading: Progress.FileOperationKind](./fileoperationkind-swift.struct/uploading.md)
  The progress is tracking a file upload operation.
- [static let receiving: Progress.FileOperationKind](./fileoperationkind-swift.struct/receiving.md)
  The progress is tracking the receipt of a file from another source.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting File Operation Progress Information
- [var fileOperationKind: Progress.FileOperationKind?](./fileoperationkind-swift.property.md)
  The kind of file operation for the progress object.
- [var fileURL: URL?](./fileurl.md)
  A URL that represents the file for the current progress object.
- [var fileTotalCount: Int?](./filetotalcount.md)
  The total number of files for a file progress object.
- [var fileCompletedCount: Int?](./filecompletedcount.md)
  The number of completed files for a file progress object.
- [fileTotalCount](../nsprogress/filetotalcount.md)
  The total number of files for a file progress object.
- [fileCompletedCount](../nsprogress/filecompletedcount.md)
  The number of completed files for a file progress object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/fileoperationkind-swift.struct)*