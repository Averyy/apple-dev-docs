# allowBluetoothA2DP

**Framework**: AVFAudio  
**Kind**: property

An option that determines whether you can stream audio from this session to Bluetooth devices that support the Advanced Audio Distribution Profile (A2DP).

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static var allowBluetoothA2DP: AVAudioSession.CategoryOptions { get }
```

#### Discussion

A2DP is a stereo, output-only profile intended for higher bandwidth audio use cases, such as music playback. The system automatically routes to A2DP ports if you configure an app’s audio session to use the [`ambient`](avaudiosession/category-swift.struct/ambient.md), [`soloAmbient`](avaudiosession/category-swift.struct/soloambient.md), or [`playback`](avaudiosession/category-swift.struct/playback.md) categories.

Starting with iOS 10.0, apps using the [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md) category may also allow routing output to paired Bluetooth A2DP devices. To enable this behavior, pass this category option when setting your audio session’s category.

Audio sessions using the [`multiRoute`](avaudiosession/category-swift.struct/multiroute.md) or [`record`](avaudiosession/category-swift.struct/record.md) categories implicitly clear this option. If you clear it, paired Bluetooth A2DP devices don’t show up as available audio output routes.

> **Note**:  If this option and the [`allowBluetooth`](avaudiosession/categoryoptions-swift.struct/allowbluetooth.md) option are both set, when a single device supports both the Hands-Free Profile (HFP) and A2DP, the system gives hands-free ports a higher priority for routing.

 If this option and the [`allowBluetooth`](avaudiosession/categoryoptions-swift.struct/allowbluetooth.md) option are both set, when a single device supports both the Hands-Free Profile (HFP) and A2DP, the system gives hands-free ports a higher priority for routing.

## See Also

- [static var mixWithOthers: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/mixwithothers.md)
  An option that indicates whether audio from this session mixes with audio from active sessions in other audio apps.
- [static var duckOthers: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/duckothers.md)
  An option that reduces the volume of other audio sessions while audio from this session plays.
- [static var interruptSpokenAudioAndMixWithOthers: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/interruptspokenaudioandmixwithothers.md)
  An option that determines whether to pause spoken audio content from other sessions when your app plays its audio.
- [static var allowBluetooth: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/allowbluetooth.md)
  An option that determines whether Bluetooth hands-free devices appear as available input routes.
- [static var allowAirPlay: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/allowairplay.md)
  An option that determines whether you can stream audio from this session to AirPlay devices.
- [static var defaultToSpeaker: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/defaulttospeaker.md)
  An option that determines whether audio from the session defaults to the built-in speaker instead of the receiver.
- [static var overrideMutedMicrophoneInterruption: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/overridemutedmicrophoneinterruption.md)
  An option that indicates whether the system interrupts the audio session when it mutes the built-in microphone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/categoryoptions-swift.struct/allowbluetootha2dp)*