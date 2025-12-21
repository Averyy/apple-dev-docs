# defaultToSpeaker

**Framework**: AVFAudio  
**Kind**: property

An option that determines whether audio from the session defaults to the built-in speaker instead of the receiver.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
static var defaultToSpeaker: AVAudioSession.CategoryOptions { get }
```

#### Discussion

You can set this option only when using the [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md) category. Use it to modify the category’s routing behavior so audio is always routed to the speaker rather than the receiver, even when other accessories, such as headphones and wireless Bluetooth headphones, are in use.

When using this option, the system doesn’t honor user gestures. For example, plugging in a headset doesn’t cause the route to change to headset mic and headphones, the route remains to the built-in mic and speaker when you’ve set this override.

In the case of using a USB input-only accessory, audio input comes from the accessory, and the system routes audio to the headphones, if attached, or to the speaker if the headphones aren’t plugged in. The use case is to route audio to the speaker instead of the receiver in cases where the audio normally goes to the receiver.

> **Note**:  Route changes and interruptions don’t reset this override. Only changing the audio session category resets this option.

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
- [static var duckOthers: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/duckothers.md)
  An option that reduces the volume of other audio sessions while audio from this session plays.
- [static var farFieldInput: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/farfieldinput.md)
  This option should be used if a session prefers to use FarFieldInput when available. This option is only valid with categories that support input - [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md) and [`record`](avaudiosession/category-swift.struct/record.md).
- [static var interruptSpokenAudioAndMixWithOthers: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/interruptspokenaudioandmixwithothers.md)
  An option that determines whether to pause spoken audio content from other sessions when your app plays its audio.
- [static var mixWithOthers: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/mixwithothers.md)
  An option that indicates whether audio from this session mixes with audio from active sessions in other audio apps.
- [static var overrideMutedMicrophoneInterruption: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/overridemutedmicrophoneinterruption.md)
  An option that indicates whether the system interrupts the audio session when it mutes the built-in microphone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/categoryoptions-swift.struct/defaulttospeaker)*