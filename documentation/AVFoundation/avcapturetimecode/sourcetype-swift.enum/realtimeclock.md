# AVCaptureTimecode.SourceType.realTimeClock

**Framework**: AVFoundation  
**Kind**: case

Synchronizes timecode to the system clock for real-time applications. Useful for live events or scenarios requiring alignment with the actual time of day.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
case realTimeClock
```

## See Also

- [AVCaptureTimecode.SourceType.external](avcapturetimecode/sourcetype-swift.enum/external.md)
  Synchronizes timecode to an external timecode data stream. Ideal for professional audio and video synchronization with external quarter-frame MIDI or HID timecode hardware.
- [AVCaptureTimecode.SourceType.frameCount](avcapturetimecode/sourcetype-swift.enum/framecount.md)
  No internal or external source is adopted. Timecodes are zero-based, sequentially generated frame counts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecode/sourcetype-swift.enum/realtimeclock)*