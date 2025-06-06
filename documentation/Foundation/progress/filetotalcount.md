# fileTotalCount

**Framework**: Foundation  
**Kind**: property

The total number of files for a file progress object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var fileTotalCount: Int? { get set }
```

#### Discussion

If the current progress is operating on a set of files, set this property to the total number of files in the operation.

If present, [`Progress`](progress.md) presents additional information in its localized description by setting a value in the `userInfo` dictionary.

## See Also

- [var fileOperationKind: Progress.FileOperationKind?](progress/fileoperationkind-swift.property.md)
  The kind of file operation for the progress object.
- [var fileURL: URL?](progress/fileurl.md)
  A URL that represents the file for the current progress object.
- [var fileCompletedCount: Int?](progress/filecompletedcount.md)
  The number of completed files for a file progress object.
- [Progress.FileOperationKind](progress/fileoperationkind-swift.struct.md)
  The kind of file operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/filetotalcount)*