# automaticallyConfiguresApplicationAudioSession

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the capture session automatically changes settings in the app’s shared audio session.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var automaticallyConfiguresApplicationAudioSession: Bool { get set }
```

#### Discussion

This property only takes effect if the value of the [`usesApplicationAudioSession`](avcapturesession/usesapplicationaudiosession.md) property is [`true`](https://developer.apple.com/documentation/swift/true).

The value of this property defaults to [`true`](https://developer.apple.com/documentation/swift/true), causing the capture session to automatically configure the app’s shared [`AVAudioSession`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession) instance for optimal recording. For example, if the capture session uses a device’s rear-facing camera, the system sets the audio session’s microphone and polar pattern for optimal recording of sound from that direction. The audio session’s original state isn’t restored after capture finishes.

If you set value to [`false`](https://developer.apple.com/documentation/swift/false), your app is responsible for selecting appropriate audio session settings. Recording may fail if the audio session’s settings are incompatible with the capture session.

## See Also

- [var usesApplicationAudioSession: Bool](avcapturesession/usesapplicationaudiosession.md)
  A Boolean value that indicates whether the capture session uses the app’s shared audio session.
- [var configuresApplicationAudioSessionToMixWithOthers: Bool](avcapturesession/configuresapplicationaudiosessiontomixwithothers.md)
  A Boolean value that Indicates whether the capture session configures the app’s audio session to mix with others.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/automaticallyconfiguresapplicationaudiosession)*