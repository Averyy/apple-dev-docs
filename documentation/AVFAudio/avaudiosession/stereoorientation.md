# AVAudioSession.StereoOrientation

**Framework**: AVFAudio  
**Kind**: enum

Constants that define the supported stereo orientations.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum StereoOrientation
```

## Topics

### Stereo Orientations
- [AVAudioSession.StereoOrientation.none](avaudiosession/stereoorientation/none.md)
  The audio session isn’t configured for stereo recording.
- [AVAudioSession.StereoOrientation.portrait](avaudiosession/stereoorientation/portrait.md)
  Audio capture should be vertically oriented, with the USB-C or Lightning connector on the bottom.
- [AVAudioSession.StereoOrientation.portraitUpsideDown](avaudiosession/stereoorientation/portraitupsidedown.md)
  Audio capture should be vertically oriented, with the USB-C or Lightning connector on the top.
- [AVAudioSession.StereoOrientation.landscapeRight](avaudiosession/stereoorientation/landscaperight.md)
  Audio capture should be horizontally oriented, with the USB-C or Lightning connector on the right.
- [AVAudioSession.StereoOrientation.landscapeLeft](avaudiosession/stereoorientation/landscapeleft.md)
  Audio capture should be horizontally oriented, with the USB-C or Lightning connector on the left.
### Initializers
- [init?(rawValue: Int)](avaudiosession/stereoorientation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var inputOrientation: AVAudioSession.StereoOrientation](avaudiosession/inputorientation.md)
  An orientation value that dictates which directions represent left and right when capturing audio from a built-in microphone configured for stereo recording.
- [var preferredInputOrientation: AVAudioSession.StereoOrientation](avaudiosession/preferredinputorientation.md)
  The audio session’s preferred stereo input orientation.
- [func setPreferredInputOrientation(AVAudioSession.StereoOrientation) throws](avaudiosession/setpreferredinputorientation(_:).md)
  Sets the audio session’s preferred stereo input orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/stereoorientation)*