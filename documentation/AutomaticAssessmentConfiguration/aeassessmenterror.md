# AEAssessmentError

**Framework**: Automatic Assessment Configuration  
**Kind**: struct

Errors issued by an assessment session to its delegate.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 14.0+
- macOS 10.15.4+

## Declaration

```swift
struct AEAssessmentError
```

## Topics

### Error codes
- [static var unknown: AEAssessmentError.Code](aeassessmenterror/unknown.md)
  The session encountered an unknown error.
- [static var unsupportedPlatform: AEAssessmentError.Code](aeassessmenterror/unsupportedplatform.md)
  The feature isn’t supported on this platform.
- [AEAssessmentError.Code](aeassessmenterror/code.md)
  Error codes that the framework returns if a session fails.
### Error characteristics
- [let AEAssessmentErrorDomain: String](aeassessmenterrordomain.md)
  A constant representing the error domain that the framework uses when issuing errors.
### Type Properties
- [static var configurationUpdatesNotSupported: AEAssessmentError.Code](aeassessmenterror/configurationupdatesnotsupported.md)
- [static var errorDomain: String](aeassessmenterror/errordomain.md)
- [static var multipleParticipantsNotSupported: AEAssessmentError.Code](aeassessmenterror/multipleparticipantsnotsupported.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [AEAssessmentError.Code](aeassessmenterror/code.md)
  Error codes that the framework returns if a session fails.
- [let AEAssessmentErrorDomain: String](aeassessmenterrordomain.md)
  A constant representing the error domain that the framework uses when issuing errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmenterror)*