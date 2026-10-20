# isWindNoiseRemovalEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
var isWindNoiseRemovalEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isWindNoiseRemovalEnabled) BOOL windNoiseRemovalEnabled;
```

## See Also

### Configuring audio properties
- [func isMultichannelAudioModeSupported(AVCaptureMultichannelAudioMode) -> Bool](./ismultichannelaudiomodesupported%28_%29.md)
  A Boolean value that indicates whether the input supports the specified multichannel audio mode.
- [var multichannelAudioMode: AVCaptureMultichannelAudioMode](./multichannelaudiomode.md)
  The multichannel audio mode to apply when recording audio.
- [enum AVCaptureMultichannelAudioMode](../avcapturemultichannelaudiomode.md)
  Constants that indicate the modes of multichannel audio.
- [var isWindNoiseRemovalSupported: Bool](./iswindnoiseremovalsupported.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/iswindnoiseremovalenabled)*