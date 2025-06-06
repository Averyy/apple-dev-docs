# cardioid

**Framework**: AVFAudio  
**Kind**: property

A data source that’s most sensitive to sound from the direction of the data source and is nearly insensitive to sound from the opposite direction.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS ?+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let cardioid: AVAudioSession.PolarPattern
```

#### Discussion

The cardioid pattern is heart-shaped and picks up most sound from the front side.

![The cardioid pattern picks up sound from the direction of the data source. ](https://docs-assets.developer.apple.com/published/f888c0f9c3ee232680a47b771c6b6f81/media-3039129%402x.png)

## See Also

- [static let stereo: AVAudioSession.PolarPattern](avaudiosession/polarpattern/stereo.md)
  A polar pattern that captures a stereo image of an audio source.
- [static let subcardioid: AVAudioSession.PolarPattern](avaudiosession/polarpattern/subcardioid.md)
  A data source that’s most sensitive to sound from the direction of the data source and is less sensitive to sound from the opposite direction.
- [static let omnidirectional: AVAudioSession.PolarPattern](avaudiosession/polarpattern/omnidirectional.md)
  A data source that’s equally sensitive to sound from any direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/polarpattern/cardioid)*