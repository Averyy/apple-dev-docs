# multichannelAudioMode

**Framework**: AVFoundation  
**Kind**: property

The multichannel audio mode to apply when recording audio.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
var multichannelAudioMode: AVCaptureMultichannelAudioMode { get set }
```

#### Discussion

This property only takes effect when the system routes audio through the built-in microphone. The system ignores the value when an external microphone is in use.

The default value is [`AVCaptureMultichannelAudioMode.none`](avcapturemultichannelaudiomode/none.md), which indicates to use single channel audio recording.

## See Also

- [func isMultichannelAudioModeSupported(AVCaptureMultichannelAudioMode) -> Bool](avcapturedeviceinput/ismultichannelaudiomodesupported(_:).md)
  A Boolean value that indicates whether the input supports the specified multichannel audio mode.
- [enum AVCaptureMultichannelAudioMode](avcapturemultichannelaudiomode.md)
  Constants that indicate the modes of multichannel audio.
- [var isWindNoiseRemovalSupported: Bool](avcapturedeviceinput/iswindnoiseremovalsupported.md)
- [var isWindNoiseRemovalEnabled: Bool](avcapturedeviceinput/iswindnoiseremovalenabled.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/multichannelaudiomode)*