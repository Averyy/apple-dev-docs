# realTimeClockSource

**Framework**: AVFoundation  
**Kind**: property

A predefined timecode source synchronized to the real-time system clock.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
class var realTimeClockSource: AVCaptureTimecode.Source { get }
```

#### Discussion

This class property provides a default timecode source based on the real-time system clock, requiring no external device. It is ideal for live events or scenarios where alignment with the current time of day is necessary.

## See Also

- [var currentSource: AVCaptureTimecode.Source](avcapturetimecodegenerator/currentsource.md)
  The active timecode source used by [`AVCaptureTimecodeGenerator`](avcapturetimecodegenerator.md) to maintain clock synchronization for accurate timecode generation.
- [var availableSources: [AVCaptureTimecode.Source]](avcapturetimecodegenerator/availablesources.md)
  An array of available timecode synchronization sources that can be used by the timecode generator.
- [class var frameCountSource: AVCaptureTimecode.Source](avcapturetimecodegenerator/framecountsource.md)
  A frame counter timecode source that operates independently of any internal or external synchronization.
- [func startSynchronization(source: AVCaptureTimecode.Source)](avcapturetimecodegenerator/startsynchronization(source:).md)
  Synchronizes the generator with the specified timecode source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/realtimeclocksource)*