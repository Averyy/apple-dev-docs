# subcardioid

**Framework**: AVFAudio  
**Kind**: property

A data source that’s most sensitive to sound from the direction of the data source and is less sensitive to sound from the opposite direction.

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
static let subcardioid: AVAudioSession.PolarPattern
```

#### Discussion

The subcardioid pattern picks up a sound from a wide radius in the front and in the back.

![The subcardioid pattern picks up more sound from the direction of the data source than from the rear. ](https://docs-assets.developer.apple.com/published/0acc584378e763be5f567d2e4921f04c/media-3039130%402x.png)

## See Also

- [static let stereo: AVAudioSession.PolarPattern](avaudiosession/polarpattern/stereo.md)
  A polar pattern that captures a stereo image of an audio source.
- [static let cardioid: AVAudioSession.PolarPattern](avaudiosession/polarpattern/cardioid.md)
  A data source that’s most sensitive to sound from the direction of the data source and is nearly insensitive to sound from the opposite direction.
- [static let omnidirectional: AVAudioSession.PolarPattern](avaudiosession/polarpattern/omnidirectional.md)
  A data source that’s equally sensitive to sound from any direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/polarpattern/subcardioid)*