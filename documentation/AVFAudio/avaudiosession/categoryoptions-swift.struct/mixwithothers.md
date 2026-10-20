# mixWithOthers

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

An option that indicates whether audio from this session mixes with audio from active sessions in other audio apps.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
static var mixWithOthers: AVAudioSession.CategoryOptions { get }
```

```c
AVAudioSessionCategoryOptionMixWithOthers
```

#### Discussion

You can set this option explicitly only if the audio session category is [`playAndRecord`](../category-swift.struct/playandrecord.md), [`playback`](../category-swift.struct/playback.md), or [`multiRoute`](../category-swift.struct/multiroute.md). If you set the audio session category to [`ambient`](../category-swift.struct/ambient.md), the session automatically sets this option. Likewise, setting the [`duckOthers`](./duckothers.md) or [`interruptSpokenAudioAndMixWithOthers`](./interruptspokenaudioandmixwithothers.md) options also enables this option.

Clearing this option and then activating your session interrupts other audio sessions. If you set this option, your app mixes its audio with audio playing in background apps, such as the Music app.

## See Also

### Getting standard category options
- [static var allowAirPlay: AVAudioSession.CategoryOptions](./allowairplay.md)
  An option that determines whether you can stream audio from this session to AirPlay devices.
- [static var allowBluetooth: AVAudioSession.CategoryOptions](./allowbluetooth.md)
  An option that determines whether Bluetooth hands-free devices appear as available input routes.
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
- [static var overrideMutedMicrophoneInterruption: AVAudioSession.CategoryOptions](./overridemutedmicrophoneinterruption.md)
  An option that indicates whether the system interrupts the audio session when it mutes the built-in microphone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/categoryoptions-swift.struct/mixwithothers)*