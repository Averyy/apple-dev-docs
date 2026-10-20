# bluetoothMicrophoneExtension

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

An optional port extension that describes capabilities relevant to Bluetooth microphone ports.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var bluetoothMicrophoneExtension: AVAudioSessionPortExtensionBluetoothMicrophone? { get }
```

```objc
@property (nonatomic, readonly, nullable) AVAudioSessionPortExtensionBluetoothMicrophone * bluetoothMicrophoneExtension;
```

#### Discussion

This property is optional and will be `nil` for all ports for which this capability set doesn’t apply.

## See Also

### Accessing the port extension
- [class AVAudioSessionPortExtensionBluetoothMicrophone](../avaudiosessionportextensionbluetoothmicrophone.md)
  An object that describes capabilities of Bluetooth microphone ports.
- [class AVAudioSessionCapability](../avaudiosessioncapability.md)
  Describes whether a specific capability is supported and if that capability is currently enabled


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionportdescription/bluetoothmicrophoneextension)*