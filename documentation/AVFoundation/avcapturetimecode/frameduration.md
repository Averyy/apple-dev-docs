# frameDuration

**Framework**: AVFoundation  
**Kind**: property

Frame duration of the timecode. If unknown, the value is `kCMTimeInvalid`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var frameDuration: CMTime
```

## See Also

- [var frames: UInt8](avcapturetimecode/frames.md)
  Frame component of the timecode, indicating the frame count within the second.
- [var hours: UInt8](avcapturetimecode/hours.md)
  Time component representing the current timecode in hours.
- [var minutes: UInt8](avcapturetimecode/minutes.md)
  Time component representing the current timecode in minutes.
- [var seconds: UInt8](avcapturetimecode/seconds.md)
  Time component representing the current timecode in seconds.
- [var userBits: UInt32](avcapturetimecode/userbits.md)
  A 32-bit field carrying SMPTE user bits, which are not strictly standardized. User bits are often used for additional metadata such as scene-take information, reel numbers, or dates, but their exact usage is application-dependent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecode/frameduration)*