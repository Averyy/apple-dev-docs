# createMetadataSampleBuffer(from:associatedWithPresentationTimeStamp:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Creates a sample buffer containing Timecode Media Description metadata for integration with a video track.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
static func createMetadataSampleBuffer(from timecode: AVCaptureTimecode, associatedWithPresentationTimeStamp presentationTimeStamp: CMTime) -> Unmanaged<CMSampleBuffer>?
```

```c
CMSampleBufferRefAVCaptureTimecodeCreateMetadataSampleBufferAssociatedWithPresentationTimeStamp(AVCaptureTimecode timecode, CMTime presentationTimeStamp);
```

## Return Value

A `CMSampleBufferRef` with the encoded Timecode Media Description metadata for video synchronization, or `nil` if sample buffer creation fails.

## Parameters

- `timecode`: The [`AVCaptureTimecode`](../avcapturetimecode.md) instance providing the timecode details to encode.
- `presentationTimeStamp`: The presentation time stamp that determines the exact moment in the media timeline where the metadata should be applied. It is embedded in the sample timing info (`CMSampleTimingInfo`) and ensures that the packaged metadata synchronizes accurately with the corresponding video frame.

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
- [AVCaptureTimecode.SourceType](./sourcetype-swift.enum.md)
  Defines possible sources for generating timecode in using a timecode generator.
- [struct AVCaptureTimecode](../avcapturetimecode.md)
  This structure represents a timecode, adhering to SMPTE standards, which define precise time information and associated timestamps for video or audio synchronization.
- [static func advanced(AVCaptureTimecode, by: Int64) -> AVCaptureTimecode](./advanced%28_,by%29.md)
  Generates a new timecode by adding a specified number of frames to the given timecode, handling overflow for seconds, minutes, and hours.
- [static func createMetadataSampleBuffer(from: AVCaptureTimecode, forDuration: CMTime) -> Unmanaged<CMSampleBuffer>?](./createmetadatasamplebuffer%28from,forduration%29.md)
  Creates a sample buffer containing Timecode Media Description metadata for a specified duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecode/createmetadatasamplebuffer(from:associatedwithpresentationtimestamp:))*