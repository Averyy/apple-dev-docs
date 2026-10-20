# AVCaptureTimecode.SourceType

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Defines possible sources for generating timecode in using a timecode generator.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
enum SourceType
```

```c
enum AVCaptureTimecodeSourceType : NSInteger;
```

## Topics

### Source types
- [AVCaptureTimecode.SourceType.external](./sourcetype-swift.enum/external.md)
  Synchronizes timecode to an external timecode data stream. Ideal for professional audio and video synchronization with external quarter-frame MIDI or HID timecode hardware.
- [AVCaptureTimecode.SourceType.frameCount](./sourcetype-swift.enum/framecount.md)
  No internal or external source is adopted. Timecodes are zero-based, sequentially generated frame counts.
- [AVCaptureTimecode.SourceType.realTimeClock](./sourcetype-swift.enum/realtimeclock.md)
  Synchronizes timecode to the system clock for real-time applications. Useful for live events or scenarios requiring alignment with the actual time of day.
### Initializers
- [init?(rawValue: Int)](./sourcetype-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Timecode generation
- [class AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md)
  Generates and synchronizes timecode data from various sources for precise video and audio synchronization.
- [protocol AVCaptureTimecodeGeneratorDelegate](../avcapturetimecodegeneratordelegate.md)
  A protocol for receiving real-time timecode updates and error notifications from a timecode generator.
- [AVCaptureTimecodeGenerator.SynchronizationStatus](../avcapturetimecodegenerator/synchronizationstatus.md)
  Constants defining the synchronization status of a timecode generator .
- [AVCaptureTimecode.Source](./source.md)
  Describes a timecode source that a timecode generator can synchronize to.
- [struct AVCaptureTimecode](../avcapturetimecode.md)
  This structure represents a timecode, adhering to SMPTE standards, which define precise time information and associated timestamps for video or audio synchronization.
- [static func advanced(AVCaptureTimecode, by: Int64) -> AVCaptureTimecode](./advanced%28_,by%29.md)
  Generates a new timecode by adding a specified number of frames to the given timecode, handling overflow for seconds, minutes, and hours.
- [static func createMetadataSampleBuffer(from: AVCaptureTimecode, associatedWithPresentationTimeStamp: CMTime) -> Unmanaged<CMSampleBuffer>?](./createmetadatasamplebuffer%28from,associatedwithpresentationtimestamp%29.md)
  Creates a sample buffer containing Timecode Media Description metadata for integration with a video track.
- [static func createMetadataSampleBuffer(from: AVCaptureTimecode, forDuration: CMTime) -> Unmanaged<CMSampleBuffer>?](./createmetadatasamplebuffer%28from,forduration%29.md)
  Creates a sample buffer containing Timecode Media Description metadata for a specified duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecode/sourcetype-swift.enum)*