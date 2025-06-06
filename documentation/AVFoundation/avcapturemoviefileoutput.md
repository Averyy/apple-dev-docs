# AVCaptureMovieFileOutput

**Framework**: AVFoundation  
**Kind**: class

A capture output that records video and audio to a QuickTime movie file.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
class AVCaptureMovieFileOutput
```

## Mentions

- [Setting Up a Capture Session](setting-up-a-capture-session.md)
- [Recording movies in alternative formats](recording-movies-in-alternative-formats.md)

#### Overview

A movie file output provides a complete file recording interface for writing media data to QuickTime movie files. It includes the ability to configure QuickTime-specific options, including writing metadata collections to each file, specify media encoding options for each track, and specify the interval at which it writes movie fragments.

## Topics

### Creating a movie file output
- [init()](avcapturemoviefileoutput/init.md)
  Creates a new of movie file output.
### Configuring movies
- [var movieFragmentInterval: CMTime](avcapturemoviefileoutput/moviefragmentinterval.md)
  The number of seconds of output that are written per fragment.
- [var metadata: [AVMetadataItem]?](avcapturemoviefileoutput/metadata.md)
  The metadata for the output file.
### Managing output settings
- [func supportedOutputSettingsKeys(for: AVCaptureConnection) -> [String]](avcapturemoviefileoutput/supportedoutputsettingskeys(for:).md)
  Returns a list of supported keys to use in the output settings dictionary.
- [func outputSettings(for: AVCaptureConnection) -> [String : Any]](avcapturemoviefileoutput/outputsettings(for:).md)
  Returns the settings the output uses to encode media from the specified connection.
- [func setOutputSettings([String : Any]?, for: AVCaptureConnection)](avcapturemoviefileoutput/setoutputsettings(_:for:).md)
  Sets the options the output uses to encode media from the given connection while recording.
- [var availableVideoCodecTypes: [AVVideoCodecType]](avcapturemoviefileoutput/availablevideocodectypes.md)
  The video codecs types the output supports for recording movie files.
### Enabling spatial capture
- [var isSpatialVideoCaptureSupported: Bool](avcapturemoviefileoutput/isspatialvideocapturesupported.md)
  A Boolean value that indicates whether a movie file output supports capturing spatial videos.
- [var isSpatialVideoCaptureEnabled: Bool](avcapturemoviefileoutput/isspatialvideocaptureenabled.md)
  A Boolean value that indicates whether a movie file output captures spatial videos.
### Setting orientation
- [func recordsVideoOrientationAndMirroringChangesAsMetadataTrack(for: AVCaptureConnection) -> Bool](avcapturemoviefileoutput/recordsvideoorientationandmirroringchangesasmetadatatrack(for:).md)
  A Boolean value that indicates whether the movie file output records video orientation and mirroring information as a metadata track.
- [func setRecordsVideoOrientationAndMirroringChangesAsMetadataTrack(Bool, for: AVCaptureConnection)](avcapturemoviefileoutput/setrecordsvideoorientationandmirroringchangesasmetadatatrack(_:for:).md)
  Sets whether the movie file output creates a timed metadata track to capture changes to the connection’s video orientation and mirroring.
### Restricting camera switching
- [var isPrimaryConstituentDeviceSwitchingBehaviorForRecordingEnabled: Bool](avcapturemoviefileoutput/isprimaryconstituentdeviceswitchingbehaviorforrecordingenabled.md)
  A Boolean value that indicates whether to restrict constituent device switching behavior during recording.
- [func setPrimaryConstituentDeviceSwitchingBehaviorForRecording(AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior, restrictedSwitchingBehaviorConditions: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions)](avcapturemoviefileoutput/setprimaryconstituentdeviceswitchingbehaviorforrecording(_:restrictedswitchingbehaviorconditions:).md)
  Sets the camera switching behavior to use during recording.
- [var primaryConstituentDeviceSwitchingBehaviorForRecording: AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior](avcapturemoviefileoutput/primaryconstituentdeviceswitchingbehaviorforrecording.md)
  The camera switching behavior to use for recording.
- [var primaryConstituentDeviceRestrictedSwitchingBehaviorConditionsForRecording: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](avcapturemoviefileoutput/primaryconstituentdevicerestrictedswitchingbehaviorconditionsforrecording.md)
  The conditions during which camera switching may occur while recording.

## Relationships

### Inherits From
- [AVCaptureFileOutput](avcapturefileoutput.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Recording movies in alternative formats](recording-movies-in-alternative-formats.md)
  Change the default format for capturing movie files.
- [class AVCaptureAudioFileOutput](avcaptureaudiofileoutput.md)
  A capture output that records audio and saves the recorded audio to a file.
- [class AVCaptureFileOutput](avcapturefileoutput.md)
  The abstract superclass for capture outputs that can record captured data to a file.
- [protocol AVCaptureFileOutputDelegate](avcapturefileoutputdelegate.md)
  Methods for monitoring or controlling the output of a media file capture.
- [protocol AVCaptureFileOutputRecordingDelegate](avcapturefileoutputrecordingdelegate.md)
  Methods for responding to events that occur while recording captured media to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput)*