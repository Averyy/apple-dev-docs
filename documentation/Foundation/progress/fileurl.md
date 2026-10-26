# fileURL

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, nullable) NSURL * fileURL;
```

#### Discussion

Set this value for a progress that you [`publish()`](./publish%28%29.md) to subscribers that register for updates using [`addSubscriber(forFileURL:withPublishingHandler:)`](./addsubscriber%28forfileurl,withpublishinghandler%29.md).

If present, [`Progress`](../progress.md) presents additional information in its localized description by setting a value in the `userInfo` dictionary.

## See Also

### Inspecting File Operation Progress Information
- [var fileOperationKind: Progress.FileOperationKind?](./fileoperationkind-swift.property.md)
  The kind of file operation for the progress object.
- [var fileTotalCount: Int?](./filetotalcount.md)
  The total number of files for a file progress object.
- [var fileCompletedCount: Int?](./filecompletedcount.md)
  The number of completed files for a file progress object.
- [Progress.FileOperationKind](./fileoperationkind-swift.struct.md)
  The kind of file operation.
- [fileTotalCount](../nsprogress/filetotalcount.md)
  The total number of files for a file progress object.
- [fileCompletedCount](../nsprogress/filecompletedcount.md)
  The number of completed files for a file progress object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/fileurl)*