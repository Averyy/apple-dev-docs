# fileURL

**Framework**: Foundation  
**Kind**: property

A URL that represents the file for the current progress object.

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
var fileURL: URL? { get set }
```

#### Discussion

Set this value for a progress that you [`publish()`](progress/publish().md) to subscribers that register for updates using [`addSubscriber(forFileURL:withPublishingHandler:)`](progress/addsubscriber(forfileurl:withpublishinghandler:).md).

If present, [`Progress`](progress.md) presents additional information in its localized description by setting a value in the `userInfo` dictionary.

## See Also

- [var fileOperationKind: Progress.FileOperationKind?](progress/fileoperationkind-swift.property.md)
  The kind of file operation for the progress object.
- [var fileTotalCount: Int?](progress/filetotalcount.md)
  The total number of files for a file progress object.
- [var fileCompletedCount: Int?](progress/filecompletedcount.md)
  The number of completed files for a file progress object.
- [Progress.FileOperationKind](progress/fileoperationkind-swift.struct.md)
  The kind of file operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/fileurl)*