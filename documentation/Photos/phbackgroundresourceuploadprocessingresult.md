# PHBackgroundResourceUploadProcessingResult

**Framework**: Photos  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
enum PHBackgroundResourceUploadProcessingResult
```

## Mentions

- [Uploading asset resources in the background](../PhotoKit/uploading-asset-resources-in-the-background.md)

## Topics

### Processing results
- [PHBackgroundResourceUploadProcessingResult.completed](./phbackgroundresourceuploadprocessingresult/completed.md)
  the extension has completed all processing required and is up to date with the photos library
- [PHBackgroundResourceUploadProcessingResult.failure](./phbackgroundresourceuploadprocessingresult/failure.md)
  the extension failed the processing task with an error
- [PHBackgroundResourceUploadProcessingResult.processing](./phbackgroundresourceuploadprocessingresult/processing.md)
  the extension has only partially completed its processing and still requires more time

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)

## See Also

### Processing upload requests
- [func process() -> PHBackgroundResourceUploadProcessingResult](./phbackgroundresourceuploadextension/process%28%29.md)
  Request to initiate processing background upload jobs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phbackgroundresourceuploadprocessingresult)*