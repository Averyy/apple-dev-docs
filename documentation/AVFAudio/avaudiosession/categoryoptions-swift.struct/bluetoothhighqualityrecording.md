# bluetoothHighQualityRecording

**Framework**: AVFAudio  
**Kind**: property

An option that indicates to enable high-quality audio for input and output routes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
static var bluetoothHighQualityRecording: AVAudioSession.CategoryOptions { get }
```

#### Discussion

Specifying this option enables full-bandwidth audio when the Bluetooth route supports it, such as on certain AirPods models. You can combine it with the [`allowBluetoothHFP`](avaudiosession/categoryoptions-swift.struct/allowbluetoothhfp.md) option, which the audio session uses as a fallback when the audio route doesn’t support the feature. You can request high-quality recording only when using the [`default`](avaudiosession/mode-swift.struct/default.md) audio session mode.

> ❗ **Important**: Bluetooth high-quality recording isn’t currently supported in the European Union.

To determine whether a Bluetooth input port supports high-quality recording, access its [`bluetoothMicrophoneExtension`](avaudiosessionportdescription/bluetoothmicrophoneextension.md) and query the extension’s [`highQualityRecording`](avaudiosessionportextensionbluetoothmicrophone/highqualityrecording.md) capability like shown below:

```swift
let audioSession = AVAudioSession.sharedInstance()
// Get the input port description for the current route.
guard let inputPort = audioSession.currentRoute.inputs.first else { return }
// Access the Bluetooth microphone extension, if it exists.
guard let micExtension = inputPort.bluetoothMicrophoneExtension else { return }
// Query the extension's high-quality recording capability.
if micExtension.highQualityRecording.isSupported {
    // The Bluetooth input supports high-quality recording.
}
```

Similarly, you can query the high-quality recording capability’s [`isEnabled`](avaudiosessioncapability/isenabled.md) property to determine whether this feature is in an enabled state for the active session.

If your app uses high-quality recording, consider setting [`setPrefersNoInterruptionsFromSystemAlerts(_:)`](avaudiosession/setprefersnointerruptionsfromsystemalerts(_:).md) while recording, to avoid the recording session being interrupted by an incoming call ringtone.

> **Note**: This option may increase input latency when enabled and isn’t recommended for real-time communication usage.

## See Also

- [static var allowAirPlay: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/allowairplay.md)
  An option that determines whether you can stream audio from this session to AirPlay devices.
- [static var allowBluetooth: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/allowbluetooth.md)
  An option that determines whether Bluetooth hands-free devices appear as available input routes.
- [static var allowBluetoothA2DP: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/allowbluetootha2dp.md)
  An option that determines whether you can stream audio from this session to Bluetooth devices that support the Advanced Audio Distribution Profile (A2DP).
- [static var allowBluetoothHFP: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/allowbluetoothhfp.md)
  An option that makes Bluetooth Hands-Free Profile (HFP) devices available for audio input.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/categoryoptions-swift.struct/bluetoothhighqualityrecording)*