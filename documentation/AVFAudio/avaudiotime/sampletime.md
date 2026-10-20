# sampleTime

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The time as a number of audio samples that the current audio device tracks.

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
var sampleTime: AVAudioFramePosition { get }
```

```objc
@property (nonatomic, readonly) AVAudioFramePosition sampleTime;
```

## See Also

### Getting sample rate information
- [var sampleRate: Double](./samplerate.md)
  The sampling rate that the sample time property expresses.
- [var isSampleTimeValid: Bool](./issampletimevalid.md)
  A Boolean value that indicates whether the sample time and sample rate properties are in a valid state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiotime/sampletime)*