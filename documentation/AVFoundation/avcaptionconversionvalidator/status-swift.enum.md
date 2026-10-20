# AVCaptionConversionValidator.Status

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the status of a validator.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
enum Status
```

```c
enum AVCaptionConversionValidatorStatus : NSInteger;
```

## Topics

### Validation statuses
- [AVCaptionConversionValidator.Status.unknown](./status-swift.enum/unknown.md)
  A status that indicates the system didn’t initialize the validation operation.
- [AVCaptionConversionValidator.Status.validating](./status-swift.enum/validating.md)
  A status that indicates the system validation is in progress.
- [AVCaptionConversionValidator.Status.completed](./status-swift.enum/completed.md)
  A status that indicates the system validation is complete.
- [AVCaptionConversionValidator.Status.stopped](./status-swift.enum/stopped.md)
  A status that indicates the system validation stopped prior to completion.
### Initializers
- [init?(rawValue: Int)](./status-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Checking the status
- [var status: AVCaptionConversionValidator.Status](./status-swift.property.md)
  A value that indicates the status of validation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionconversionvalidator/status-swift.enum)*