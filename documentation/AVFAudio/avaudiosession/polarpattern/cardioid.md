# cardioid

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

A data source that’s most sensitive to sound from the direction of the data source and is nearly insensitive to sound from the opposite direction.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let cardioid: AVAudioSession.PolarPattern
```

```c
extern AVAudioSessionPolarPattern const AVAudioSessionPolarPatternCardioid;
```

#### Discussion

The cardioid pattern is heart-shaped and picks up most sound from the front side.

![The cardioid pattern picks up sound from the direction of the data source. ](https://developer.apple.com/tutorials/images/com.apple.avfaudio/media-3039129@2x.png)

## See Also

### Getting standard polar patterns
- [static let stereo: AVAudioSession.PolarPattern](./stereo.md)
  A polar pattern that captures a stereo image of an audio source.
- [static let subcardioid: AVAudioSession.PolarPattern](./subcardioid.md)
  A data source that’s most sensitive to sound from the direction of the data source and is less sensitive to sound from the opposite direction.
- [static let omnidirectional: AVAudioSession.PolarPattern](./omnidirectional.md)
  A data source that’s equally sensitive to sound from any direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/polarpattern/cardioid)*