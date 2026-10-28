# init(settings:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithSettings:(NSDictionary<NSString *,id> *) settings;
```

## Return Value

A new `AVAudioFormat` instance, or `nil` if the initialization fails.

## Discussion

Note that many settings dictionary elements aren’t relevant for the format, so this method ignores them. For information about supported dictionary values, see [Audio settings](../../AVFoundation/audio-settings.md).

## Parameters

- `settings`: The settings dictionary.

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
- [init?(streamDescription: UnsafePointer<AudioStreamBasicDescription>)](./init%28streamdescription%29.md)
  Creates an audio format instance from a stream description.
- [init?(streamDescription: UnsafePointer<AudioStreamBasicDescription>, channelLayout: AVAudioChannelLayout?)](./init%28streamdescription,channellayout%29.md)
  Creates an audio format instance from a stream description and channel layout.
- [init?(formatDescription: CMAudioFormatDescription)](./init%28formatdescription%29.md)
- [init(cmAudioFormatDescription: CMAudioFormatDescription)](./init%28cmaudioformatdescription%29-8rdfj.md)
  Creates an audio format instance from a Core Media audio format description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioformat/init(settings:))*