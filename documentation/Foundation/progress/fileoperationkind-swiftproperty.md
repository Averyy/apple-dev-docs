# fileOperationKind

**Framework**: Foundation  
**Kind**: property

The kind of file operation for the progress object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var fileOperationKind: Progress.FileOperationKind? { get set }
```

#### Discussion

Set this value when the [`kind`](progress/kind.md) property is [`file`](progresskind/file.md) to describe the kind of file operation.

If present, [`Progress`](progress.md) presents additional information in its localized description by setting a value in the `userInfo` dictionary.

## See Also

- [var fileURL: URL?](progress/fileurl.md)
  A URL that represents the file for the current progress object.
- [var fileTotalCount: Int?](progress/filetotalcount.md)
  The total number of files for a file progress object.
- [var fileCompletedCount: Int?](progress/filecompletedcount.md)
  The number of completed files for a file progress object.
- [Progress.FileOperationKind](progress/fileoperationkind-swift.struct.md)
  The kind of file operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/fileoperationkind-swift.property)*