# frames

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Frame component of the timecode, indicating the frame count within the second.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var frames: UInt8
```

```c
uint8_t frames;
```

## See Also

### Accessing timecode components
- [var frameDuration: CMTime](./frameduration.md)
  Frame duration of the timecode. If unknown, the value is `kCMTimeInvalid`.
- [var hours: UInt8](./hours.md)
  Time component representing the current timecode in hours.
- [var minutes: UInt8](./minutes.md)
  Time component representing the current timecode in minutes.
- [var seconds: UInt8](./seconds.md)
  Time component representing the current timecode in seconds.
- [var userBits: UInt32](./userbits.md)
  A 32-bit field carrying SMPTE user bits, which are not strictly standardized. User bits are often used for additional metadata such as scene-take information, reel numbers, or dates, but their exact usage is application-dependent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecode/frames)*