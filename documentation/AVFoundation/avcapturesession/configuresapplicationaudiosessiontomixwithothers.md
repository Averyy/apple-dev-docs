# configuresApplicationAudioSessionToMixWithOthers

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) BOOL configuresApplicationAudioSessionToMixWithOthers;
```

## Discussion

By default, a capture session’s audio session interrupts the audio of other apps. To enable background audio from other apps to continue while capturing video, set this value to [`true`](../../Swift/true.md).

> **Note**:  This property value has no effect when the value of [`usesApplicationAudioSession`](./usesapplicationaudiosession.md) is [`false`](../../Swift/false.md). It also has no effect on Live Photo movie complement capture (where music is always mixed).

The default value is [`false`](../../Swift/false.md).

## See Also

### Configuring the app’s audio session
- [var usesApplicationAudioSession: Bool](./usesapplicationaudiosession.md)
  A Boolean value that indicates whether the capture session uses the app’s shared audio session.
- [var automaticallyConfiguresApplicationAudioSession: Bool](./automaticallyconfiguresapplicationaudiosession.md)
  A Boolean value that indicates whether the capture session automatically changes settings in the app’s shared audio session.
- [var configuresApplicationAudioSessionForBluetoothHighQualityRecording: Bool](./configuresapplicationaudiosessionforbluetoothhighqualityrecording.md)
  A Boolean value that indicates whether the capture session configures the app’s audio session for bluetooth high-quality recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/configuresapplicationaudiosessiontomixwithothers)*