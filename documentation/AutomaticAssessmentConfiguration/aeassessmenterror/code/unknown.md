# AEAssessmentError.Code.unknown

**Framework**: Automatic Assessment Configuration  
**Kind**: case  
**Role**: Case

The session encountered an unknown error.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 14.0+
- macOS 10.15.4+

## Declaration

```swift
case unknown
```

```c
AEAssessmentErrorUnknown
```

## See Also

### Possible errors
- [AEAssessmentError.Code.configurationUpdatesNotSupported](./configurationupdatesnotsupported.md)
  An active session fails to update its configuration because configuration updates are not supported by the current device or platform.
- [AEAssessmentError.Code.multipleParticipantsNotSupported](./multipleparticipantsnotsupported.md)
  A session fails to begin or update with a configuration that contains one or more participant applications because mulitple participant configurations are not supported by the device or platform.
- [AEAssessmentError.Code.unsupportedPlatform](./unsupportedplatform.md)
  The feature isn’t supported on this platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmenterror/code/unknown)*