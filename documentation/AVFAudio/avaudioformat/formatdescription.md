# formatDescription

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The audio format description to use with Core Media APIs.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var formatDescription: CMAudioFormatDescription { get }
```

```objc
@property (nonatomic, readonly) CMAudioFormatDescriptionRef formatDescription;
```

## See Also

### Getting audio format values
- [var sampleRate: Double](./samplerate.md)
  The audio format sampling rate, in hertz.
- [var channelCount: AVAudioChannelCount](./channelcount.md)
  The number of channels of audio data.
- [var channelLayout: AVAudioChannelLayout?](./channellayout.md)
  The underlying audio channel layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioformat/formatdescription)*