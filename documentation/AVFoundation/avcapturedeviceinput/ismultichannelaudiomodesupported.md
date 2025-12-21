# isMultichannelAudioModeSupported(_:)

**Framework**: AVFoundation  
**Kind**: method

A Boolean value that indicates whether the input supports the specified multichannel audio mode.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
func isMultichannelAudioModeSupported(_ multichannelAudioMode: AVCaptureMultichannelAudioMode) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the input supports the mode; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

You can only set the [`multichannelAudioMode`](avcapturedeviceinput/multichannelaudiomode.md) property if the input supports the value.

> **Note**:  Multichannel audio modes aren’t supported when used in with [`AVCaptureMultiCamSession`](avcapturemulticamsession.md).

## Parameters

- `multichannelAudioMode`: The multichannel audio mode to test.

## See Also

- [var multichannelAudioMode: AVCaptureMultichannelAudioMode](avcapturedeviceinput/multichannelaudiomode.md)
  The multichannel audio mode to apply when recording audio.
- [enum AVCaptureMultichannelAudioMode](avcapturemultichannelaudiomode.md)
  Constants that indicate the modes of multichannel audio.
- [var isWindNoiseRemovalSupported: Bool](avcapturedeviceinput/iswindnoiseremovalsupported.md)
- [var isWindNoiseRemovalEnabled: Bool](avcapturedeviceinput/iswindnoiseremovalenabled.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/ismultichannelaudiomodesupported(_:))*