# AVCaptureTimecode.SourceType

**Framework**: AVFoundation  
**Kind**: enum

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

## Topics

### Source types
- [AVCaptureTimecode.SourceType.external](avcapturetimecode/sourcetype-swift.enum/external.md)
  Synchronizes timecode to an external timecode data stream. Ideal for professional audio and video synchronization with external quarter-frame MIDI or HID timecode hardware.
- [AVCaptureTimecode.SourceType.frameCount](avcapturetimecode/sourcetype-swift.enum/framecount.md)
  No internal or external source is adopted. Timecodes are zero-based, sequentially generated frame counts.
- [AVCaptureTimecode.SourceType.realTimeClock](avcapturetimecode/sourcetype-swift.enum/realtimeclock.md)
  Synchronizes timecode to the system clock for real-time applications. Useful for live events or scenarios requiring alignment with the actual time of day.
### Initializers
- [init?(rawValue: Int)](avcapturetimecode/sourcetype-swift.enum/init(rawvalue:).md)

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
- [AVCaptureTimecodeGenerator.SynchronizationStatus](avcapturetimecodegenerator/synchronizationstatus.md)
  Constants defining the synchronization status of a timecode generator .
- [AVCaptureTimecode.Source](avcapturetimecode/source.md)
  Describes a timecode source that a timecode generator can synchronize to.
- [struct AVCaptureTimecode](avcapturetimecode.md)
  This structure represents a timecode, adhering to SMPTE standards, which define precise time information and associated timestamps for video or audio synchronization.
- [static func advanced(AVCaptureTimecode, by: Int64) -> AVCaptureTimecode](avcapturetimecode/advanced(_:by:).md)
  Generates a new timecode by adding a specified number of frames to the given timecode, handling overflow for seconds, minutes, and hours.
- [static func createMetadataSampleBuffer(from: AVCaptureTimecode, associatedWithPresentationTimeStamp: CMTime) -> Unmanaged<CMSampleBuffer>?](avcapturetimecode/createmetadatasamplebuffer(from:associatedwithpresentationtimestamp:).md)
  Creates a sample buffer containing Timecode Media Description metadata for integration with a video track.
- [static func createMetadataSampleBuffer(from: AVCaptureTimecode, forDuration: CMTime) -> Unmanaged<CMSampleBuffer>?](avcapturetimecode/createmetadatasamplebuffer(from:forduration:).md)
  Creates a sample buffer containing Timecode Media Description metadata for a specified duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecode/sourcetype-swift.enum)*