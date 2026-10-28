# init(streamDescription:channelLayout:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

Creates an audio format instance from a stream description and channel layout.

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
init?(streamDescription asbd: UnsafePointer<AudioStreamBasicDescription>, channelLayout layout: AVAudioChannelLayout?)
```

```objc
- (instancetype) initWithStreamDescription:(const AudioStreamBasicDescription *) asbd channelLayout:(AVAudioChannelLayout *) layout;
```

## Return Value

A new `AVAudioFormat` instance, or `nil` if the initialization fails.

## Discussion

When `layout` is `nil`, and `asbd` specifies one or two channels, this method assumes mono or stereo layout, respectively.

If the [`AudioStreamBasicDescription`](../../CoreAudioTypes/audiostreambasicdescription.md) specifies more than two channels and `layout` is `nil`, this method fails and returns `nil`.

## Parameters

- `asbd`: The audio stream description.
- `layout`: The channel layout.

## See Also

### Creating an audio format
- [init(standardFormatWithSampleRate: Double, channelLayout: AVAudioChannelLayout)](./init%28standardformatwithsamplerate,channellayout%29.md)
  Creates an audio format instance as a deinterleaved float with the specified sample rate and channel layout.
- [init?(standardFormatWithSampleRate: Double, channels: AVAudioChannelCount)](./init%28standardformatwithsamplerate,channels%29.md)
  Creates an audio format instance with the specified sample rate and channel count.
- [init?(commonFormat: AVAudioCommonFormat, sampleRate: Double, channels: AVAudioChannelCount, interleaved: Bool)](./init%28commonformat,samplerate,channels,interleaved%29.md)
  Creates an audio format instance.
- [init(commonFormat: AVAudioCommonFormat, sampleRate: Double, interleaved: Bool, channelLayout: AVAudioChannelLayout)](./init%28commonformat,samplerate,interleaved,channellayout%29.md)
  Creates an audio format instance with the specified audio format, sample rate, interleaved state, and channel layout.
- [init?(settings: [String : Any])](./init%28settings%29.md)
  Creates an audio format instance using the specified settings dictionary.
- [init?(streamDescription: UnsafePointer<AudioStreamBasicDescription>)](./init%28streamdescription%29.md)
  Creates an audio format instance from a stream description.
- [init?(formatDescription: CMAudioFormatDescription)](./init%28formatdescription%29.md)
- [init(cmAudioFormatDescription: CMAudioFormatDescription)](./init%28cmaudioformatdescription%29-8rdfj.md)
  Creates an audio format instance from a Core Media audio format description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioformat/init(streamdescription:channellayout:))*