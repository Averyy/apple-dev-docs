# AVAudioSession.StereoOrientation

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Constants that define the supported stereo orientations.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum StereoOrientation
```

```c
enum AVAudioStereoOrientation : NSInteger;
```

## Topics

### Creating a stereo orientation
- [init?(rawValue: Int)](./stereoorientation/init%28rawvalue%29.md)
### Choosing a stereo orientation
- [AVAudioSession.StereoOrientation.none](./stereoorientation/none.md)
  The audio session isn’t configured for stereo recording.
- [AVAudioSession.StereoOrientation.portrait](./stereoorientation/portrait.md)
  Audio capture should be vertically oriented, with the USB-C or Lightning connector on the bottom.
- [AVAudioSession.StereoOrientation.portraitUpsideDown](./stereoorientation/portraitupsidedown.md)
  Audio capture should be vertically oriented, with the USB-C or Lightning connector on the top.
- [AVAudioSession.StereoOrientation.landscapeRight](./stereoorientation/landscaperight.md)
  Audio capture should be horizontally oriented, with the USB-C or Lightning connector on the right.
- [AVAudioSession.StereoOrientation.landscapeLeft](./stereoorientation/landscapeleft.md)
  Audio capture should be horizontally oriented, with the USB-C or Lightning connector on the left.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Enabling stereo recording
- [var inputOrientation: AVAudioSession.StereoOrientation](./inputorientation.md)
  An orientation value that dictates which directions represent left and right when capturing audio from a built-in microphone configured for stereo recording.
- [var preferredInputOrientation: AVAudioSession.StereoOrientation](./preferredinputorientation.md)
  The audio session’s preferred stereo input orientation.
- [func setPreferredInputOrientation(AVAudioSession.StereoOrientation) throws](./setpreferredinputorientation%28_%29.md)
  Sets the audio session’s preferred stereo input orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/stereoorientation)*