# init(formatDescription:)

**Framework**: AVFAudio  
**Kind**: init

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init?(formatDescription: CMAudioFormatDescription)
```

#### Discussion

Initialize from a CMAudioFormatDescriptionRef.

If formatDescription is invalid, this method fails (returns nil).

## Parameters

- `formatDescription`: The CMAudioFormatDescriptionRef.

## See Also

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
- [init(cmAudioFormatDescription: CMAudioFormatDescription)](avaudioformat/init(cmaudioformatdescription:)-8rdfj.md)
  Creates an audio format instance from a Core Media audio format description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioformat/init(formatdescription:))*