# Audio settings

**Framework**: AVFAudio  
**Role**: API Collection

Configure audio processing settings using standard key and value constants.

## Topics

### Format and layout keys
- [let AVChannelLayoutKey: String](./avchannellayoutkey.md)
- [Linear PCM format settings](./linear-pcm-format-settings.md)
  The audio settings that apply to linear PCM audio formats.
- [Format settings](./format-settings.md)
  The audio settings that apply to all audio formats that the audio player and recorder classes support.
### Encoder and processing settings
- [Sample rate conversion settings](./sample-rate-conversion-settings.md)
  The constants that define sample rate converter audio quality settings.
- [enum AVAudioQuality](./avaudioquality.md)
  The values that specify the sample rate audio quality for encoding and conversion.
- [Encoder settings](./encoder-settings.md)
  The constants that define the audio encoder settings for the audio recorder class.
- [Time pitch algorithm settings](../AVFoundation/time-pitch-algorithm-settings.md)
  The constants that define the values for the time pitch algorithms.
### Bit rate strategies
- [Encoder bit rate strategy values](./encoder-bit-rate-strategy-values.md)
  The constants that represent the possible bit rate strategy values.

## See Also

### Audio data
- [class AVAudioFile](./avaudiofile.md)
  An object that represents an audio file that the system can open for reading or writing.
- [class AVAudioPCMBuffer](./avaudiopcmbuffer.md)
  An object that represents an audio buffer you use with PCM audio formats.
- [class AVAudioCompressedBuffer](./avaudiocompressedbuffer.md)
  An object that represents an audio buffer that you use for compressed audio formats.
- [struct AVReadOnlyAudioPCMBuffer](./avreadonlyaudiopcmbuffer.md)
  A read-only, Sendable audio buffer for safe concurrent access.
- [class AVAudioBuffer](./avaudiobuffer.md)
  An object that represents a buffer of audio data with a format.
- [class AVAudioFormat](./avaudioformat.md)
  An object that describes the representation of an audio format.
- [class AVAudioChannelLayout](./avaudiochannellayout.md)
  An object that describes the roles of a set of audio channels.
- [class AVAudioConverter](./avaudioconverter.md)
  An object that converts streams of audio between formats.
- [class AVAudioTime](./avaudiotime.md)
  An object you use to represent a moment in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/audio-settings)*