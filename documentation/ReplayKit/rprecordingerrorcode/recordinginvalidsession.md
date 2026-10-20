# RPRecordingErrorCode.recordingInvalidSession

**Framework**: ReplayKit  
**Kind**: case  
**Role**: Case

Attempted to start an invalid recording session.

**Availability**:
- iOS 9.0+ - Deprecated in 27.0
- iPadOS 9.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use ScreenCaptureKit instead

## Declaration

```swift
case recordingInvalidSession
```

```c
RPRecordingErrorRecordingInvalidSession
```

## See Also

### Errors
- [RPRecordingErrorCode.activePhoneCall](./activephonecall.md)
  Unable to record due to an active phone call.
- [RPRecordingErrorCode.attemptToStartInRecordingState](./attempttostartinrecordingstate.md)
  Attempted to start a recording that’s already in a recording state.
- [RPRecordingErrorCode.attemptToStopNonRecording](./attempttostopnonrecording.md)
  Attempted to stop a recording that’s not in a recording state.
- [RPRecordingErrorCode.broadcastInvalidSession](./broadcastinvalidsession.md)
  Attempted to start a broadcast without a prior session.
- [RPRecordingErrorCode.broadcastSetupFailed](./broadcastsetupfailed.md)
  The broadcast set up failed.
- [RPRecordingErrorCode.carPlay](./carplay.md)
  Failed to start recording because CarPlay is active.
- [RPRecordingErrorCode.codeSuccessful](./codesuccessful.md)
  Successfully saved the recording to the Camera Roll.
- [RPRecordingErrorCode.contentResize](./contentresize.md)
  Recording interrupted by multitasking and content resizing.
- [RPRecordingErrorCode.disabled](./disabled.md)
  Recording disabled via parental controls.
- [RPRecordingErrorCode.entitlements](./entitlements.md)
  Recording failed due to missing entitlements.
- [RPRecordingErrorCode.failed](./failed.md)
  Recording error occurred.
- [RPRecordingErrorCode.failedApplicationConnectionInterrupted](./failedapplicationconnectioninterrupted.md)
  The recording failed because the app’s connection was interrupted.
- [RPRecordingErrorCode.failedApplicationConnectionInvalid](./failedapplicationconnectioninvalid.md)
  The recording failed because the app’s connection is invalid.
- [RPRecordingErrorCode.failedAssetWriterExportCanceled](./failedassetwriterexportcanceled.md)
  The recording failed because the user canceled the export.
- [RPRecordingErrorCode.failedAssetWriterExportFailed](./failedassetwriterexportfailed.md)
  The recording failed due to an error exporting the movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/recordinginvalidsession)*