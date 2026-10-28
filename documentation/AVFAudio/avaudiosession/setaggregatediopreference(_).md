# setAggregatedIOPreference(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) setAggregatedIOPreference:(AVAudioSessionIOType) inIOType error:(NSError **) outError;
```

## Discussion

Starting with iOS 10, [`AVCaptureSession`](../../AVFoundation/avcapturesession.md) has changed its default audio input configuration on iPhone and iPad devices that support the Live Photos feature. This change allows taking a Live Photo without interrupting background audio playback. Configure your preferred audio input behavior by setting your aggregated I/O preference.

Apps that use [`AVCaptureSession`](../../AVFoundation/avcapturesession.md) in its default audio input configuration ([`usesApplicationAudioSession`](../../AVFoundation/avcapturesession/usesapplicationaudiosession.md) `=` [`true`](../../Swift/true.md), [`automaticallyConfiguresApplicationAudioSession`](../../AVFoundation/avcapturesession/automaticallyconfiguresapplicationaudiosession.md) `=` [`true`](../../Swift/true.md)), and that need to guarantee the same behavior as previous versions of iOS, should opt-out of this new behavior by setting the aggregated I/O preference to [`AVAudioSession.IOType.aggregated`](./iotype/aggregated.md).

Apps that don’t use [`AVCaptureSession`](../../AVFoundation/avcapturesession.md), or that use a capture session in its nondefault configuration, can ignore this preference. In these cases, there’s no change in behavior from previous versions of iOS.

## Parameters

- `inIOType`: The aggregated I/O preference that you want to use.

## See Also

### Setting the aggregated I/O preference
- [AVAudioSession.IOType](./iotype.md)
  Constant values used to specify the audio session’s aggregated I/O behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setaggregatediopreference(_:))*