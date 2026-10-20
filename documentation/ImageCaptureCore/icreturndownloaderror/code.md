# ICReturnDownloadError.Code

**Framework**: ImageCaptureCore  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

```swift
enum Code
```

```c
enum ICReturnDownloadErrorCode : NSInteger;
```

## Topics

### Enumeration Cases
- [ICReturnDownloadError.Code.fileWritable](./code/filewritable.md)
  The destination file is not writable.
- [ICReturnDownloadError.Code.pathInvalid](./code/pathinvalid.md)
  The destination path is invalid.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Error Codes
- [static var fileWritable: ICReturnDownloadError.Code](./filewritable.md)
  The destination file is not writable.
- [static var pathInvalid: ICReturnDownloadError.Code](./pathinvalid.md)
  The destination path is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icreturndownloaderror/code)*