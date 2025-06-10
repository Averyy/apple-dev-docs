# bluetoothHighQualityRecording

**Framework**: AVFAudio  
**Kind**: property

When this option is specified with a category that supports both input and output, the session will enable full-bandwidth audio in both input & output directions, if the Bluetooth route supports it (e.g. certain AirPods models). It is currently compatible only with mode [`default`](avaudiosession/mode-swift.struct/default.md).

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
static var bluetoothHighQualityRecording: AVAudioSession.CategoryOptions { get }
```

#### Discussion

- Support for this can be queried on input ports via the BluetoothMicrophone interface on a port, via its member `highQualityRecording.isSupported`.
- Active sessions can see if full-bandwidth Bluetooth audio was successfully enabled by querying the BluetoothMicrophone interface of the input port of the current route for: `highQualityRecording.isEnabled`.
- When this option is provided alone, it will be enabled if the route supports it, otherwise the option will be ignored. This option may be combined with `AVAudioSessionCategoryOptionAllowBluetoothHFP`, in which case HFP will be used as a fallback if the route does not support this `AVAudioSessionCategoryOptionBluetoothHighQualityRecording` option.
- Note This option may increase input latency when enabled and is therefore not recommended for real-time communication usage.
- Note Apps using `AVAudioSessionCategoryOptionBluetoothHighQualityRecording` may want to consider setting [`setPrefersNoInterruptionsFromSystemAlerts(_:)`](avaudiosession/setprefersnointerruptionsfromsystemalerts(_:).md) while recording, to avoid the recording session being interrupted by an incoming call ringtone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/categoryoptions-swift.struct/bluetoothhighqualityrecording)*