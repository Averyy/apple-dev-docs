# AVCaptureTimecode

**Framework**: AVFoundation  
**Kind**: struct

This structure represents a timecode, adhering to SMPTE standards, which define precise time information and associated timestamps for video or audio synchronization.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
struct AVCaptureTimecode
```

#### Overview

This structure corresponds to the SMPTE 12M-1 Linear Timecode (LTC) format, widely used for professional video and audio synchronization.

## Topics

### Accessing timecode components
- [var frameDuration: CMTime](avcapturetimecode/frameduration.md)
  Frame duration of the timecode. If unknown, the value is `kCMTimeInvalid`.
- [var frames: UInt8](avcapturetimecode/frames.md)
  Frame component of the timecode, indicating the frame count within the second.
- [var hours: UInt8](avcapturetimecode/hours.md)
  Time component representing the current timecode in hours.
- [var minutes: UInt8](avcapturetimecode/minutes.md)
  Time component representing the current timecode in minutes.
- [var seconds: UInt8](avcapturetimecode/seconds.md)
  Time component representing the current timecode in seconds.
- [var userBits: UInt32](avcapturetimecode/userbits.md)
  A 32-bit field carrying SMPTE user bits, which are not strictly standardized. User bits are often used for additional metadata such as scene-take information, reel numbers, or dates, but their exact usage is application-dependent.
### Working with sources
- [var sourceType: AVCaptureTimecode.SourceType](avcapturetimecode/sourcetype-swift.property.md)
  Source type of the timecode, indicating the emitter, carriage, or transport mechanism.
- [AVCaptureTimecode.SourceType](avcapturetimecode/sourcetype-swift.enum.md)
  Defines possible sources for generating timecode in using a timecode generator.
- [AVCaptureTimecode.Source](avcapturetimecode/source.md)
  Describes a timecode source that a timecode generator can synchronize to.
### Manipulating timecodes
- [static func advanced(AVCaptureTimecode, by: Int64) -> AVCaptureTimecode](avcapturetimecode/advanced(_:by:).md)
  Generates a new timecode by adding a specified number of frames to the given timecode, handling overflow for seconds, minutes, and hours.
### Creating metadata sample buffers
- [static func createMetadataSampleBuffer(from: AVCaptureTimecode, associatedWithPresentationTimeStamp: CMTime) -> Unmanaged<CMSampleBuffer>?](avcapturetimecode/createmetadatasamplebuffer(from:associatedwithpresentationtimestamp:).md)
  Creates a sample buffer containing Timecode Media Description metadata for integration with a video track.
- [static func createMetadataSampleBuffer(from: AVCaptureTimecode, forDuration: CMTime) -> Unmanaged<CMSampleBuffer>?](avcapturetimecode/createmetadatasamplebuffer(from:forduration:).md)
  Creates a sample buffer containing Timecode Media Description metadata for a specified duration.
### Initializers
- [init()](avcapturetimecode/init.md)
- [init(hours: UInt8, minutes: UInt8, seconds: UInt8, frames: UInt8, userBits: UInt32, frameDuration: CMTime, sourceType: AVCaptureTimecode.SourceType)](avcapturetimecode/init(hours:minutes:seconds:frames:userbits:frameduration:sourcetype:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class AVCaptureTimecodeGenerator](avcapturetimecodegenerator.md)
  Generates and synchronizes timecode data from various sources for precise video and audio synchronization.
- [protocol AVCaptureTimecodeGeneratorDelegate](avcapturetimecodegeneratordelegate.md)
  A protocol for receiving real-time timecode updates and error notifications from a timecode generator.
- [AVCaptureTimecodeGenerator.SynchronizationStatus](avcapturetimecodegenerator/synchronizationstatus.md)
  Constants defining the synchronization status of a timecode generator .
- [AVCaptureTimecode.Source](avcapturetimecode/source.md)
  Describes a timecode source that a timecode generator can synchronize to.
- [AVCaptureTimecode.SourceType](avcapturetimecode/sourcetype-swift.enum.md)
  Defines possible sources for generating timecode in using a timecode generator.
- [static func advanced(AVCaptureTimecode, by: Int64) -> AVCaptureTimecode](avcapturetimecode/advanced(_:by:).md)
  Generates a new timecode by adding a specified number of frames to the given timecode, handling overflow for seconds, minutes, and hours.
- [static func createMetadataSampleBuffer(from: AVCaptureTimecode, associatedWithPresentationTimeStamp: CMTime) -> Unmanaged<CMSampleBuffer>?](avcapturetimecode/createmetadatasamplebuffer(from:associatedwithpresentationtimestamp:).md)
  Creates a sample buffer containing Timecode Media Description metadata for integration with a video track.
- [static func createMetadataSampleBuffer(from: AVCaptureTimecode, forDuration: CMTime) -> Unmanaged<CMSampleBuffer>?](avcapturetimecode/createmetadatasamplebuffer(from:forduration:).md)
  Creates a sample buffer containing Timecode Media Description metadata for a specified duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecode)*