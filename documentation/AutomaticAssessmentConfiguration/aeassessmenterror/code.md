# AEAssessmentError.Code

**Framework**: Automatic Assessment Configuration  
**Kind**: enum

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

## Topics

### Possible errors
- [AEAssessmentError.Code.configurationUpdatesNotSupported](aeassessmenterror/code/configurationupdatesnotsupported.md)
  An active session fails to update its configuration because configuration updates are not supported by the current device or platform.
- [AEAssessmentError.Code.multipleParticipantsNotSupported](aeassessmenterror/code/multipleparticipantsnotsupported.md)
  A session fails to begin or update with a configuration that contains one or more participant applications because mulitple participant configurations are not supported by the device or platform.
- [AEAssessmentError.Code.unknown](aeassessmenterror/code/unknown.md)
  The session encountered an unknown error.
- [AEAssessmentError.Code.unsupportedPlatform](aeassessmenterror/code/unsupportedplatform.md)
  The feature isn’t supported on this platform.
### Enumeration Cases
- [AEAssessmentError.Code.requiredParticipantsNotAvailable](aeassessmenterror/code/requiredparticipantsnotavailable.md)
### Initializers
- [init?(rawValue: Int)](aeassessmenterror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AEAssessmentError](aeassessmenterror.md)
  Errors issued by an assessment session to its delegate.
- [let AEAssessmentErrorDomain: String](aeassessmenterrordomain.md)
  A constant representing the error domain that the framework uses when issuing errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmenterror/code)*