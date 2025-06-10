# AVCaptureMultichannelAudioMode

**Framework**: AVFoundation  
**Kind**: enum

Constants that indicate the modes of multichannel audio.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
enum AVCaptureMultichannelAudioMode
```

## Topics

### Modes
- [AVCaptureMultichannelAudioMode.none](avcapturemultichannelaudiomode/none.md)
  A mode that indicates there’s no multichannel audio.
- [AVCaptureMultichannelAudioMode.stereo](avcapturemultichannelaudiomode/stereo.md)
  A mode that indicates the recording uses stereo audio.
- [AVCaptureMultichannelAudioMode.firstOrderAmbisonics](avcapturemultichannelaudiomode/firstorderambisonics.md)
  An audio mode that indicates the recording uses first-order ambisonics.
### Initializers
- [init?(rawValue: Int)](avcapturemultichannelaudiomode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func isMultichannelAudioModeSupported(AVCaptureMultichannelAudioMode) -> Bool](avcapturedeviceinput/ismultichannelaudiomodesupported(_:).md)
  A Boolean value that indicates whether the input supports the specified multichannel audio mode.
- [var multichannelAudioMode: AVCaptureMultichannelAudioMode](avcapturedeviceinput/multichannelaudiomode.md)
  The multichannel audio mode to apply when recording audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemultichannelaudiomode)*