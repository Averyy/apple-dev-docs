# audioSettings

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The settings used to decode or re-encode audio before it’s output.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var audioSettings: [String : Any]! { get set }
```

```objc
@property (nonatomic, copy, null_resettable) NSDictionary<NSString *,id> * audioSettings;
```

#### Discussion

The value of this property is a dictionary containing values for audio settings keys defined in [Audio settings](../audio-settings.md).

If the value of this property is `nil`, samples are output in their device native format.

## See Also

### Configuring audio capture
- [func recommendedAudioSettingsForAssetWriter(writingTo: AVFileType) -> [String : Any]?](./recommendedaudiosettingsforassetwriter%28writingto%29.md)
  Specifies the recommended settings for use with an `AVAssetWriterInput`.
- [var spatialAudioChannelLayoutTag: AudioChannelLayoutTag](./spatialaudiochannellayouttag.md)
  The audio channel layout tag of the audio sample buffers produced by the audio data output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput/audiosettings)*