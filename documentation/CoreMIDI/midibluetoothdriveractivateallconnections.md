# MIDIBluetoothDriverActivateAllConnections()

**Framework**: Core MIDI  
**Kind**: func

Promote all active Bluetooth connections into an online MIDI device capable of input and output.

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
func MIDIBluetoothDriverActivateAllConnections() -> OSStatus
```

#### Return Value

A status code that indicates the result of the activation.

#### Discussion

To establish a Bluetooth MIDI driver connection to a Bluetooth Low Energy (BLE) MIDI peripheral, perform the following steps:

1. Scan for the peripheral’s advertised BLE MIDI service by using [`Core Bluetooth`](https://developer.apple.com/documentation/CoreBluetooth).
2. Connect to the advertised peripheral by using [`Core Bluetooth`](https://developer.apple.com/documentation/CoreBluetooth).
3. Call [`MIDIBluetoothDriverActivateAllConnections()`](midibluetoothdriveractivateallconnections().md) upon successful connection.
4. Confirm the peripheral’s registration by using [`Core MIDI`](CoreMIDI.md) and inspecting [`MIDIDeviceRef`](midideviceref.md).

If the device reference is present, [`Core MIDI`](CoreMIDI.md) owns a connection to the peripheral, so use [`Core Bluetooth`](https://developer.apple.com/documentation/CoreBluetooth) to disconnect from the peripheral.

## See Also

- [func MIDIBluetoothDriverDisconnect(CFString) -> OSStatus](midibluetoothdriverdisconnect(_:).md)
  Disconnect the Bluetooth MIDI driver from a Bluetooth Low Energy MIDI peripheral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midibluetoothdriveractivateallconnections())*