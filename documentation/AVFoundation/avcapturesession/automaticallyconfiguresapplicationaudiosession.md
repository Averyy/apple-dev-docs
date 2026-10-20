# automaticallyConfiguresApplicationAudioSession

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) BOOL automaticallyConfiguresApplicationAudioSession;
```

#### Discussion

This property only takes effect if the value of the [`usesApplicationAudioSession`](./usesapplicationaudiosession.md) property is [`true`](../../Swift/true.md).

The value of this property defaults to [`true`](../../Swift/true.md), causing the capture session to automatically configure the app’s shared [`AVAudioSession`](../../AVFAudio/avaudiosession.md) instance for optimal recording. For example, if the capture session uses a device’s rear-facing camera, the system sets the audio session’s microphone and polar pattern for optimal recording of sound from that direction. The audio session’s original state isn’t restored after capture finishes.

If you set value to [`false`](../../Swift/false.md), your app is responsible for selecting appropriate audio session settings. Recording may fail if the audio session’s settings are incompatible with the capture session.

## See Also

### Configuring the app’s audio session
- [var usesApplicationAudioSession: Bool](./usesapplicationaudiosession.md)
  A Boolean value that indicates whether the capture session uses the app’s shared audio session.
- [var configuresApplicationAudioSessionToMixWithOthers: Bool](./configuresapplicationaudiosessiontomixwithothers.md)
  A Boolean value that Indicates whether the capture session configures the app’s audio session to mix with others.
- [var configuresApplicationAudioSessionForBluetoothHighQualityRecording: Bool](./configuresapplicationaudiosessionforbluetoothhighqualityrecording.md)
  A Boolean value that indicates whether the capture session configures the app’s audio session for bluetooth high-quality recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/automaticallyconfiguresapplicationaudiosession)*