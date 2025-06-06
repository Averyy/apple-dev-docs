# mixWithOthers

**Framework**: AVFAudio  
**Kind**: property

An option that indicates whether audio from this session mixes with audio from active sessions in other audio apps.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
static var mixWithOthers: AVAudioSession.CategoryOptions { get }
```

#### Discussion

You can set this option explicitly only if the audio session category is [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md), [`playback`](avaudiosession/category-swift.struct/playback.md), or [`multiRoute`](avaudiosession/category-swift.struct/multiroute.md). If you set the audio session category to [`ambient`](avaudiosession/category-swift.struct/ambient.md), the session automatically sets this option. Likewise, setting the [`duckOthers`](avaudiosession/categoryoptions-swift.struct/duckothers.md) or [`interruptSpokenAudioAndMixWithOthers`](avaudiosession/categoryoptions-swift.struct/interruptspokenaudioandmixwithothers.md) options also enables this option.

Clearing this option and then activating your session interrupts other audio sessions. If you set this option, your app mixes its audio with audio playing in background apps, such as the Music app.

## See Also

- [static var duckOthers: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/duckothers.md)
  An option that reduces the volume of other audio sessions while audio from this session plays.
- [static var interruptSpokenAudioAndMixWithOthers: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/interruptspokenaudioandmixwithothers.md)
  An option that determines whether to pause spoken audio content from other sessions when your app plays its audio.
- [static var allowBluetooth: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/allowbluetooth.md)
  An option that determines whether Bluetooth hands-free devices appear as available input routes.
- [static var allowBluetoothA2DP: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/allowbluetootha2dp.md)
  An option that determines whether you can stream audio from this session to Bluetooth devices that support the Advanced Audio Distribution Profile (A2DP).
- [static var allowAirPlay: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/allowairplay.md)
  An option that determines whether you can stream audio from this session to AirPlay devices.
- [static var defaultToSpeaker: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/defaulttospeaker.md)
  An option that determines whether audio from the session defaults to the built-in speaker instead of the receiver.
- [static var overrideMutedMicrophoneInterruption: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/overridemutedmicrophoneinterruption.md)
  An option that indicates whether the system interrupts the audio session when it mutes the built-in microphone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/categoryoptions-swift.struct/mixwithothers)*