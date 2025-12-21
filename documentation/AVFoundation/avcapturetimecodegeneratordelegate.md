# AVCaptureTimecodeGeneratorDelegate

**Framework**: AVFoundation  
**Kind**: protocol

A protocol for receiving real-time timecode updates and error notifications from a timecode generator.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
protocol AVCaptureTimecodeGeneratorDelegate : NSObjectProtocol
```

## Topics

### Responding to timecode events
- [func timecodeGenerator(AVCaptureTimecodeGenerator, didReceiveUpdate: AVCaptureTimecode, from: AVCaptureTimecode.Source)](avcapturetimecodegeneratordelegate/timecodegenerator(_:didreceiveupdate:from:).md)
  Notifies the delegate when new, unaligned timecodes are parsed from the specified source.
- [func timecodeGenerator(AVCaptureTimecodeGenerator, didUpdateAvailableSources: [AVCaptureTimecode.Source])](avcapturetimecodegeneratordelegate/timecodegenerator(_:didupdateavailablesources:).md)
  Notifies the delegate when the list of available timecode synchronization sources is updated.
- [func timecodeGenerator(AVCaptureTimecodeGenerator, transitionedTo: AVCaptureTimecodeGenerator.SynchronizationStatus, for: AVCaptureTimecode.Source)](avcapturetimecodegeneratordelegate/timecodegenerator(_:transitionedto:for:).md)
  Notifies the delegate when the synchronization status of a timecode source changes.
- [AVCaptureTimecodeGenerator.SynchronizationStatus](avcapturetimecodegenerator/synchronizationstatus.md)
  Constants defining the synchronization status of a timecode generator .

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVCaptureTimecodeGenerator](avcapturetimecodegenerator.md)
  Generates and synchronizes timecode data from various sources for precise video and audio synchronization.
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
- [static func createMetadataSampleBuffer(from: AVCaptureTimecode, forDuration: CMTime) -> Unmanaged<CMSampleBuffer>?](avcapturetimecode/createmetadatasamplebuffer(from:forduration:).md)
  Creates a sample buffer containing Timecode Media Description metadata for a specified duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecodegeneratordelegate)*