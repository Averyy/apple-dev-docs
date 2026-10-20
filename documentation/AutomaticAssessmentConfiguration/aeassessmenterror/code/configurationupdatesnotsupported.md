# AEAssessmentError.Code.configurationUpdatesNotSupported

**Framework**: Automatic Assessment Configuration  
**Kind**: case  
**Role**: Case

An active session fails to update its configuration because configuration updates are not supported by the current device or platform.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- macOS 14.5+

## Declaration

```swift
case configurationUpdatesNotSupported
```

```c
AEAssessmentErrorConfigurationUpdatesNotSupported
```

## See Also

### Possible errors
- [AEAssessmentError.Code.multipleParticipantsNotSupported](./multipleparticipantsnotsupported.md)
  A session fails to begin or update with a configuration that contains one or more participant applications because mulitple participant configurations are not supported by the device or platform.
- [AEAssessmentError.Code.unknown](./unknown.md)
  The session encountered an unknown error.
- [AEAssessmentError.Code.unsupportedPlatform](./unsupportedplatform.md)
  The feature isn’t supported on this platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmenterror/code/configurationupdatesnotsupported)*