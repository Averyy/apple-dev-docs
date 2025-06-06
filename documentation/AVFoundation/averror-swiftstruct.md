# AVError

**Framework**: AVFoundation  
**Kind**: struct

A structure that defines the errors that framework operations can generate.

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
struct AVError
```

## Topics

### Error Domain
- [static var errorDomain: String](averror-swift.struct/errordomain.md)
### Error Codes
- [AVError.Code](averror-swift.struct/code.md)
  An enumeration that defines the errors that framework operations can generate.
- [static var airPlayControllerRequiresInternet: AVError.Code](averror-swift.struct/airplaycontrollerrequiresinternet.md)
  The AirPlay controller requires an internet connection to function.
- [static var airPlayReceiverRequiresInternet: AVError.Code](averror-swift.struct/airplayreceiverrequiresinternet.md)
  The AirPlay receiver requires an internet connection to function.
- [static var airPlayReceiverTemporarilyUnavailable: AVError.Code](averror-swift.struct/airplayreceivertemporarilyunavailable.md)
  An AirPlay receiver is temporarily unavailable.
- [static var applicationIsNotAuthorized: AVError.Code](averror-swift.struct/applicationisnotauthorized.md)
  The app isn’t authorized to play media.
- [static var applicationIsNotAuthorizedToUseDevice: AVError.Code](averror-swift.struct/applicationisnotauthorizedtousedevice.md)
  The user denied this app permission to capture media.
- [static var compositionTrackSegmentsNotContiguous: AVError.Code](averror-swift.struct/compositiontracksegmentsnotcontiguous.md)
  The composition can’t add the source media because it contains gaps.
- [static var contentIsNotAuthorized: AVError.Code](averror-swift.struct/contentisnotauthorized.md)
  The user isn’t authorized to play the media.
- [static var contentIsProtected: AVError.Code](averror-swift.struct/contentisprotected.md)
  The app isn’t authorized to open the media.
- [static var contentIsUnavailable: AVError.Code](averror-swift.struct/contentisunavailable.md)
  The captured content is unavailable.
- [static var contentKeyRequestCancelled: AVError.Code](averror-swift.struct/contentkeyrequestcancelled.md)
  The app canceled a request to retrieve a content key.
- [static var contentNotUpdated: AVError.Code](averror-swift.struct/contentnotupdated.md)
  The system couldn’t update the captured content.
- [static var createContentKeyRequestFailed: AVError.Code](averror-swift.struct/createcontentkeyrequestfailed.md)
  The app couldn’t create a content key request.
- [static var decodeFailed: AVError.Code](averror-swift.struct/decodefailed.md)
  The system failed to decode the media.
- [static var decoderNotFound: AVError.Code](averror-swift.struct/decodernotfound.md)
  The system can’t find a suitable decoder for the media.
- [static var decoderTemporarilyUnavailable: AVError.Code](averror-swift.struct/decodertemporarilyunavailable.md)
  A suitable decoder for the media is temporarily available.
- [static var deviceAlreadyUsedByAnotherSession: AVError.Code](averror-swift.struct/devicealreadyusedbyanothersession.md)
  Your app can’t access the device because another session is currently using it.
- [static var deviceInUseByAnotherApplication: AVError.Code](averror-swift.struct/deviceinusebyanotherapplication.md)
  Your app can’t access the device because another app is currently using it.
- [static var deviceLockedForConfigurationByAnotherProcess: AVError.Code](averror-swift.struct/devicelockedforconfigurationbyanotherprocess.md)
  Your app can’t change device settings because another process currently controls the device.
- [static var deviceNotConnected: AVError.Code](averror-swift.struct/devicenotconnected.md)
  You app can’t access the device because it isn’t connected.
- [static var deviceWasDisconnected: AVError.Code](averror-swift.struct/devicewasdisconnected.md)
  A previously connected device is no longer accessible.
- [static var diskFull: AVError.Code](averror-swift.struct/diskfull.md)
  Recording stopped because the disk is full.
- [static var displayWasDisabled: AVError.Code](averror-swift.struct/displaywasdisabled.md)
  Screen capture failed because the display was inactive.
- [static var encodeFailed: AVError.Code](averror-swift.struct/encodefailed.md)
  The system couldn’t encode the media data.
- [static var encoderNotFound: AVError.Code](averror-swift.struct/encodernotfound.md)
  The requested encoder isn’t found.
- [static var encoderTemporarilyUnavailable: AVError.Code](averror-swift.struct/encodertemporarilyunavailable.md)
  An appropriate encoder isn’t currently available.
- [static var exportFailed: AVError.Code](averror-swift.struct/exportfailed.md)
  The requested export operation failed.
- [static var externalPlaybackNotSupportedForAsset: AVError.Code](averror-swift.struct/externalplaybacknotsupportedforasset.md)
  The current asset doesn’t support playback.
- [static var failedToLoadMediaData: AVError.Code](averror-swift.struct/failedtoloadmediadata.md)
  The system can’t load the requested media data.
- [static var failedToLoadSampleData: AVError.Code](averror-swift.struct/failedtoloadsampledata.md)
  The system can’t load the requested sample data.
- [static var failedToParse: AVError.Code](averror-swift.struct/failedtoparse.md)
  The system can’t parse the media.
- [static var fileAlreadyExists: AVError.Code](averror-swift.struct/filealreadyexists.md)
  A file with the same name exists at the location and you can’t overwrite it.
- [static var fileFailedToParse: AVError.Code](averror-swift.struct/filefailedtoparse.md)
  The file is corrupt or in an unrecognized format.
- [static var fileFormatNotRecognized: AVError.Code](averror-swift.struct/fileformatnotrecognized.md)
  The system can’t open the file because it’s in an unrecognized format.
- [static var fileTypeDoesNotSupportSampleReferences: AVError.Code](averror-swift.struct/filetypedoesnotsupportsamplereferences.md)
  The file type doesn’t support sample references.
- [static var formatUnsupported: AVError.Code](averror-swift.struct/formatunsupported.md)
  The current asset format isn’t supported.
- [static var incompatibleAsset: AVError.Code](averror-swift.struct/incompatibleasset.md)
  You can’t display the media because the device isn’t capable of playing the content.
- [static var incorrectlyConfigured: AVError.Code](averror-swift.struct/incorrectlyconfigured.md)
  The system is incorrectly configured for the requested operation.
- [static var invalidCompositionTrackSegmentDuration: AVError.Code](averror-swift.struct/invalidcompositiontracksegmentduration.md)
  You can’t add the source media because its duration in the destination is invalid.
- [static var invalidCompositionTrackSegmentSourceDuration: AVError.Code](averror-swift.struct/invalidcompositiontracksegmentsourceduration.md)
  You can’t add the source media because it has no duration.
- [static var invalidCompositionTrackSegmentSourceStartTime: AVError.Code](averror-swift.struct/invalidcompositiontracksegmentsourcestarttime.md)
  You can’t add the source media because its start time in the destination is invalid.
- [static var invalidOutputURLPathExtension: AVError.Code](averror-swift.struct/invalidoutputurlpathextension.md)
  The path extension of the output URL is invalid.
- [static var invalidSampleCursor: AVError.Code](averror-swift.struct/invalidsamplecursor.md)
  An invalid sample cursor produced an error.
- [static var invalidSourceMedia: AVError.Code](averror-swift.struct/invalidsourcemedia.md)
  The system couldn’t read the source media.
- [static var invalidVideoComposition: AVError.Code](averror-swift.struct/invalidvideocomposition.md)
  You attempted to present an unsupported video composition.
- [static var malformedDepth: AVError.Code](averror-swift.struct/malformeddepth.md)
  The depth data isn’t properly structured.
- [static var maximumDurationReached: AVError.Code](averror-swift.struct/maximumdurationreached.md)
  The recording stopped because it reached the file’s maximum duration.
- [static var maximumFileSizeReached: AVError.Code](averror-swift.struct/maximumfilesizereached.md)
  The recording stopped because it reached the file’s maximum size.
- [static var maximumNumberOfSamplesForFileFormatReached: AVError.Code](averror-swift.struct/maximumnumberofsamplesforfileformatreached.md)
  The recording stopped because it reached the file’s maximum number of samples.
- [static var maximumStillImageCaptureRequestsExceeded: AVError.Code](averror-swift.struct/maximumstillimagecapturerequestsexceeded.md)
  Your app can’t take a photo because there are too many unfinished photo capture requests.
- [static var mediaChanged: AVError.Code](averror-swift.struct/mediachanged.md)
  Recording stopped because the format of the source media changed.
- [static var mediaDiscontinuity: AVError.Code](averror-swift.struct/mediadiscontinuity.md)
  Recording stopped because there was an interruption in the input media.
- [static var mediaServicesWereReset: AVError.Code](averror-swift.struct/mediaserviceswerereset.md)
  The system couldn’t perform the operation because media services were unavailable.
- [static var noCompatibleAlternatesForExternalDisplay: AVError.Code](averror-swift.struct/nocompatiblealternatesforexternaldisplay.md)
  The system found no compatible external displays.
- [static var noDataCaptured: AVError.Code](averror-swift.struct/nodatacaptured.md)
  The recording failed because the system received no data.
- [static var noImageAtTime: AVError.Code](averror-swift.struct/noimageattime.md)
  No image is available in the media at the indicated time.
- [static var noLongerPlayable: AVError.Code](averror-swift.struct/nolongerplayable.md)
  The asset is no longer playable.
- [static var noSourceTrack: AVError.Code](averror-swift.struct/nosourcetrack.md)
  The asset doesn’t contain a source track.
- [static var operationCancelled: AVError.Code](averror-swift.struct/operationcancelled.md)
  The asset handled a request to cancel loading a property value asynchronously.
- [static var operationInterrupted: AVError.Code](averror-swift.struct/operationinterrupted.md)
  An interruption occurred while performing a reading or writing operation.
- [static var operationNotAllowed: AVError.Code](averror-swift.struct/operationnotallowed.md)
  The requested operation isn’t allowed.
- [static var operationNotSupportedForAsset: AVError.Code](averror-swift.struct/operationnotsupportedforasset.md)
  Your app attempted to perform an unsupported operation with the asset.
- [static var operationNotSupportedForPreset: AVError.Code](averror-swift.struct/operationnotsupportedforpreset.md)
  Your app attempted to perform an unsupported operation for the current preset.
- [static var outOfMemory: AVError.Code](averror-swift.struct/outofmemory.md)
  The operation couldn’t finish because there isn’t enough memory available to process the media.
- [static var recordingAlreadyInProgress: AVError.Code](averror-swift.struct/recordingalreadyinprogress.md)
  Your app attempted to start recording a movie file while an existing recording is underway.
- [static var referenceForbiddenByReferencePolicy: AVError.Code](averror-swift.struct/referenceforbiddenbyreferencepolicy.md)
  The current reference restrictions prevent the system from loading referenced media.
- [static var rosettaNotInstalled: AVError.Code](averror-swift.struct/rosettanotinstalled.md)
  The system doesn’t have Rosetta installed and can’t perform the requested operation.
- [static var sandboxExtensionDenied: AVError.Code](averror-swift.struct/sandboxextensiondenied.md)
  The system denied issuing the sandbox extension.
- [static var screenCaptureFailed: AVError.Code](averror-swift.struct/screencapturefailed.md)
  An unexpected problem occurred that prevented screen capture.
- [static var segmentStartedWithNonSyncSample: AVError.Code](averror-swift.struct/segmentstartedwithnonsyncsample.md)
  The operation attempted to write a new MPEG-4 segment that didn’t start with a sync sample.
- [static var serverIncorrectlyConfigured: AVError.Code](averror-swift.struct/serverincorrectlyconfigured.md)
  The configuration of the HTTP server that streams the media resource isn’t correct.
- [static var sessionConfigurationChanged: AVError.Code](averror-swift.struct/sessionconfigurationchanged.md)
  Recording stopped because the configuration of media sources and destinations changed.
- [static var sessionHardwareCostOverage: AVError.Code](averror-swift.struct/sessionhardwarecostoverage.md)
  Your app requested too many camera hardware resources.
- [static var sessionNotRunning: AVError.Code](averror-swift.struct/sessionnotrunning.md)
  The recording couldn’t start because the session isn’t running.
- [static var sessionWasInterrupted: AVError.Code](averror-swift.struct/sessionwasinterrupted.md)
  The recording stopped because the system interrupted the audio session.
- [static var toneMappingFailed: AVError.Code](averror-swift.struct/tonemappingfailed.md)
  The requested tone mapping failed.
- [static var torchLevelUnavailable: AVError.Code](averror-swift.struct/torchlevelunavailable.md)
  The specified torch level is valid but currently unavailable, possibly due to overheating.
- [static var undecodableMediaData: AVError.Code](averror-swift.struct/undecodablemediadata.md)
  The system couldn’t decode the media data.
- [static var unknown: AVError.Code](averror-swift.struct/unknown.md)
  An unknown error occurred.
- [static var unsupportedDeviceActiveFormat: AVError.Code](averror-swift.struct/unsupporteddeviceactiveformat.md)
  The capture session doesn’t support the camera device’s active format.
- [static var unsupportedOutputSettings: AVError.Code](averror-swift.struct/unsupportedoutputsettings.md)
  Your app requested unsupported output settings.
- [static var videoCompositorFailed: AVError.Code](averror-swift.struct/videocompositorfailed.md)
  The compositor couldn’t composite video frames.
- [static var deviceIsNotAvailableInBackground: AVError.Code](averror-swift.struct/deviceisnotavailableinbackground.md)
  You attempted to start a capture session in the background, which isn’t allowed in iOS.
### Error Properties
- [var device: AVCaptureDevice?](averror-swift.struct/device-5iio4.md)
  The capture device in use.
- [var fileSize: Int64?](averror-swift.struct/filesize.md)
  The asset file size.
- [var fileType: AVFileType?](averror-swift.struct/filetype.md)
  The asset file type.
- [var mediaSubtypes: [Int]?](averror-swift.struct/mediasubtypes.md)
  An array of media subtypes.
- [var mediaType: AVMediaType?](averror-swift.struct/mediatype-7ksjb.md)
  The asset media type.
- [var persistentTrackID: CMPersistentTrackID?](averror-swift.struct/persistenttrackid.md)
  The persistent track ID, if the track exists.
- [var presentationTimeStamp: CMTime?](averror-swift.struct/presentationtimestamp.md)
  The presentation time stamp.
- [var processID: Int?](averror-swift.struct/processid.md)
  The process ID.
- [var recordingSuccessfullyFinished: Bool?](averror-swift.struct/recordingsuccessfullyfinished.md)
  A Boolean value that indicates whether recording finished successfully.
- [var time: CMTime?](averror-swift.struct/time.md)
  The time duration of the error.
### User Info Keys
- [let AVErrorDeviceKey: String](averrordevicekey.md)
  The user information key to retrieve the device name.
- [let AVErrorDiscontinuityFlagsKey: String](averrordiscontinuityflagskey.md)
  The user information key to retrieve discontinuity flags.
- [let AVErrorFileSizeKey: String](averrorfilesizekey.md)
  The user information key to retrieve the file size in bytes.
- [let AVErrorFileTypeKey: String](averrorfiletypekey.md)
  The user information key to retrieve the file type.
- [let AVErrorMediaTypeKey: String](averrormediatypekey.md)
  The user information key to retrieve the media type.
- [let AVErrorMediaSubTypeKey: String](averrormediasubtypekey.md)
  The user information key to retrieve the media subtype.
- [let AVErrorPersistentTrackIDKey: String](averrorpersistenttrackidkey.md)
  The user information key to retrieve the track’s persistent identifier.
- [let AVErrorPIDKey: String](averrorpidkey.md)
  The user information key to retrieve the process ID value.
- [let AVErrorPresentationTimeStampKey: String](averrorpresentationtimestampkey.md)
  The user information key to retrieve the presentation time stamp.
- [let AVErrorRecordingSuccessfullyFinishedKey: String](averrorrecordingsuccessfullyfinishedkey.md)
  The user information key to retrieve a Boolean value that indicates whether recording finished successfully.
- [let AVErrorTimeKey: String](averrortimekey.md)
  The user information key to retrieve the error time.
### Type Properties
- [static var mediaExtensionConflict: AVError.Code](averror-swift.struct/mediaextensionconflict.md)
- [static var mediaExtensionDisabled: AVError.Code](averror-swift.struct/mediaextensiondisabled.md)
### Instance Properties
- [var device: String?](averror-swift.struct/device-1qfzr.md)
- [var mediaType: String?](averror-swift.struct/mediatype-5d8ie.md)
  The media type.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let AVFoundationErrorDomain: String](avfoundationerrordomain.md)
  The error domain of AVFoundation errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/averror-swift.struct)*