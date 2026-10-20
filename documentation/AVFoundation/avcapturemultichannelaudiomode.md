# AVCaptureMultichannelAudioMode

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AVCaptureMultichannelAudioMode : NSInteger;
```

## Topics

### Modes
- [AVCaptureMultichannelAudioMode.none](./avcapturemultichannelaudiomode/none.md)
  A mode that indicates there’s no multichannel audio.
- [AVCaptureMultichannelAudioMode.stereo](./avcapturemultichannelaudiomode/stereo.md)
  A mode that indicates the recording uses stereo audio.
- [AVCaptureMultichannelAudioMode.firstOrderAmbisonics](./avcapturemultichannelaudiomode/firstorderambisonics.md)
  An audio mode that indicates the recording uses first-order ambisonics.
### Initializers
- [init?(rawValue: Int)](./avcapturemultichannelaudiomode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring audio properties
- [func isMultichannelAudioModeSupported(AVCaptureMultichannelAudioMode) -> Bool](./avcapturedeviceinput/ismultichannelaudiomodesupported%28_%29.md)
  A Boolean value that indicates whether the input supports the specified multichannel audio mode.
- [var multichannelAudioMode: AVCaptureMultichannelAudioMode](./avcapturedeviceinput/multichannelaudiomode.md)
  The multichannel audio mode to apply when recording audio.
- [var isWindNoiseRemovalSupported: Bool](./avcapturedeviceinput/iswindnoiseremovalsupported.md)
- [var isWindNoiseRemovalEnabled: Bool](./avcapturedeviceinput/iswindnoiseremovalenabled.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemultichannelaudiomode)*