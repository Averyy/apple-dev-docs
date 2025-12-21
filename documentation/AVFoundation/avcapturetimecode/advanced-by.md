# advanced(_:by:)

**Framework**: AVFoundation  
**Kind**: method

Generates a new timecode by adding a specified number of frames to the given timecode, handling overflow for seconds, minutes, and hours.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
static func advanced(_ timecode: AVCaptureTimecode, by framesToAdd: Int64) -> AVCaptureTimecode
```

#### Return Value

A new [`AVCaptureTimecode`](avcapturetimecode.md) struct with the updated time values after adding the specified frames.

## Parameters

- `timecode`: The original   to be incremented.
- `framesToAdd`: The number of frames to add to the timecode.

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
- [struct AVCaptureTimecode](avcapturetimecode.md)
  This structure represents a timecode, adhering to SMPTE standards, which define precise time information and associated timestamps for video or audio synchronization.
- [static func createMetadataSampleBuffer(from: AVCaptureTimecode, associatedWithPresentationTimeStamp: CMTime) -> Unmanaged<CMSampleBuffer>?](avcapturetimecode/createmetadatasamplebuffer(from:associatedwithpresentationtimestamp:).md)
  Creates a sample buffer containing Timecode Media Description metadata for integration with a video track.
- [static func createMetadataSampleBuffer(from: AVCaptureTimecode, forDuration: CMTime) -> Unmanaged<CMSampleBuffer>?](avcapturetimecode/createmetadatasamplebuffer(from:forduration:).md)
  Creates a sample buffer containing Timecode Media Description metadata for a specified duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecode/advanced(_:by:))*