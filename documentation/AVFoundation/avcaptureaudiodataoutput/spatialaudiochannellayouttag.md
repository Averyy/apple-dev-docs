# spatialAudioChannelLayoutTag

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The audio channel layout tag of the audio sample buffers produced by the audio data output.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var spatialAudioChannelLayoutTag: AudioChannelLayoutTag { get set }
```

```objc
@property (nonatomic) AudioChannelLayoutTag spatialAudioChannelLayoutTag;
```

#### Discussion

When you set your audio data output’s associated [`multichannelAudioMode`](../avcapturedeviceinput/multichannelaudiomode.md) property to `AVCaptureMultichannelAudioModeFirstOrderAmbisonics`, the [`AVCaptureSession`](../avcapturesession.md) allows up to two [`AVCaptureAudioDataOutput`](../avcaptureaudiodataoutput.md) instances to be connected to the First-order Ambisonsics (FOA) input. If you connect a single [`AVCaptureAudioDataOutput`](../avcaptureaudiodataoutput.md) instance, you must configure its [`spatialAudioChannelLayoutTag`](./spatialaudiochannellayouttag.md) property to produce either four channels of FOA audio or two channels of Stereo audio. If you connect two [`AVCaptureAudioDataOutput`](../avcaptureaudiodataoutput.md) instances, you must configure one to output four channels of FOA audio and the other to output two channels of Stereo audio.

Thus, when you set your associated [`multichannelAudioMode`](../avcapturedeviceinput/multichannelaudiomode.md) property to `AVCaptureMultichannelAudioModeFirstOrderAmbisonics`, you must set your connected [`AVCaptureAudioDataOutput`](../avcaptureaudiodataoutput.md) instance’s [`spatialAudioChannelLayoutTag`](./spatialaudiochannellayouttag.md) property to either `kAudioChannelLayoutTag_Stereo` for stereo, or `(kAudioChannelLayoutTag_HOA_ACN_SN3D | 4)` for FOA (see [`AudioChannelLayoutTag`](../../CoreAudioTypes/audiochannellayouttag.md)). When you set your associated [`multichannelAudioMode`](../avcapturedeviceinput/multichannelaudiomode.md) to any other value, the [`AVCaptureSession`](../avcapturesession.md) only supports one [`AVCaptureAudioDataOutput`](../avcaptureaudiodataoutput.md), and you may only set [`spatialAudioChannelLayoutTag`](./spatialaudiochannellayouttag.md) to `kAudioChannelLayoutTag_Unknown` (the default value).

Your [`AVCaptureSession`](../avcapturesession.md) validates your app’s adherence to the the above rules when you call `AVCaptureSession/startRunning:` or [`commitConfiguration()`](../avcapturesession/commitconfiguration%28%29.md) and throws a `NSInvalidArgumentException` if necessary.

## See Also

### Configuring audio capture
- [var audioSettings: [String : Any]!](./audiosettings.md)
  The settings used to decode or re-encode audio before it’s output.
- [func recommendedAudioSettingsForAssetWriter(writingTo: AVFileType) -> [String : Any]?](./recommendedaudiosettingsforassetwriter%28writingto%29.md)
  Specifies the recommended settings for use with an `AVAssetWriterInput`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput/spatialaudiochannellayouttag)*