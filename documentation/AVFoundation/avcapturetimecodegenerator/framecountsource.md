# frameCountSource

**Framework**: AVFoundation  
**Kind**: property

A frame counter timecode source that operates independently of any internal or external synchronization.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
class var frameCountSource: AVCaptureTimecode.Source { get }
```

#### Discussion

This class property represents a standalone timecode source that advances based purely on frame count, independent of any real-time or external synchronization. It is ideal for scenarios where a simple, self-contained timing reference is sufficient, without requiring alignment to system clocks or external devices.

## See Also

- [var currentSource: AVCaptureTimecode.Source](avcapturetimecodegenerator/currentsource.md)
  The active timecode source used by [`AVCaptureTimecodeGenerator`](avcapturetimecodegenerator.md) to maintain clock synchronization for accurate timecode generation.
- [var availableSources: [AVCaptureTimecode.Source]](avcapturetimecodegenerator/availablesources.md)
  An array of available timecode synchronization sources that can be used by the timecode generator.
- [class var realTimeClockSource: AVCaptureTimecode.Source](avcapturetimecodegenerator/realtimeclocksource.md)
  A predefined timecode source synchronized to the real-time system clock.
- [func startSynchronization(source: AVCaptureTimecode.Source)](avcapturetimecodegenerator/startsynchronization(source:).md)
  Synchronizes the generator with the specified timecode source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/framecountsource)*