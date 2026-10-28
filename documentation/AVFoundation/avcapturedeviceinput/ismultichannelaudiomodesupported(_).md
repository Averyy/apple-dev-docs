# isMultichannelAudioModeSupported(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) isMultichannelAudioModeSupported:(AVCaptureMultichannelAudioMode) multichannelAudioMode;
```

## Return Value

[`true`](../../Swift/true.md) if the input supports the mode; otherwise, [`false`](../../Swift/false.md).

## Discussion

You can only set the [`multichannelAudioMode`](./multichannelaudiomode.md) property if the input supports the value.

> **Note**:  Multichannel audio modes aren’t supported when used in with [`AVCaptureMultiCamSession`](../avcapturemulticamsession.md).

## Parameters

- `multichannelAudioMode`: The multichannel audio mode to test.

## See Also

### Configuring audio properties
- [var multichannelAudioMode: AVCaptureMultichannelAudioMode](./multichannelaudiomode.md)
  The multichannel audio mode to apply when recording audio.
- [enum AVCaptureMultichannelAudioMode](../avcapturemultichannelaudiomode.md)
  Constants that indicate the modes of multichannel audio.
- [var isWindNoiseRemovalSupported: Bool](./iswindnoiseremovalsupported.md)
- [var isWindNoiseRemovalEnabled: Bool](./iswindnoiseremovalenabled.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/ismultichannelaudiomodesupported(_:))*