# setPreferredInputOrientation(_:)

**Framework**: AVFAudio  
**Kind**: method

Sets the audio session’s preferred stereo input orientation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func setPreferredInputOrientation(_ orientation: AVAudioSession.StereoOrientation) throws
```

#### Discussion

Configure the input orientation to match how the user is holding the device when they begin recording. In a single-window app, set the input orientation to a value corresponding to the app’s user interface orientation.

## Parameters

- `orientation`: The stereo orientation.

## See Also

- [var inputOrientation: AVAudioSession.StereoOrientation](avaudiosession/inputorientation.md)
  An orientation value that dictates which directions represent left and right when capturing audio from a built-in microphone configured for stereo recording.
- [var preferredInputOrientation: AVAudioSession.StereoOrientation](avaudiosession/preferredinputorientation.md)
  The audio session’s preferred stereo input orientation.
- [AVAudioSession.StereoOrientation](avaudiosession/stereoorientation.md)
  Constants that define the supported stereo orientations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setpreferredinputorientation(_:))*