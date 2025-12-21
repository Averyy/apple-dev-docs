# allowBluetooth

**Framework**: AVFAudio  
**Kind**: property

An option that determines whether Bluetooth hands-free devices appear as available input routes.

**Availability**:
- iOS 1.0+
- iPadOS 1.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
static var allowBluetooth: AVAudioSession.CategoryOptions { get }
```

#### Discussion

You’re required to set this option to allow routing audio input and output to a paired Bluetooth Hands-Free Profile (HFP) device. If you clear this option, paired Bluetooth HFP devices don’t show up as available audio input routes.

If an application uses the [`setPreferredInput(_:)`](avaudiosession/setpreferredinput(_:).md) method to select a Bluetooth HFP input, the output automatically changes to the corresponding Bluetooth HFP output. Likewise, selecting a Bluetooth HFP output using an [`MPVolumeView`](https://developer.apple.com/documentation/MediaPlayer/MPVolumeView) object’s route picker automatically changes the input to the corresponding Bluetooth HFP input. Therefore, both audio input and output are routed to the Bluetooth HFP device even though you only selected the input or output.

You can set this option only if the audio session category is [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md) or [`record`](avaudiosession/category-swift.struct/record.md).

## See Also

- [static var allowAirPlay: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/allowairplay.md)
  An option that determines whether you can stream audio from this session to AirPlay devices.
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
- [static var overrideMutedMicrophoneInterruption: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/overridemutedmicrophoneinterruption.md)
  An option that indicates whether the system interrupts the audio session when it mutes the built-in microphone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/categoryoptions-swift.struct/allowbluetooth)*