# MIDIBluetoothDriverDisconnect(_:)

**Framework**: Core MIDI  
**Kind**: func

Disconnect the Bluetooth MIDI driver from a Bluetooth Low Energy MIDI peripheral.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func MIDIBluetoothDriverDisconnect(_ uuid: CFString) -> OSStatus
```

#### Return Value

A status code that indicates the result of the disconnect.

#### Discussion

If a [`Core MIDI`](CoreMIDI.md) device is in a connected state to a Bluetooth Low Energy MIDI peripheral with the identifier you specify, the system disconnects it.

## Parameters

- `uuid`: A unique identifier that represents the peripheral to disconnect.

## See Also

- [func MIDIBluetoothDriverActivateAllConnections() -> OSStatus](midibluetoothdriveractivateallconnections().md)
  Promote all active Bluetooth connections into an online MIDI device capable of input and output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midibluetoothdriverdisconnect(_:))*