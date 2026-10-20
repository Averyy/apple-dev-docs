# init(commonFormat:sampleRate:interleaved:channelLayout:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

Creates an audio format instance with the specified audio format, sample rate, interleaved state, and channel layout.

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
init(commonFormat format: AVAudioCommonFormat, sampleRate: Double, interleaved: Bool, channelLayout layout: AVAudioChannelLayout)
```

```objc
- (instancetype) initWithCommonFormat:(AVAudioCommonFormat) format sampleRate:(double) sampleRate interleaved:(BOOL) interleaved channelLayout:(AVAudioChannelLayout *) layout;
```

#### Return Value

A new `AVAudioFormat` instance.

#### Discussion

For information about possible `format` values, see [`AVAudioCommonFormat`](../avaudiocommonformat.md).

## Parameters

- `format`: The audio format.
- `sampleRate`: The sampling rate, in hertz.
- `interleaved`: The Boolean value that indicates whether `format` is in an interleaved state.
- `layout`: The channel layout, which must not be `nil`.

## See Also

### Related Documentation
- [var sampleRate: Double](./samplerate.md)
  The audio format sampling rate, in hertz.
- [var isInterleaved: Bool](./isinterleaved.md)
  A Boolean value that indicates whether the samples mix into one stream.
- [var commonFormat: AVAudioCommonFormat](./commonformat.md)
  The common format identifier instance.
- [var channelLayout: AVAudioChannelLayout?](./channellayout.md)
  The underlying audio channel layout.
### Creating an audio format
- [init(standardFormatWithSampleRate: Double, channelLayout: AVAudioChannelLayout)](./init%28standardformatwithsamplerate,channellayout%29.md)
  Creates an audio format instance as a deinterleaved float with the specified sample rate and channel layout.
- [init?(standardFormatWithSampleRate: Double, channels: AVAudioChannelCount)](./init%28standardformatwithsamplerate,channels%29.md)
  Creates an audio format instance with the specified sample rate and channel count.
- [init?(commonFormat: AVAudioCommonFormat, sampleRate: Double, channels: AVAudioChannelCount, interleaved: Bool)](./init%28commonformat,samplerate,channels,interleaved%29.md)
  Creates an audio format instance.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioformat/init(commonformat:samplerate:interleaved:channellayout:))*