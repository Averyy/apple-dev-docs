# bluetoothMicrophoneExtension

**Framework**: AVFAudio  
**Kind**: property

An optional port extension that describes capabilities relevant to Bluetooth microphone ports.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var bluetoothMicrophoneExtension: AVAudioSessionPortExtensionBluetoothMicrophone? { get }
```

#### Discussion

This property is optional and will be `nil` for all ports for which this capability set doesn’t apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionportdescription/bluetoothmicrophoneextension)*