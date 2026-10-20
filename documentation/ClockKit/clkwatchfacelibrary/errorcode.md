# CLKWatchFaceLibrary.ErrorCode

**Framework**: ClockKit  
**Kind**: enum  
**Role**: Enumeration

Error codes that the watch face library returns.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.0+

## Declaration

```swift
enum ErrorCode
```

```c
enum CLKWatchFaceLibraryErrorCode : NSInteger;
```

## Topics

### Errors
- [CLKWatchFaceLibrary.ErrorCode.notFileURL](./errorcode/notfileurl.md)
  No file was found at the specified URL.
- [CLKWatchFaceLibrary.ErrorCode.invalidFile](./errorcode/invalidfile.md)
  The specified file wasn’t a valid watch face file.
- [CLKWatchFaceLibrary.ErrorCode.permissionDenied](./errorcode/permissiondenied.md)
  The app does not have permission to read the specified file.
- [CLKWatchFaceLibrary.ErrorCode.faceNotAvailable](./errorcode/facenotavailable.md)
  The watch face is not available on this device.
- [CLKWatchFaceLibrary.ErrorCode.notFileURL](./errorcode/notfileurl.md)
  No file was found at the specified URL.
- [CLKWatchFaceLibrary.ErrorCode.invalidFile](./errorcode/invalidfile.md)
  The specified file wasn’t a valid watch face file.
- [CLKWatchFaceLibrary.ErrorCode.permissionDenied](./errorcode/permissiondenied.md)
  The app does not have permission to read the specified file.
- [CLKWatchFaceLibrary.ErrorCode.faceNotAvailable](./errorcode/facenotavailable.md)
  The watch face is not available on this device.
### Enumeration Cases
- [CLKWatchFaceLibrary.ErrorCode.noURL](./errorcode/nourl.md)
### Initializers
- [init?(rawValue: Int)](./errorcode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling Errors
- [class let ErrorDomain: String](./errordomain.md)
  The domain for errors while importing watch faces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkwatchfacelibrary/errorcode)*