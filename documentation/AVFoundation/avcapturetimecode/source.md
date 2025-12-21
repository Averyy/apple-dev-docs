# AVCaptureTimecode.Source

**Framework**: AVFoundation  
**Kind**: class

Describes a timecode source that a timecode generator can synchronize to.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
class Source
```

#### Overview

`AVCaptureTimecodeSource` provides information about a specific timecode source available for synchronization in `AVCaptureTimecodeGenerator`. It includes metadata such as the source’s name, type, and unique identifier.

## Topics

### Inspecting the source
- [var displayName: String](avcapturetimecode/source/displayname.md)
  The name of the timecode source.
- [var type: AVCaptureTimecode.SourceType](avcapturetimecode/source/type.md)
  The type of timecode source.
- [var uuid: UUID](avcapturetimecode/source/uuid.md)
  A unique identifier for the timecode source.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVCaptureTimecodeGenerator](avcapturetimecodegenerator.md)
  Generates and synchronizes timecode data from various sources for precise video and audio synchronization.
- [protocol AVCaptureTimecodeGeneratorDelegate](avcapturetimecodegeneratordelegate.md)
  A protocol for receiving real-time timecode updates and error notifications from a timecode generator.
- [AVCaptureTimecodeGenerator.SynchronizationStatus](avcapturetimecodegenerator/synchronizationstatus.md)
  Constants defining the synchronization status of a timecode generator .
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecode/source)*