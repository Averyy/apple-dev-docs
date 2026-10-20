# subcardioid

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

A data source that’s most sensitive to sound from the direction of the data source and is less sensitive to sound from the opposite direction.

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
static let subcardioid: AVAudioSession.PolarPattern
```

```c
extern AVAudioSessionPolarPattern const AVAudioSessionPolarPatternSubcardioid;
```

#### Discussion

The subcardioid pattern picks up a sound from a wide radius in the front and in the back.

![The subcardioid pattern picks up more sound from the direction of the data source than from the rear. ](https://developer.apple.com/tutorials/images/com.apple.avfaudio/media-3039130@2x.png)

## See Also

### Getting standard polar patterns
- [static let stereo: AVAudioSession.PolarPattern](./stereo.md)
  A polar pattern that captures a stereo image of an audio source.
- [static let cardioid: AVAudioSession.PolarPattern](./cardioid.md)
  A data source that’s most sensitive to sound from the direction of the data source and is nearly insensitive to sound from the opposite direction.
- [static let omnidirectional: AVAudioSession.PolarPattern](./omnidirectional.md)
  A data source that’s equally sensitive to sound from any direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/polarpattern/subcardioid)*