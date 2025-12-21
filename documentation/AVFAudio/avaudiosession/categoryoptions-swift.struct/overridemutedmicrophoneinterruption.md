# overrideMutedMicrophoneInterruption

**Framework**: AVFAudio  
**Kind**: property

An option that indicates whether the system interrupts the audio session when it mutes the built-in microphone.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+
- watchOS 7.3+

## Declaration

```swift
static var overrideMutedMicrophoneInterruption: AVAudioSession.CategoryOptions { get }
```

## Mentions

- [Handling audio interruptions](handling-audio-interruptions.md)

#### Discussion

Some devices include a privacy feature that mutes the built-in microphone at the hardware level in certain conditions, such as when you close the Smart Folio cover of an iPad. When this occurs, the system interrupts the audio session that’s capturing input from the microphone. Attempting to start audio input after the system mutes the microphone results in an error.

If your app uses an audio session category that supports input and output, such as [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md), you can set this option to disable the default behavior and continue using the session. Disabling the default behavior may be useful to allow your app to continue playback when recording or monitoring a muted microphone doesn’t lead to a poor user experience. When you set this option, playback continues as normal, and the microphone hardware produces sample buffers, but with values of `0`.

> ❗ **Important**:  Attempting to use this option with a session category that doesn’t support audio input results in an error.

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
- [static var duckOthers: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/duckothers.md)
  An option that reduces the volume of other audio sessions while audio from this session plays.
- [static var farFieldInput: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/farfieldinput.md)
  This option should be used if a session prefers to use FarFieldInput when available. This option is only valid with categories that support input - [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md) and [`record`](avaudiosession/category-swift.struct/record.md).
- [static var interruptSpokenAudioAndMixWithOthers: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/interruptspokenaudioandmixwithothers.md)
  An option that determines whether to pause spoken audio content from other sessions when your app plays its audio.
- [static var mixWithOthers: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/mixwithothers.md)
  An option that indicates whether audio from this session mixes with audio from active sessions in other audio apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/categoryoptions-swift.struct/overridemutedmicrophoneinterruption)*