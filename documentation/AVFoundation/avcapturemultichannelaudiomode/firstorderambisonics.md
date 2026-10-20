# AVCaptureMultichannelAudioMode.firstOrderAmbisonics

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

An audio mode that indicates the recording uses first-order ambisonics.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
case firstOrderAmbisonics
```

```c
AVCaptureMultichannelAudioModeFirstOrderAmbisonics
```

#### Discussion

When recording a QuickTime movie file, the system records a stereo audio track with the first-order ambisonics track for backward playback compatibility.

## See Also

### Modes
- [AVCaptureMultichannelAudioMode.none](./none.md)
  A mode that indicates there’s no multichannel audio.
- [AVCaptureMultichannelAudioMode.stereo](./stereo.md)
  A mode that indicates the recording uses stereo audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemultichannelaudiomode/firstorderambisonics)*