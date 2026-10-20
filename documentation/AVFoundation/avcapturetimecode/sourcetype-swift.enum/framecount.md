# AVCaptureTimecode.SourceType.frameCount

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

No internal or external source is adopted. Timecodes are zero-based, sequentially generated frame counts.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
case frameCount
```

```c
AVCaptureTimecodeSourceTypeFrameCount
```

## See Also

### Source types
- [AVCaptureTimecode.SourceType.external](./external.md)
  Synchronizes timecode to an external timecode data stream. Ideal for professional audio and video synchronization with external quarter-frame MIDI or HID timecode hardware.
- [AVCaptureTimecode.SourceType.realTimeClock](./realtimeclock.md)
  Synchronizes timecode to the system clock for real-time applications. Useful for live events or scenarios requiring alignment with the actual time of day.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecode/sourcetype-swift.enum/framecount)*