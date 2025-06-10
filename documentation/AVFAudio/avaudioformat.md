# AVAudioFormat

**Framework**: AVFAudio  
**Kind**: class

An object that describes the representation of an audio format.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class AVAudioFormat
```

#### Overview

The [`AVAudioFormat`](avaudioformat.md) class wraps Core Audio’s [`AudioStreamBasicDescription`](https://developer.apple.com/documentation/CoreAudioTypes/AudioStreamBasicDescription), and includes convenience initializers and accessors for common formats, including Core Audio’s standard deinterleaved 32-bit floating point format.

Instances of this class are immutable.

## Topics

### Creating a New Audio Format Representation
- [init(standardFormatWithSampleRate: Double, channelLayout: AVAudioChannelLayout)](avaudioformat/init(standardformatwithsamplerate:channellayout:).md)
  Creates an audio format instance as a deinterleaved float with the specified sample rate and channel layout.
- [init?(standardFormatWithSampleRate: Double, channels: AVAudioChannelCount)](avaudioformat/init(standardformatwithsamplerate:channels:).md)
  Creates an audio format instance with the specified sample rate and channel count.
- [init?(commonFormat: AVAudioCommonFormat, sampleRate: Double, channels: AVAudioChannelCount, interleaved: Bool)](avaudioformat/init(commonformat:samplerate:channels:interleaved:).md)
  Creates an audio format instance.
- [init(commonFormat: AVAudioCommonFormat, sampleRate: Double, interleaved: Bool, channelLayout: AVAudioChannelLayout)](avaudioformat/init(commonformat:samplerate:interleaved:channellayout:).md)
  Creates an audio format instance with the specified audio format, sample rate, interleaved state, and channel layout.
- [init?(settings: [String : Any])](avaudioformat/init(settings:).md)
  Creates an audio format instance using the specified settings dictionary.
- [init?(streamDescription: UnsafePointer<AudioStreamBasicDescription>)](avaudioformat/init(streamdescription:).md)
  Creates an audio format instance from a stream description.
- [init?(streamDescription: UnsafePointer<AudioStreamBasicDescription>, channelLayout: AVAudioChannelLayout?)](avaudioformat/init(streamdescription:channellayout:).md)
  Creates an audio format instance from a stream description and channel layout.
- [init(cmAudioFormatDescription: CMAudioFormatDescription)](avaudioformat/init(cmaudioformatdescription:).md)
  Creates an audio format instance from a Core Media audio format description.
### Getting the Audio Stream Description
- [var streamDescription: UnsafePointer<AudioStreamBasicDescription>](avaudioformat/streamdescription.md)
  The audio format properties of a stream of audio data.
### Comparing Instances
- [func isEqual(Any) -> Bool](avaudioformat/isequal(_:).md)
  Indicates whether the audio format instance and a specified object are functionally equivalent.
### Getting Audio Format Values
- [var sampleRate: Double](avaudioformat/samplerate.md)
  The audio format sampling rate, in hertz.
- [var channelCount: AVAudioChannelCount](avaudioformat/channelcount.md)
  The number of channels of audio data.
- [var channelLayout: AVAudioChannelLayout?](avaudioformat/channellayout.md)
  The underlying audio channel layout.
- [var formatDescription: CMAudioFormatDescription](avaudioformat/formatdescription.md)
  The audio format description to use with Core Media APIs.
### Determining the Audio Format
- [var isInterleaved: Bool](avaudioformat/isinterleaved.md)
  A Boolean value that indicates whether the samples mix into one stream.
- [var isStandard: Bool](avaudioformat/isstandard.md)
  A Boolean value that indicates whether the format is in a deinterleaved native-endian float state.
- [var commonFormat: AVAudioCommonFormat](avaudioformat/commonformat.md)
  The common format identifier instance.
- [var settings: [String : Any]](avaudioformat/settings.md)
  A dictionary that represents the format as a dictionary using audio setting keys.
- [var magicCookie: Data?](avaudioformat/magiccookie.md)
  An object that contains metadata that encoders and decoders require.
### Constants
- [enum AVAudioCommonFormat](avaudiocommonformat.md)
  The format options that describe common audio formats.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AVAudioChannelLayout](avaudiochannellayout.md)
  An object that describes the roles of a set of audio channels.
- [let AVChannelLayoutKey: String](avchannellayoutkey.md)
- [Linear PCM Format Settings](linear-pcm-format-settings.md)
  The audio settings that apply to linear PCM audio formats.
- [Format Settings](format-settings.md)
  The audio settings that apply to all audio formats that the audio player and recorder classes support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioformat)*