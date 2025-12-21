# startSynchronization(source:)

**Framework**: AVFoundation  
**Kind**: method

Synchronizes the generator with the specified timecode source.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
func startSynchronization(source: AVCaptureTimecode.Source)
```

## Parameters

- `source`: The timecode source for synchronization.

## See Also

- [var currentSource: AVCaptureTimecode.Source](avcapturetimecodegenerator/currentsource.md)
  The active timecode source used by [`AVCaptureTimecodeGenerator`](avcapturetimecodegenerator.md) to maintain clock synchronization for accurate timecode generation.
- [var availableSources: [AVCaptureTimecode.Source]](avcapturetimecodegenerator/availablesources.md)
  An array of available timecode synchronization sources that can be used by the timecode generator.
- [class var frameCountSource: AVCaptureTimecode.Source](avcapturetimecodegenerator/framecountsource.md)
  A frame counter timecode source that operates independently of any internal or external synchronization.
- [class var realTimeClockSource: AVCaptureTimecode.Source](avcapturetimecodegenerator/realtimeclocksource.md)
  A predefined timecode source synchronized to the real-time system clock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/startsynchronization(source:))*