# AVError.Code

**Framework**: AVFoundation  
**Kind**: enum

An enumeration that defines the errors that framework operations can generate.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum Code
```

## Topics

### Error Codes
- [AVError.Code.airPlayControllerRequiresInternet](averror-swift.struct/code/airplaycontrollerrequiresinternet.md)
  The AirPlay controller requires an internet connection to function.
- [AVError.Code.airPlayReceiverRequiresInternet](averror-swift.struct/code/airplayreceiverrequiresinternet.md)
  The AirPlay receiver requires an internet connection to function.
- [AVError.Code.airPlayReceiverTemporarilyUnavailable](averror-swift.struct/code/airplayreceivertemporarilyunavailable.md)
  An AirPlay receiver is temporarily unavailable.
- [AVError.Code.applicationIsNotAuthorized](averror-swift.struct/code/applicationisnotauthorized.md)
  The app isn’t authorized to play media.
- [AVError.Code.applicationIsNotAuthorizedToUseDevice](averror-swift.struct/code/applicationisnotauthorizedtousedevice.md)
  The user denied this app permission to capture media.
- [AVError.Code.compositionTrackSegmentsNotContiguous](averror-swift.struct/code/compositiontracksegmentsnotcontiguous.md)
  The composition can’t add the source media because it contains gaps.
- [AVError.Code.contentIsNotAuthorized](averror-swift.struct/code/contentisnotauthorized.md)
  The user isn’t authorized to play the media.
- [AVError.Code.contentIsProtected](averror-swift.struct/code/contentisprotected.md)
  The app isn’t authorized to open the media.
- [AVError.Code.contentIsUnavailable](averror-swift.struct/code/contentisunavailable.md)
  The captured content is unavailable.
- [AVError.Code.contentKeyRequestCancelled](averror-swift.struct/code/contentkeyrequestcancelled.md)
  The app canceled a request to retrieve a content key.
- [AVError.Code.contentNotUpdated](averror-swift.struct/code/contentnotupdated.md)
  The system couldn’t update the captured content.
- [AVError.Code.createContentKeyRequestFailed](averror-swift.struct/code/createcontentkeyrequestfailed.md)
  The app couldn’t create a content key request.
- [AVError.Code.decodeFailed](averror-swift.struct/code/decodefailed.md)
  The system failed to decode the media.
- [AVError.Code.decoderNotFound](averror-swift.struct/code/decodernotfound.md)
  The system can’t find a suitable decoder for the media.
- [AVError.Code.decoderTemporarilyUnavailable](averror-swift.struct/code/decodertemporarilyunavailable.md)
  A suitable decoder for the media is temporarily available.
- [AVError.Code.deviceAlreadyUsedByAnotherSession](averror-swift.struct/code/devicealreadyusedbyanothersession.md)
  Your app can’t access the device because another session is currently using it.
- [AVError.Code.deviceInUseByAnotherApplication](averror-swift.struct/code/deviceinusebyanotherapplication.md)
  Your app can’t access the device because another app is currently using it.
- [AVError.Code.deviceLockedForConfigurationByAnotherProcess](averror-swift.struct/code/devicelockedforconfigurationbyanotherprocess.md)
  Your app can’t change device settings because another process currently controls the device.
- [AVError.Code.deviceNotConnected](averror-swift.struct/code/devicenotconnected.md)
  You app can’t access the device because it isn’t connected.
- [AVError.Code.deviceWasDisconnected](averror-swift.struct/code/devicewasdisconnected.md)
  A previously connected device is no longer accessible.
- [AVError.Code.diskFull](averror-swift.struct/code/diskfull.md)
  Recording stopped because the disk is full.
- [AVError.Code.displayWasDisabled](averror-swift.struct/code/displaywasdisabled.md)
  Screen capture failed because the display was inactive.
- [AVError.Code.encodeFailed](averror-swift.struct/code/encodefailed.md)
  The system couldn’t encode the media data.
- [AVError.Code.encoderNotFound](averror-swift.struct/code/encodernotfound.md)
  The requested encoder isn’t found.
- [AVError.Code.encoderTemporarilyUnavailable](averror-swift.struct/code/encodertemporarilyunavailable.md)
  An appropriate encoder isn’t currently available.
- [AVError.Code.exportFailed](averror-swift.struct/code/exportfailed.md)
  The requested export operation failed.
- [AVError.Code.externalPlaybackNotSupportedForAsset](averror-swift.struct/code/externalplaybacknotsupportedforasset.md)
  The current asset doesn’t support playback.
- [AVError.Code.failedToLoadMediaData](averror-swift.struct/code/failedtoloadmediadata.md)
  The system can’t load the requested media data.
- [AVError.Code.failedToLoadSampleData](averror-swift.struct/code/failedtoloadsampledata.md)
  The system can’t load the requested sample data.
- [AVError.Code.failedToParse](averror-swift.struct/code/failedtoparse.md)
  The system can’t parse the media.
- [AVError.Code.fileAlreadyExists](averror-swift.struct/code/filealreadyexists.md)
  A file with the same name exists at the location and you can’t overwrite it.
- [AVError.Code.fileFailedToParse](averror-swift.struct/code/filefailedtoparse.md)
  The file is corrupt or in an unrecognized format.
- [AVError.Code.fileFormatNotRecognized](averror-swift.struct/code/fileformatnotrecognized.md)
  The system can’t open the file because it’s in an unrecognized format.
- [AVError.Code.fileTypeDoesNotSupportSampleReferences](averror-swift.struct/code/filetypedoesnotsupportsamplereferences.md)
  The file type doesn’t support sample references.
- [AVError.Code.formatUnsupported](averror-swift.struct/code/formatunsupported.md)
  The current asset format isn’t supported.
- [AVError.Code.incompatibleAsset](averror-swift.struct/code/incompatibleasset.md)
  You can’t display the media because the device isn’t capable of playing the content.
- [AVError.Code.incorrectlyConfigured](averror-swift.struct/code/incorrectlyconfigured.md)
  The system is incorrectly configured for the requested operation.
- [AVError.Code.invalidCompositionTrackSegmentDuration](averror-swift.struct/code/invalidcompositiontracksegmentduration.md)
  You can’t add the source media because its duration in the destination is invalid.
- [AVError.Code.invalidCompositionTrackSegmentSourceDuration](averror-swift.struct/code/invalidcompositiontracksegmentsourceduration.md)
  You can’t add the source media because it has no duration.
- [AVError.Code.invalidCompositionTrackSegmentSourceStartTime](averror-swift.struct/code/invalidcompositiontracksegmentsourcestarttime.md)
  You can’t add the source media because its start time in the destination is invalid.
- [AVError.Code.invalidOutputURLPathExtension](averror-swift.struct/code/invalidoutputurlpathextension.md)
  The path extension of the output URL is invalid.
- [AVError.Code.invalidSampleCursor](averror-swift.struct/code/invalidsamplecursor.md)
  An invalid sample cursor produced an error.
- [AVError.Code.invalidSourceMedia](averror-swift.struct/code/invalidsourcemedia.md)
  The system couldn’t read the source media.
- [AVError.Code.invalidVideoComposition](averror-swift.struct/code/invalidvideocomposition.md)
  You attempted to present an unsupported video composition.
- [AVError.Code.malformedDepth](averror-swift.struct/code/malformeddepth.md)
  The depth data isn’t properly structured.
- [AVError.Code.maximumDurationReached](averror-swift.struct/code/maximumdurationreached.md)
  The recording stopped because it reached the file’s maximum duration.
- [AVError.Code.maximumFileSizeReached](averror-swift.struct/code/maximumfilesizereached.md)
  The recording stopped because it reached the file’s maximum size.
- [AVError.Code.maximumNumberOfSamplesForFileFormatReached](averror-swift.struct/code/maximumnumberofsamplesforfileformatreached.md)
  The recording stopped because it reached the file’s maximum number of samples.
- [AVError.Code.maximumStillImageCaptureRequestsExceeded](averror-swift.struct/code/maximumstillimagecapturerequestsexceeded.md)
  Your app can’t take a photo because there are too many unfinished photo capture requests.
- [AVError.Code.mediaChanged](averror-swift.struct/code/mediachanged.md)
  Recording stopped because the format of the source media changed.
- [AVError.Code.mediaDiscontinuity](averror-swift.struct/code/mediadiscontinuity.md)
  Recording stopped because there was an interruption in the input media.
- [AVError.Code.mediaServicesWereReset](averror-swift.struct/code/mediaserviceswerereset.md)
  The system couldn’t perform the operation because media services were unavailable.
- [AVError.Code.noCompatibleAlternatesForExternalDisplay](averror-swift.struct/code/nocompatiblealternatesforexternaldisplay.md)
  The system found no compatible external displays.
- [AVError.Code.noDataCaptured](averror-swift.struct/code/nodatacaptured.md)
  The recording failed because the system received no data.
- [AVError.Code.noImageAtTime](averror-swift.struct/code/noimageattime.md)
  No image is available in the media at the indicated time.
- [AVError.Code.noLongerPlayable](averror-swift.struct/code/nolongerplayable.md)
  The asset is no longer playable.
- [AVError.Code.noSourceTrack](averror-swift.struct/code/nosourcetrack.md)
  The asset doesn’t contain a source track.
- [AVError.Code.operationCancelled](averror-swift.struct/code/operationcancelled.md)
  The asset handled a request to cancel loading a property value asynchronously.
- [AVError.Code.operationInterrupted](averror-swift.struct/code/operationinterrupted.md)
  An interruption occurred while performing a reading or writing operation.
- [AVError.Code.operationNotAllowed](averror-swift.struct/code/operationnotallowed.md)
  The requested operation isn’t allowed.
- [AVError.Code.operationNotSupportedForAsset](averror-swift.struct/code/operationnotsupportedforasset.md)
  Your app attempted to perform an unsupported operation with the asset.
- [AVError.Code.operationNotSupportedForPreset](averror-swift.struct/code/operationnotsupportedforpreset.md)
  Your app attempted to perform an unsupported operation for the current preset.
- [AVError.Code.outOfMemory](averror-swift.struct/code/outofmemory.md)
  The operation couldn’t finish because there isn’t enough memory available to process the media.
- [AVError.Code.recordingAlreadyInProgress](averror-swift.struct/code/recordingalreadyinprogress.md)
  Your app attempted to start recording a movie file while an existing recording is underway.
- [AVError.Code.referenceForbiddenByReferencePolicy](averror-swift.struct/code/referenceforbiddenbyreferencepolicy.md)
  The current reference restrictions prevent the system from loading referenced media.
- [AVError.Code.rosettaNotInstalled](averror-swift.struct/code/rosettanotinstalled.md)
  The system doesn’t have Rosetta installed and can’t perform the requested operation.
- [AVError.Code.sandboxExtensionDenied](averror-swift.struct/code/sandboxextensiondenied.md)
  The system denied issuing the sandbox extension.
- [AVError.Code.screenCaptureFailed](averror-swift.struct/code/screencapturefailed.md)
  An unexpected problem occurred that prevented screen capture.
- [AVError.Code.segmentStartedWithNonSyncSample](averror-swift.struct/code/segmentstartedwithnonsyncsample.md)
  The operation attempted to write a new MPEG-4 segment that didn’t start with a sync sample.
- [AVError.Code.serverIncorrectlyConfigured](averror-swift.struct/code/serverincorrectlyconfigured.md)
  The configuration of the HTTP server that streams the media resource isn’t correct.
- [AVError.Code.sessionConfigurationChanged](averror-swift.struct/code/sessionconfigurationchanged.md)
  Recording stopped because the configuration of media sources and destinations changed.
- [AVError.Code.sessionHardwareCostOverage](averror-swift.struct/code/sessionhardwarecostoverage.md)
  Your app requested too many camera hardware resources.
- [AVError.Code.sessionNotRunning](averror-swift.struct/code/sessionnotrunning.md)
  The recording couldn’t start because the session isn’t running.
- [AVError.Code.sessionWasInterrupted](averror-swift.struct/code/sessionwasinterrupted.md)
  The recording stopped because the system interrupted the audio session.
- [AVError.Code.toneMappingFailed](averror-swift.struct/code/tonemappingfailed.md)
  The requested tone mapping failed.
- [AVError.Code.torchLevelUnavailable](averror-swift.struct/code/torchlevelunavailable.md)
  The specified torch level is valid but currently unavailable, possibly due to overheating.
- [AVError.Code.undecodableMediaData](averror-swift.struct/code/undecodablemediadata.md)
  The system couldn’t decode the media data.
- [AVError.Code.unknown](averror-swift.struct/code/unknown.md)
  An unknown error occurred.
- [AVError.Code.unsupportedDeviceActiveFormat](averror-swift.struct/code/unsupporteddeviceactiveformat.md)
  The capture session doesn’t support the camera device’s active format.
- [AVError.Code.unsupportedOutputSettings](averror-swift.struct/code/unsupportedoutputsettings.md)
  Your app requested unsupported output settings.
- [AVError.Code.videoCompositorFailed](averror-swift.struct/code/videocompositorfailed.md)
  The compositor couldn’t composite video frames.
- [AVError.Code.deviceIsNotAvailableInBackground](averror-swift.struct/code/deviceisnotavailableinbackground.md)
  You attempted to start a capture session in the background, which isn’t allowed in iOS.
### Enumeration Cases
- [AVError.Code.mediaExtensionConflict](averror-swift.struct/code/mediaextensionconflict.md)
- [AVError.Code.mediaExtensionDisabled](averror-swift.struct/code/mediaextensiondisabled.md)
### Initializers
- [init?(rawValue: Int)](averror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/averror-swift.struct/code)*