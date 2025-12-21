# configuresApplicationAudioSessionToMixWithOthers

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that Indicates whether the capture session configures the app’s audio session to mix with others.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+

## Declaration

```swift
var configuresApplicationAudioSessionToMixWithOthers: Bool { get set }
```

#### Discussion

By default, a capture session’s audio session interrupts the audio of other apps. To enable background audio from other apps to continue while capturing video, set this value to [`true`](https://developer.apple.com/documentation/Swift/true).

> **Note**:  This property value has no effect when the value of [`usesApplicationAudioSession`](avcapturesession/usesapplicationaudiosession.md) is [`false`](https://developer.apple.com/documentation/Swift/false). It also has no effect on Live Photo movie complement capture (where music is always mixed).

The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var usesApplicationAudioSession: Bool](avcapturesession/usesapplicationaudiosession.md)
  A Boolean value that indicates whether the capture session uses the app’s shared audio session.
- [var automaticallyConfiguresApplicationAudioSession: Bool](avcapturesession/automaticallyconfiguresapplicationaudiosession.md)
  A Boolean value that indicates whether the capture session automatically changes settings in the app’s shared audio session.
- [var configuresApplicationAudioSessionForBluetoothHighQualityRecording: Bool](avcapturesession/configuresapplicationaudiosessionforbluetoothhighqualityrecording.md)
  A Boolean value that indicates whether the capture session configures the app’s audio session for bluetooth high-quality recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/configuresapplicationaudiosessiontomixwithothers)*