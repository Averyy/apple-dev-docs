# AVAudioSessionPortExtensionBluetoothMicrophone

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

An object that describes capabilities of Bluetooth microphone ports.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
class AVAudioSessionPortExtensionBluetoothMicrophone
```

```objc
@interface AVAudioSessionPortExtensionBluetoothMicrophone : NSObject
```

## Topics

### Inspecting the port extension
- [var farFieldCapture: AVAudioSessionCapability](./avaudiosessionportextensionbluetoothmicrophone/farfieldcapture.md)
  Describes whether this port supports far-field input capture.
- [var highQualityRecording: AVAudioSessionCapability](./avaudiosessionportextensionbluetoothmicrophone/highqualityrecording.md)
  Describes whether this port supports Bluetooth high-quality recording.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing the port extension
- [var bluetoothMicrophoneExtension: AVAudioSessionPortExtensionBluetoothMicrophone?](./avaudiosessionportdescription/bluetoothmicrophoneextension.md)
  An optional port extension that describes capabilities relevant to Bluetooth microphone ports.
- [class AVAudioSessionCapability](./avaudiosessioncapability.md)
  Describes whether a specific capability is supported and if that capability is currently enabled


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionportextensionbluetoothmicrophone)*