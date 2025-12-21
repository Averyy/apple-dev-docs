# currentSource

**Framework**: AVFoundation  
**Kind**: property

The active timecode source used by [`AVCaptureTimecodeGenerator`](avcapturetimecodegenerator.md) to maintain clock synchronization for accurate timecode generation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var currentSource: AVCaptureTimecode.Source { get }
```

#### Discussion

Indicates the active timecode source, as defined in the `AVCaptureTimecodeSynchronizationSourceType` enum. If an [`AVCaptureTimecodeGenerator`](avcapturetimecodegenerator.md) becomes disconnected from its source, it continues generating timecodes using historical data from its ring buffer. This approach allows the generator to maintain synchronization during brief disruptions, as is common in cinema workflows where timecode signals may experience discontinuities.

## See Also

- [var availableSources: [AVCaptureTimecode.Source]](avcapturetimecodegenerator/availablesources.md)
  An array of available timecode synchronization sources that can be used by the timecode generator.
- [class var frameCountSource: AVCaptureTimecode.Source](avcapturetimecodegenerator/framecountsource.md)
  A frame counter timecode source that operates independently of any internal or external synchronization.
- [class var realTimeClockSource: AVCaptureTimecode.Source](avcapturetimecodegenerator/realtimeclocksource.md)
  A predefined timecode source synchronized to the real-time system clock.
- [func startSynchronization(source: AVCaptureTimecode.Source)](avcapturetimecodegenerator/startsynchronization(source:).md)
  Synchronizes the generator with the specified timecode source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/currentsource)*