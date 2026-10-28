# allowBluetooth

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

An option that determines whether Bluetooth hands-free devices appear as available input routes.

**Availability**:
- iOS 1.0+ - Deprecated in 8.0 (renamed: AVAudioSession.CategoryOptions.allowBluetoothHFP)
- iPadOS 1.0+ - Deprecated in 8.0 (renamed: AVAudioSession.CategoryOptions.allowBluetoothHFP)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: AVAudioSession.CategoryOptions.allowBluetoothHFP)
- tvOS 17.0+ - Deprecated in 17.0 (renamed: AVAudioSession.CategoryOptions.allowBluetoothHFP)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: AVAudioSession.CategoryOptions.allowBluetoothHFP)
- watchOS 11.0+ - Deprecated in 11.0 (renamed: AVAudioSession.CategoryOptions.allowBluetoothHFP)

## Declaration

```swift
static var allowBluetooth: AVAudioSession.CategoryOptions { get }
```

```c
AVAudioSessionCategoryOptionAllowBluetooth
```

## Discussion

You’re required to set this option to allow routing audio input and output to a paired Bluetooth Hands-Free Profile (HFP) device. If you clear this option, paired Bluetooth HFP devices don’t show up as available audio input routes.

If an application uses the [`setPreferredInput(_:)`](../setpreferredinput%28_%29.md) method to select a Bluetooth HFP input, the output automatically changes to the corresponding Bluetooth HFP output. Likewise, selecting a Bluetooth HFP output using an [`MPVolumeView`](../../../MediaPlayer/mpvolumeview.md) object’s route picker automatically changes the input to the corresponding Bluetooth HFP input. Therefore, both audio input and output are routed to the Bluetooth HFP device even though you only selected the input or output.

You can set this option only if the audio session category is [`playAndRecord`](../category-swift.struct/playandrecord.md) or [`record`](../category-swift.struct/record.md).

## See Also

### Getting standard category options
- [static var allowAirPlay: AVAudioSession.CategoryOptions](./allowairplay.md)
  An option that determines whether you can stream audio from this session to AirPlay devices.
- [static var allowBluetoothA2DP: AVAudioSession.CategoryOptions](./allowbluetootha2dp.md)
  An option that determines whether you can stream audio from this session to Bluetooth devices that support the Advanced Audio Distribution Profile (A2DP).
- [static var allowBluetoothHFP: AVAudioSession.CategoryOptions](./allowbluetoothhfp.md)
  An option that makes Bluetooth Hands-Free Profile (HFP) devices available for audio input.
- [static var bluetoothHighQualityRecording: AVAudioSession.CategoryOptions](./bluetoothhighqualityrecording.md)
  An option that indicates to enable high-quality audio for input and output routes.
- [static var defaultToSpeaker: AVAudioSession.CategoryOptions](./defaulttospeaker.md)
  An option that determines whether audio from the session defaults to the built-in speaker instead of the receiver.
- [static var duckOthers: AVAudioSession.CategoryOptions](./duckothers.md)
  An option that reduces the volume of other audio sessions while audio from this session plays.
- [static var farFieldInput: AVAudioSession.CategoryOptions](./farfieldinput.md)
  This option should be used if a session prefers to use FarFieldInput when available. This option is only valid with categories that support input - [`playAndRecord`](../category-swift.struct/playandrecord.md), [`record`](../category-swift.struct/record.md), and `AVAudioSessionMultiRoute` with [`dualRoute`](../mode-swift.struct/dualroute.md).
- [static var interruptSpokenAudioAndMixWithOthers: AVAudioSession.CategoryOptions](./interruptspokenaudioandmixwithothers.md)
  An option that determines whether to pause spoken audio content from other sessions when your app plays its audio.
- [static var mixWithOthers: AVAudioSession.CategoryOptions](./mixwithothers.md)
  An option that indicates whether audio from this session mixes with audio from active sessions in other audio apps.
- [static var overrideMutedMicrophoneInterruption: AVAudioSession.CategoryOptions](./overridemutedmicrophoneinterruption.md)
  An option that indicates whether the system interrupts the audio session when it mutes the built-in microphone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/categoryoptions-swift.struct/allowbluetooth)*