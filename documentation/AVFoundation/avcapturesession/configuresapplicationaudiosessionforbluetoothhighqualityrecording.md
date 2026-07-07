# configuresApplicationAudioSessionForBluetoothHighQualityRecording

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the capture session configures the app’s audio session for bluetooth high-quality recording.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var configuresApplicationAudioSessionForBluetoothHighQualityRecording: Bool { get set }
```

#### Discussion

Use this property to enable using AirPods as a high-quality microphone. Set this value to `true` to tell a capture session to opt-in to high-quality bluetooth recording, which enables a person to select AirPods as the active mic source for capture. This property has no effect when the value of [`usesApplicationAudioSession`](avcapturesession/usesapplicationaudiosession.md) is `false`.

## See Also

- [var usesApplicationAudioSession: Bool](avcapturesession/usesapplicationaudiosession.md)
  A Boolean value that indicates whether the capture session uses the app’s shared audio session.
- [var automaticallyConfiguresApplicationAudioSession: Bool](avcapturesession/automaticallyconfiguresapplicationaudiosession.md)
  A Boolean value that indicates whether the capture session automatically changes settings in the app’s shared audio session.
- [var configuresApplicationAudioSessionToMixWithOthers: Bool](avcapturesession/configuresapplicationaudiosessiontomixwithothers.md)
  A Boolean value that Indicates whether the capture session configures the app’s audio session to mix with others.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/configuresapplicationaudiosessionforbluetoothhighqualityrecording)*