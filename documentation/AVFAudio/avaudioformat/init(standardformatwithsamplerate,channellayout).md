# init(standardFormatWithSampleRate:channelLayout:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

Creates an audio format instance as a deinterleaved float with the specified sample rate and channel layout.

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
init(standardFormatWithSampleRate sampleRate: Double, channelLayout layout: AVAudioChannelLayout)
```

```objc
- (instancetype) initStandardFormatWithSampleRate:(double) sampleRate channelLayout:(AVAudioChannelLayout *) layout;
```

#### Return Value

A new `AVAudioFormat` instance.

#### Discussion

The returned `AVAudioFormat` instance uses the [`AVAudioCommonFormat.pcmFormatFloat32`](../avaudiocommonformat/pcmformatfloat32.md) format.

## Parameters

- `sampleRate`: The sampling rate, in hertz.
- `layout`: The channel layout, which must not be `nil`.

## See Also

### Related Documentation
- [var sampleRate: Double](./samplerate.md)
  The audio format sampling rate, in hertz.
- [var channelLayout: AVAudioChannelLayout?](./channellayout.md)
  The underlying audio channel layout.
### Creating an audio format
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
- [init?(streamDescription: UnsafePointer<AudioStreamBasicDescription>, channelLayout: AVAudioChannelLayout?)](./init%28streamdescription,channellayout%29.md)
  Creates an audio format instance from a stream description and channel layout.
- [init?(formatDescription: CMAudioFormatDescription)](./init%28formatdescription%29.md)
- [init(cmAudioFormatDescription: CMAudioFormatDescription)](./init%28cmaudioformatdescription%29-8rdfj.md)
  Creates an audio format instance from a Core Media audio format description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioformat/init(standardformatwithsamplerate:channellayout:))*