# usesApplicationAudioSession

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) BOOL usesApplicationAudioSession;
```

#### Discussion

The default value is [`true`](../../Swift/true.md). If you set the value to [`false`](../../Swift/false.md), the capture session uses a private [`AVAudioSession`](../../AVFAudio/avaudiosession.md) instance for audio recording, which may cause interruptions if your app uses its own audio session for playback.

## See Also

### Configuring the app’s audio session
- [var automaticallyConfiguresApplicationAudioSession: Bool](./automaticallyconfiguresapplicationaudiosession.md)
  A Boolean value that indicates whether the capture session automatically changes settings in the app’s shared audio session.
- [var configuresApplicationAudioSessionToMixWithOthers: Bool](./configuresapplicationaudiosessiontomixwithothers.md)
  A Boolean value that Indicates whether the capture session configures the app’s audio session to mix with others.
- [var configuresApplicationAudioSessionForBluetoothHighQualityRecording: Bool](./configuresapplicationaudiosessionforbluetoothhighqualityrecording.md)
  A Boolean value that indicates whether the capture session configures the app’s audio session for bluetooth high-quality recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/usesapplicationaudiosession)*