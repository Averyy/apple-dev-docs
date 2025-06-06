# init(settings:)

**Framework**: AVFAudio  
**Kind**: init

Creates an audio format instance using the specified settings dictionary.

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
init?(settings: [String : Any])
```

#### Return Value

A new `AVAudioFormat` instance, or `nil` if the initialization fails.

#### Discussion

Note that many settings dictionary elements aren’t relevant for the format, so this method ignores them. For information about supported dictionary values, see [`Audio settings`](https://developer.apple.com/documentation/AVFoundation/audio-settings).

## Parameters

- `settings`: The settings dictionary.

## See Also

- [init(standardFormatWithSampleRate: Double, channelLayout: AVAudioChannelLayout)](avaudioformat/init(standardformatwithsamplerate:channellayout:).md)
  Creates an audio format instance as a deinterleaved float with the specified sample rate and channel layout.
- [init?(standardFormatWithSampleRate: Double, channels: AVAudioChannelCount)](avaudioformat/init(standardformatwithsamplerate:channels:).md)
  Creates an audio format instance with the specified sample rate and channel count.
- [init?(commonFormat: AVAudioCommonFormat, sampleRate: Double, channels: AVAudioChannelCount, interleaved: Bool)](avaudioformat/init(commonformat:samplerate:channels:interleaved:).md)
  Creates an audio format instance.
- [init(commonFormat: AVAudioCommonFormat, sampleRate: Double, interleaved: Bool, channelLayout: AVAudioChannelLayout)](avaudioformat/init(commonformat:samplerate:interleaved:channellayout:).md)
  Creates an audio format instance with the specified audio format, sample rate, interleaved state, and channel layout.
- [init?(streamDescription: UnsafePointer<AudioStreamBasicDescription>)](avaudioformat/init(streamdescription:).md)
  Creates an audio format instance from a stream description.
- [init?(streamDescription: UnsafePointer<AudioStreamBasicDescription>, channelLayout: AVAudioChannelLayout?)](avaudioformat/init(streamdescription:channellayout:).md)
  Creates an audio format instance from a stream description and channel layout.
- [init(cmAudioFormatDescription: CMAudioFormatDescription)](avaudioformat/init(cmaudioformatdescription:).md)
  Creates an audio format instance from a Core Media audio format description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioformat/init(settings:))*