# setAggregatedIOPreference(_:)

**Framework**: AVFAudio  
**Kind**: method

Sets the audio session’s aggregated I/O configuration preference.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setAggregatedIOPreference(_ inIOType: AVAudioSession.IOType) throws
```

#### Discussion

Starting with iOS 10, [`AVCaptureSession`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession) has changed its default audio input configuration on iPhone and iPad devices that support the Live Photos feature. This change allows taking a Live Photo without interrupting background audio playback. Configure your preferred audio input behavior by setting your aggregated I/O preference.

Apps that use [`AVCaptureSession`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession) in its default audio input configuration ([`usesApplicationAudioSession`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession/usesApplicationAudioSession) `=` [`true`](https://developer.apple.com/documentation/Swift/true), [`automaticallyConfiguresApplicationAudioSession`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession/automaticallyConfiguresApplicationAudioSession) `=` [`true`](https://developer.apple.com/documentation/Swift/true)), and that need to guarantee the same behavior as previous versions of iOS, should opt-out of this new behavior by setting the aggregated I/O preference to [`AVAudioSession.IOType.aggregated`](avaudiosession/iotype/aggregated.md).

Apps that don’t use [`AVCaptureSession`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession), or that use a capture session in its nondefault configuration, can ignore this preference. In these cases, there’s no change in behavior from previous versions of iOS.

## Parameters

- `inIOType`: The aggregated I/O preference that you want to use.

## See Also

- [AVAudioSession.IOType](avaudiosession/iotype.md)
  Constant values used to specify the audio session’s aggregated I/O behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setaggregatediopreference(_:))*