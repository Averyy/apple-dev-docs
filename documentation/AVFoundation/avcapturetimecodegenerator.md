# AVCaptureTimecodeGenerator

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

Generates and synchronizes timecode data from various sources for precise video and audio synchronization.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
class AVCaptureTimecodeGenerator
```

```objc
@interface AVCaptureTimecodeGenerator : NSObject
```

## Overview

The [`AVCaptureTimecodeGenerator`](./avcapturetimecodegenerator.md) class supports multiple timecode sources, including frame counting, system clock synchronization, and MIDI timecode input (MTC). Suitable for playback, recording, or other time-sensitive operations where precise timecode metadata is required.

Use the [`startSynchronization(source:)`](./avcapturetimecodegenerator/startsynchronization%28source%29.md) method to set up the desired timecode source.

## Topics

### Generating timecode
- [func generateInitialTimecode() -> AVCaptureTimecode](./avcapturetimecodegenerator/generateinitialtimecode%28%29.md)
  Generates an initial timecode intended to be the first in a sequence.
### Managing sources
- [var currentSource: AVCaptureTimecode.Source](./avcapturetimecodegenerator/currentsource.md)
  The active timecode source used by [`AVCaptureTimecodeGenerator`](./avcapturetimecodegenerator.md) to maintain clock synchronization for accurate timecode generation.
- [var availableSources: [AVCaptureTimecode.Source]](./avcapturetimecodegenerator/availablesources.md)
  An array of available timecode synchronization sources that can be used by the timecode generator.
- [class var frameCountSource: AVCaptureTimecode.Source](./avcapturetimecodegenerator/framecountsource.md)
  A frame counter timecode source that operates independently of any internal or external synchronization.
- [class var realTimeClockSource: AVCaptureTimecode.Source](./avcapturetimecodegenerator/realtimeclocksource.md)
  A predefined timecode source synchronized to the real-time system clock.
- [func startSynchronization(source: AVCaptureTimecode.Source)](./avcapturetimecodegenerator/startsynchronization%28source%29.md)
  Synchronizes the generator with the specified timecode source.
### Configuring the generator
- [var synchronizationTimeout: TimeInterval](./avcapturetimecodegenerator/synchronizationtimeout.md)
  The maximum time interval allowed for source synchronization attempts before timing out.
- [var timecodeAlignmentOffset: TimeInterval](./avcapturetimecodegenerator/timecodealignmentoffset.md)
  The time offset, in seconds, applied to the generated timecode.
- [var timecodeFrameDuration: CMTime](./avcapturetimecodegenerator/timecodeframeduration.md)
  The frame duration that the generator will use to generate timecodes.
- [func setDelegate((any AVCaptureTimecodeGeneratorDelegate)?, queue: dispatch_queue_t?)](./avcapturetimecodegenerator/setdelegate%28_,queue%29.md)
  Assigns a delegate to receive real-time timecode updates and specifies a queue for callbacks.
### Handling delegate callbacks
- [var delegate: (any AVCaptureTimecodeGeneratorDelegate)?](./avcapturetimecodegenerator/delegate.md)
  The delegate that receives timecode updates from the timecode generator.
- [var delegateCallbackQueue: dispatch_queue_t?](./avcapturetimecodegenerator/delegatecallbackqueue.md)
  The dispatch queue on which delegate callbacks are invoked.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Timecode generation
- [protocol AVCaptureTimecodeGeneratorDelegate](./avcapturetimecodegeneratordelegate.md)
  A protocol for receiving real-time timecode updates and error notifications from a timecode generator.
- [AVCaptureTimecodeGenerator.SynchronizationStatus](./avcapturetimecodegenerator/synchronizationstatus.md)
  Constants defining the synchronization status of a timecode generator .
- [AVCaptureTimecode.Source](./avcapturetimecode/source.md)
  Describes a timecode source that a timecode generator can synchronize to.
- [AVCaptureTimecode.SourceType](./avcapturetimecode/sourcetype-swift.enum.md)
  Defines possible sources for generating timecode in using a timecode generator.
- [struct AVCaptureTimecode](./avcapturetimecode.md)
  This structure represents a timecode, adhering to SMPTE standards, which define precise time information and associated timestamps for video or audio synchronization.
- [static func advanced(AVCaptureTimecode, by: Int64) -> AVCaptureTimecode](./avcapturetimecode/advanced%28_,by%29.md)
  Generates a new timecode by adding a specified number of frames to the given timecode, handling overflow for seconds, minutes, and hours.
- [static func createMetadataSampleBuffer(from: AVCaptureTimecode, associatedWithPresentationTimeStamp: CMTime) -> Unmanaged<CMSampleBuffer>?](./avcapturetimecode/createmetadatasamplebuffer%28from,associatedwithpresentationtimestamp%29.md)
  Creates a sample buffer containing Timecode Media Description metadata for integration with a video track.
- [static func createMetadataSampleBuffer(from: AVCaptureTimecode, forDuration: CMTime) -> Unmanaged<CMSampleBuffer>?](./avcapturetimecode/createmetadatasamplebuffer%28from,forduration%29.md)
  Creates a sample buffer containing Timecode Media Description metadata for a specified duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator)*