# createMetadataSampleBuffer(from:forDuration:)

**Framework**: AVFoundation  
**Kind**: method

Creates a sample buffer containing Timecode Media Description metadata for a specified duration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
static func createMetadataSampleBuffer(from timecode: AVCaptureTimecode, forDuration duration: CMTime) -> Unmanaged<CMSampleBuffer>?
```

#### Return Value

A `CMSampleBufferRef` with encoded Timecode Media Description metadata for the given duration, or `nil` if sample buffer creation fails.

#### Discussion

Use this function for scenarios where timecode metadata needs to span a custom interval (not just a single frame), such as non-frame-accurate workflows or for describing a segment of media with a consistent timecode.

## Parameters

- `timecode`: The   instance providing the timecode details for the metadata sample.
- `duration`: The duration that the metadata sample buffer should represent.

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
- [static func advanced(AVCaptureTimecode, by: Int64) -> AVCaptureTimecode](avcapturetimecode/advanced(_:by:).md)
  Generates a new timecode by adding a specified number of frames to the given timecode, handling overflow for seconds, minutes, and hours.
- [static func createMetadataSampleBuffer(from: AVCaptureTimecode, associatedWithPresentationTimeStamp: CMTime) -> Unmanaged<CMSampleBuffer>?](avcapturetimecode/createmetadatasamplebuffer(from:associatedwithpresentationtimestamp:).md)
  Creates a sample buffer containing Timecode Media Description metadata for integration with a video track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecode/createmetadatasamplebuffer(from:forduration:))*