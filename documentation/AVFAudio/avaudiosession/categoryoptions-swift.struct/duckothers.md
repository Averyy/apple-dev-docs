# duckOthers

**Framework**: AVFAudio  
**Kind**: property

An option that reduces the volume of other audio sessions while audio from this session plays.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
static var duckOthers: AVAudioSession.CategoryOptions { get }
```

#### Discussion

You can set this option only if the audio session category is [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md), [`playback`](avaudiosession/category-swift.struct/playback.md), or [`multiRoute`](avaudiosession/category-swift.struct/multiroute.md). Setting it implicitly sets the [`mixWithOthers`](avaudiosession/categoryoptions-swift.struct/mixwithothers.md) option.

Use this option to mix your app’s audio with that of others. While your app plays audio, the system reduces the volume of other audio sessions to make yours more prominent. If your app provides occasional spoken audio, such as in a turn-by-turn navigation app or an exercise app, you should also set the [`interruptSpokenAudioAndMixWithOthers`](avaudiosession/categoryoptions-swift.struct/interruptspokenaudioandmixwithothers.md) option.

Ducking begins when you activate your app’s audio session and ends when you deactivate the session. If you clear this option, activating your session interrupts other audio sessions.

> ❗ **Important**:  Set this option on a temporary basis only. Don’t use it to duck the audio of other apps for more than a few seconds.

## See Also

- [static var allowAirPlay: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/allowairplay.md)
  An option that determines whether you can stream audio from this session to AirPlay devices.
- [static var allowBluetooth: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/allowbluetooth.md)
  An option that determines whether Bluetooth hands-free devices appear as available input routes.
- [static var allowBluetoothA2DP: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/allowbluetootha2dp.md)
  An option that determines whether you can stream audio from this session to Bluetooth devices that support the Advanced Audio Distribution Profile (A2DP).
- [static var allowBluetoothHFP: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/allowbluetoothhfp.md)
  An option that makes Bluetooth Hands-Free Profile (HFP) devices available for audio input.
- [static var bluetoothHighQualityRecording: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/bluetoothhighqualityrecording.md)
  An option that indicates to enable high-quality audio for input and output routes.
- [static var defaultToSpeaker: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/defaulttospeaker.md)
  An option that determines whether audio from the session defaults to the built-in speaker instead of the receiver.
- [static var farFieldInput: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/farfieldinput.md)
  This option should be used if a session prefers to use FarFieldInput when available. This option is only valid with categories that support input - [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md) and [`record`](avaudiosession/category-swift.struct/record.md).
- [static var interruptSpokenAudioAndMixWithOthers: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/interruptspokenaudioandmixwithothers.md)
  An option that determines whether to pause spoken audio content from other sessions when your app plays its audio.
- [static var mixWithOthers: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/mixwithothers.md)
  An option that indicates whether audio from this session mixes with audio from active sessions in other audio apps.
- [static var overrideMutedMicrophoneInterruption: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/overridemutedmicrophoneinterruption.md)
  An option that indicates whether the system interrupts the audio session when it mutes the built-in microphone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/categoryoptions-swift.struct/duckothers)*