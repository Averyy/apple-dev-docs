# usesApplicationAudioSession

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the capture session uses the app’s shared audio session.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var usesApplicationAudioSession: Bool { get set }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/Swift/true). If you set the value to [`false`](https://developer.apple.com/documentation/Swift/false), the capture session uses a private [`AVAudioSession`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession) instance for audio recording, which may cause interruptions if your app uses its own audio session for playback.

## See Also

- [var automaticallyConfiguresApplicationAudioSession: Bool](avcapturesession/automaticallyconfiguresapplicationaudiosession.md)
  A Boolean value that indicates whether the capture session automatically changes settings in the app’s shared audio session.
- [var configuresApplicationAudioSessionToMixWithOthers: Bool](avcapturesession/configuresapplicationaudiosessiontomixwithothers.md)
  A Boolean value that Indicates whether the capture session configures the app’s audio session to mix with others.
- [var configuresApplicationAudioSessionForBluetoothHighQualityRecording: Bool](avcapturesession/configuresapplicationaudiosessionforbluetoothhighqualityrecording.md)
  A Boolean value that indicates whether the capture session configures the app’s audio session for bluetooth high-quality recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/usesapplicationaudiosession)*