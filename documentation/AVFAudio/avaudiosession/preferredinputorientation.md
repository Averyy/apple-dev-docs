# preferredInputOrientation

**Framework**: AVFAudio  
**Kind**: property

The audio session’s preferred stereo input orientation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var preferredInputOrientation: AVAudioSession.StereoOrientation { get }
```

## See Also

- [var inputOrientation: AVAudioSession.StereoOrientation](avaudiosession/inputorientation.md)
  An orientation value that dictates which directions represent left and right when capturing audio from a built-in microphone configured for stereo recording.
- [func setPreferredInputOrientation(AVAudioSession.StereoOrientation) throws](avaudiosession/setpreferredinputorientation(_:).md)
  Sets the audio session’s preferred stereo input orientation.
- [AVAudioSession.StereoOrientation](avaudiosession/stereoorientation.md)
  Constants that define the supported stereo orientations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/preferredinputorientation)*