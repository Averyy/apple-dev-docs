# channelLayout

**Framework**: AVFAudio  
**Kind**: property

The underlying audio channel layout.

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
var channelLayout: AVAudioChannelLayout? { get }
```

#### Discussion

Only formats with more than two channels require channel layouts.

## See Also

- [var sampleRate: Double](avaudioformat/samplerate.md)
  The audio format sampling rate, in hertz.
- [var channelCount: AVAudioChannelCount](avaudioformat/channelcount.md)
  The number of channels of audio data.
- [var formatDescription: CMAudioFormatDescription](avaudioformat/formatdescription.md)
  The audio format description to use with Core Media APIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioformat/channellayout)*