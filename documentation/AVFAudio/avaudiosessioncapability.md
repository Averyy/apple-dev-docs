# AVAudioSessionCapability

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

Describes whether a specific capability is supported and if that capability is currently enabled

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
class AVAudioSessionCapability
```

```objc
@interface AVAudioSessionCapability : NSObject
```

## Topics

### Inspecting a capability
- [var isEnabled: Bool](./avaudiosessioncapability/isenabled.md)
  A Boolean value that indicates whether the capability is enabled.
- [var isSupported: Bool](./avaudiosessioncapability/issupported.md)
  A Boolean value that indicates whether the capability is supported.

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
- [class AVAudioSessionPortExtensionBluetoothMicrophone](./avaudiosessionportextensionbluetoothmicrophone.md)
  An object that describes capabilities of Bluetooth microphone ports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessioncapability)*