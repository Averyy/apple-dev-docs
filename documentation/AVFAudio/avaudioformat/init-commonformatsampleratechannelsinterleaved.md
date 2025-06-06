# init(commonFormat:sampleRate:channels:interleaved:)

**Framework**: AVFAudio  
**Kind**: init

Creates an audio format instance.

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
init?(commonFormat format: AVAudioCommonFormat, sampleRate: Double, channels: AVAudioChannelCount, interleaved: Bool)
```

#### Return Value

A new `AVAudioFormat` instance, or `nil` if the initialization fails.

#### Discussion

For information about possible `format` values, see [`AVAudioCommonFormat`](avaudiocommonformat.md).

## Parameters

- `format`: The audio format.
- `sampleRate`: The sampling rate, in hertz.
- `channels`: The channel count.
- `interleaved`: The Boolean value that indicates whether   is in an interleaved state.

## See Also

- [var sampleRate: Double](avaudioformat/samplerate.md)
  The audio format sampling rate, in hertz.
- [var isInterleaved: Bool](avaudioformat/isinterleaved.md)
  A Boolean value that indicates whether the samples mix into one stream.
- [var commonFormat: AVAudioCommonFormat](avaudioformat/commonformat.md)
  The common format identifier instance.
- [init(standardFormatWithSampleRate: Double, channelLayout: AVAudioChannelLayout)](avaudioformat/init(standardformatwithsamplerate:channellayout:).md)
  Creates an audio format instance as a deinterleaved float with the specified sample rate and channel layout.
- [init?(standardFormatWithSampleRate: Double, channels: AVAudioChannelCount)](avaudioformat/init(standardformatwithsamplerate:channels:).md)
  Creates an audio format instance with the specified sample rate and channel count.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioformat/init(commonformat:samplerate:channels:interleaved:))*