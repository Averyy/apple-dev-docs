# AVCaptureTimecodeGenerator.SynchronizationStatus

**Framework**: AVFoundation  
**Kind**: enum

Constants defining the synchronization status of a timecode generator .

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
enum SynchronizationStatus
```

## Topics

### Status values
- [AVCaptureTimecodeGenerator.SynchronizationStatus.notRequired](avcapturetimecodegenerator/synchronizationstatus/notrequired.md)
  The timecode generator does not require active synchronization for a given source.
- [AVCaptureTimecodeGenerator.SynchronizationStatus.sourceSelected](avcapturetimecodegenerator/synchronizationstatus/sourceselected.md)
  A timecode source has been selected, but synchronization has not yet started.
- [AVCaptureTimecodeGenerator.SynchronizationStatus.sourceUnavailable](avcapturetimecodegenerator/synchronizationstatus/sourceunavailable.md)
  The timecode generator has failed to establish a connection with a given source.
- [AVCaptureTimecodeGenerator.SynchronizationStatus.sourceUnsupported](avcapturetimecodegenerator/synchronizationstatus/sourceunsupported.md)
  The timecode generator is receiving data from the source in an unrecognized format.
- [AVCaptureTimecodeGenerator.SynchronizationStatus.synchronized](avcapturetimecodegenerator/synchronizationstatus/synchronized.md)
  The timecode generator is successfully synchronized to the selected source, maintaining active timing alignment.
- [AVCaptureTimecodeGenerator.SynchronizationStatus.synchronizing](avcapturetimecodegenerator/synchronizationstatus/synchronizing.md)
  The timecode generator is actively synchronizing to the selected source.
- [AVCaptureTimecodeGenerator.SynchronizationStatus.timedOut](avcapturetimecodegenerator/synchronizationstatus/timedout.md)
  The synchronization has timed out.
- [AVCaptureTimecodeGenerator.SynchronizationStatus.unknown](avcapturetimecodegenerator/synchronizationstatus/unknown.md)
  The initial state before a source is selected or during error conditions.
### Initializers
- [init?(rawValue: Int)](avcapturetimecodegenerator/synchronizationstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AVCaptureTimecodeGenerator](avcapturetimecodegenerator.md)
  Generates and synchronizes timecode data from various sources for precise video and audio synchronization.
- [protocol AVCaptureTimecodeGeneratorDelegate](avcapturetimecodegeneratordelegate.md)
  A protocol for receiving real-time timecode updates and error notifications from a timecode generator.
- [AVCaptureTimecode.Source](avcapturetimecode/source.md)
  Describes a timecode source that a timecode generator can synchronize to.
- [AVCaptureTimecode.SourceType](avcapturetimecode/sourcetype-swift.enum.md)
  Defines possible sources for generating timecode in using a timecode generator.
- [struct AVCaptureTimecode](avcapturetimecode.md)
  This structure represents a timecode, adhering to SMPTE standards, which define precise time information and associated timestamps for video or audio synchronization.
- [static func advanced(AVCaptureTimecode, by: Int64) -> AVCaptureTimecode](avcapturetimecode/advanced(_:by:).md)
  Generates a new timecode by adding a specified number of frames to the given timecode, handling overflow for seconds, minutes, and hours.
- [static func createMetadataSampleBuffer(from: AVCaptureTimecode, associatedWithPresentationTimeStamp: CMTime) -> Unmanaged<CMSampleBuffer>?](avcapturetimecode/createmetadatasamplebuffer(from:associatedwithpresentationtimestamp:).md)
  Creates a sample buffer containing Timecode Media Description metadata for integration with a video track.
- [static func createMetadataSampleBuffer(from: AVCaptureTimecode, forDuration: CMTime) -> Unmanaged<CMSampleBuffer>?](avcapturetimecode/createmetadatasamplebuffer(from:forduration:).md)
  Creates a sample buffer containing Timecode Media Description metadata for a specified duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/synchronizationstatus)*