# init(standardFormatWithSampleRate:channels:)

**Framework**: AVFAudio  
**Kind**: init

Creates an audio format instance with the specified sample rate and channel count.

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
init?(standardFormatWithSampleRate sampleRate: Double, channels: AVAudioChannelCount)
```

#### Return Value

A new `AVAudioFormat` instance, or `nil` if the initialization fails.

#### Discussion

The returned `AVAudioFormat` instance uses the [`AVAudioCommonFormat.pcmFormatFloat32`](avaudiocommonformat/pcmformatfloat32.md) format.

## Parameters

- `sampleRate`: The sampling rate, in hertz.
- `channels`: The channel count.

## See Also

- [var sampleRate: Double](avaudioformat/samplerate.md)
  The audio format sampling rate, in hertz.
- [var channelLayout: AVAudioChannelLayout?](avaudioformat/channellayout.md)
  The underlying audio channel layout.
- [init(standardFormatWithSampleRate: Double, channelLayout: AVAudioChannelLayout)](avaudioformat/init(standardformatwithsamplerate:channellayout:).md)
  Creates an audio format instance as a deinterleaved float with the specified sample rate and channel layout.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioformat/init(standardformatwithsamplerate:channels:))*