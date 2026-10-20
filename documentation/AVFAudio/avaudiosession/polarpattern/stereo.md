# stereo

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

A polar pattern that captures a stereo image of an audio source.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
static let stereo: AVAudioSession.PolarPattern
```

```c
extern AVAudioSessionPolarPattern const AVAudioSessionPolarPatternStereo;
```

#### Discussion

If you select a data source with this polar pattern, call [`setPreferredInputOrientation(_:)`](../setpreferredinputorientation%28_%29.md) on your audio session to ensure that left and right are correctly oriented in the captured audio.

## See Also

### Getting standard polar patterns
- [static let cardioid: AVAudioSession.PolarPattern](./cardioid.md)
  A data source that’s most sensitive to sound from the direction of the data source and is nearly insensitive to sound from the opposite direction.
- [static let subcardioid: AVAudioSession.PolarPattern](./subcardioid.md)
  A data source that’s most sensitive to sound from the direction of the data source and is less sensitive to sound from the opposite direction.
- [static let omnidirectional: AVAudioSession.PolarPattern](./omnidirectional.md)
  A data source that’s equally sensitive to sound from any direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/polarpattern/stereo)*