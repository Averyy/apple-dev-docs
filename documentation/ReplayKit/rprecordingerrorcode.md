# RPRecordingErrorCode

**Framework**: ReplayKit  
**Kind**: enum

The ReplayKit error domain codes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum RPRecordingErrorCode
```

## Topics

### Errors
- [RPRecordingErrorCode.activePhoneCall](rprecordingerrorcode/activephonecall.md)
  Unable to record due to an active phone call.
- [RPRecordingErrorCode.attemptToStartInRecordingState](rprecordingerrorcode/attempttostartinrecordingstate.md)
  Attempted to start a recording that’s already in a recording state.
- [RPRecordingErrorCode.attemptToStopNonRecording](rprecordingerrorcode/attempttostopnonrecording.md)
  Attempted to stop a recording that’s not in a recording state.
- [RPRecordingErrorCode.broadcastInvalidSession](rprecordingerrorcode/broadcastinvalidsession.md)
  Attempted to start a broadcast without a prior session.
- [RPRecordingErrorCode.broadcastSetupFailed](rprecordingerrorcode/broadcastsetupfailed.md)
  The broadcast set up failed.
- [RPRecordingErrorCode.carPlay](rprecordingerrorcode/carplay.md)
  Failed to start recording because CarPlay is active.
- [RPRecordingErrorCode.codeSuccessful](rprecordingerrorcode/codesuccessful.md)
  Successfully saved the recording to the Camera Roll.
- [RPRecordingErrorCode.contentResize](rprecordingerrorcode/contentresize.md)
  Recording interrupted by multitasking and content resizing.
- [RPRecordingErrorCode.disabled](rprecordingerrorcode/disabled.md)
  Recording disabled via parental controls.
- [RPRecordingErrorCode.entitlements](rprecordingerrorcode/entitlements.md)
  Recording failed due to missing entitlements.
- [RPRecordingErrorCode.failed](rprecordingerrorcode/failed.md)
  Recording error occurred.
- [RPRecordingErrorCode.failedApplicationConnectionInterrupted](rprecordingerrorcode/failedapplicationconnectioninterrupted.md)
  The recording failed because the app’s connection was interrupted.
- [RPRecordingErrorCode.failedApplicationConnectionInvalid](rprecordingerrorcode/failedapplicationconnectioninvalid.md)
  The recording failed because the app’s connection is invalid.
- [RPRecordingErrorCode.failedAssetWriterExportCanceled](rprecordingerrorcode/failedassetwriterexportcanceled.md)
  The recording failed because the user canceled the export.
- [RPRecordingErrorCode.failedAssetWriterExportFailed](rprecordingerrorcode/failedassetwriterexportfailed.md)
  The recording failed due to an error exporting the movie.
- [RPRecordingErrorCode.failedAssetWriterFailedToSave](rprecordingerrorcode/failedassetwriterfailedtosave.md)
  The recording failed due to an asset writer failure.
- [RPRecordingErrorCode.failedAssetWriterInWrongState](rprecordingerrorcode/failedassetwriterinwrongstate.md)
  The recording failed because the asset writer is in an invalid state.
- [RPRecordingErrorCode.failedIncorrectTimeStamps](rprecordingerrorcode/failedincorrecttimestamps.md)
  The recording failed due to malformed start and end time intervals.
- [RPRecordingErrorCode.failedMediaServicesFailure](rprecordingerrorcode/failedmediaservicesfailure.md)
  The recording failed due to a mediaservices daemon failure.
- [RPRecordingErrorCode.failedNoAssetWriter](rprecordingerrorcode/failednoassetwriter.md)
  The recording failed because there is no asset writer available.
- [RPRecordingErrorCode.failedNoMatchingApplicationContext](rprecordingerrorcode/failednomatchingapplicationcontext.md)
  The context identifier doesn’t match the app identifier.
- [RPRecordingErrorCode.failedToObtainURL](rprecordingerrorcode/failedtoobtainurl.md)
  The recording failed due to a failure to obtain the URL.
- [RPRecordingErrorCode.failedToProcessFirstSample](rprecordingerrorcode/failedtoprocessfirstsample.md)
  The recording failed because the asset writer failed to process the first media sample.
- [RPRecordingErrorCode.failedToRemoveFile](rprecordingerrorcode/failedtoremovefile.md)
  The recording failed because the temporary file wasn’t removed.
- [RPRecordingErrorCode.failedToStartCaptureStack](rprecordingerrorcode/failedtostartcapturestack.md)
  The system failed to configure the app for A/V recording.
- [RPRecordingErrorCode.failedToStart](rprecordingerrorcode/failedtostart.md)
  Recording failed to start.
- [RPRecordingErrorCode.failedToSave](rprecordingerrorcode/failedtosave.md)
  The recording failed to save.
- [RPRecordingErrorCode.filePermissions](rprecordingerrorcode/filepermissions.md)
  The recording failed due to a file permission error.
- [RPRecordingErrorCode.insufficientStorage](rprecordingerrorcode/insufficientstorage.md)
  Not enough storage available on the device.
- [RPRecordingErrorCode.interrupted](rprecordingerrorcode/interrupted.md)
  Recording interrupted by another app.
- [RPRecordingErrorCode.invalidParameter](rprecordingerrorcode/invalidparameter.md)
  The recording failed because of an invalid parameter.
- [RPRecordingErrorCode.photoFailure](rprecordingerrorcode/photofailure.md)
  Failed saving the video the Camera Roll.
- [RPRecordingErrorCode.recordingInvalidSession](rprecordingerrorcode/recordinginvalidsession.md)
  Attempted to start an invalid recording session.
- [RPRecordingErrorCode.systemDormancy](rprecordingerrorcode/systemdormancy.md)
  Recording forced to end by the user pressing the power button.
- [RPRecordingErrorCode.unknown](rprecordingerrorcode/unknown.md)
  Error cause unknown.
- [RPRecordingErrorCode.userDeclined](rprecordingerrorcode/userdeclined.md)
  User declined recording request.
- [RPRecordingErrorCode.videoMixingFailure](rprecordingerrorcode/videomixingfailure.md)
  The recording failed due to an A/V mixing failure.
### Enumeration Cases
- [RPRecordingErrorCode.exportClipToURLInProgress](rprecordingerrorcode/exportcliptourlinprogress.md)
### Initializers
- [init?(rawValue: Int)](rprecordingerrorcode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let RPRecordingErrorDomain: String](rprecordingerrordomain.md)
  The ReplayKit error domain.
- [let SCStreamErrorDomain: String](scstreamerrordomain.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode)*