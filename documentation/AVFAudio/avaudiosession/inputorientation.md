# inputOrientation

**Framework**: AVFAudio  
**Kind**: property

An orientation value that dictates which directions represent left and right when capturing audio from a built-in microphone configured for stereo recording.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var inputOrientation: AVAudioSession.StereoOrientation { get }
```

#### Discussion

If you’re recording video, set the input orientation to match the video orientation. If you’re recording audio only, set the input orientation to match the user interface orientation. In either case, don’t modify the input orientation during recording.

> ❗ **Important**:  The audio session’s input orientation is independent of the [`orientation`](avaudiosessiondatasourcedescription/orientation.md) property of an [`AVAudioSessionDataSourceDescription`](avaudiosessiondatasourcedescription.md).

 The audio session’s input orientation is independent of the [`orientation`](avaudiosessiondatasourcedescription/orientation.md) property of an [`AVAudioSessionDataSourceDescription`](avaudiosessiondatasourcedescription.md).

## See Also

- [var preferredInputOrientation: AVAudioSession.StereoOrientation](avaudiosession/preferredinputorientation.md)
  The audio session’s preferred stereo input orientation.
- [func setPreferredInputOrientation(AVAudioSession.StereoOrientation) throws](avaudiosession/setpreferredinputorientation(_:).md)
  Sets the audio session’s preferred stereo input orientation.
- [AVAudioSession.StereoOrientation](avaudiosession/stereoorientation.md)
  Constants that define the supported stereo orientations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/inputorientation)*