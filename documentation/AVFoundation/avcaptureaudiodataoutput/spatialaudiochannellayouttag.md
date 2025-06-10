# spatialAudioChannelLayoutTag

**Framework**: AVFoundation  
**Kind**: property

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
var spatialAudioChannelLayoutTag: AudioChannelLayoutTag { get set }
```

#### Discussion

Specifies the audio channel layout tag that describes the audio channel layout to be output by the AVCaptureAudioDataOutput.

The value of this property is from the AudioChannelLayoutTag enumeration defined in CoreAudioBaseTypes.h. Currently, the only two supported values are kAudioChannelLayoutTag_Stereo or ( kAudioChannelLayoutTag_HOA_ACN_SN3D | 4 ) which will provide either a Stereo channel pair or four channels of First Order Ambisonic audio data output. The default value is kAudioChannelLayoutTag_Unknown which results in an AudioChannelLayout determined by the AVCaptureDeviceInput’s configuration.

The rules for allowed values in a given AVCaptureSession are as follows:

When the associated AVCaptureDeviceInput’s multichannelAudioMode property is set to AVCaptureMultichannelAudioModeFirstOrderAmbisonics, the AVCaptureSession can support up to two AVCaptureAudioDataOutput instances. If a single AVCaptureAudioDataOutput is present it can produce either four channels of First Order Ambisonic audio or two channels of Stereo audio. If two AVCaptureAudioDataOutputs are present, one of them must output four channels of First Order Ambisonic audio and the other must output two channels of Stereo audio.

When the associated AVCaptureDeviceInput’s multichannelAudioMode property is set to anything other than AVCaptureMultichannelAudioModeFirstOrderAmbisonics, there must be only one AVCaptureAudioDataOutput present in the AVCaptureSession with its spatialAudioChannelLayoutTag property set to kAudioChannelLayoutTag_Unknown or left at the default value.

These rules are validated when a client calls -[AVCaptureSession startRunning:] or -[AVCaptureSession commitConfiguration:]. If the validation fails an exception will be thrown indicating the invalid setting and the session will not start running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput/spatialaudiochannellayouttag)*