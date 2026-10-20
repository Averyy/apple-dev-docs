# AEAssessmentError.Code

**Framework**: Automatic Assessment Configuration  
**Kind**: enum  
**Role**: Enumeration

Error codes that the framework returns if a session fails.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 14.0+
- macOS 10.15.4+

## Declaration

```swift
enum Code
```

```c
enum AEAssessmentErrorCode : NSInteger;
```

## Topics

### Possible errors
- [AEAssessmentError.Code.configurationUpdatesNotSupported](./code/configurationupdatesnotsupported.md)
  An active session fails to update its configuration because configuration updates are not supported by the current device or platform.
- [AEAssessmentError.Code.multipleParticipantsNotSupported](./code/multipleparticipantsnotsupported.md)
  A session fails to begin or update with a configuration that contains one or more participant applications because mulitple participant configurations are not supported by the device or platform.
- [AEAssessmentError.Code.unknown](./code/unknown.md)
  The session encountered an unknown error.
- [AEAssessmentError.Code.unsupportedPlatform](./code/unsupportedplatform.md)
  The feature isn’t supported on this platform.
### Enumeration Cases
- [AEAssessmentError.Code.requiredParticipantsNotAvailable](./code/requiredparticipantsnotavailable.md)
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

### Errors
- [struct AEAssessmentError](../aeassessmenterror.md)
  Errors issued by an assessment session to its delegate.
- [let AEAssessmentErrorDomain: String](../aeassessmenterrordomain.md)
  A constant representing the error domain that the framework uses when issuing errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmenterror/code)*