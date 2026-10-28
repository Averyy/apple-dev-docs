# bluetoothTransportBridging

**Framework**: AccessorySetupKit  
**Kind**: property  
**Role**: Type Property

The accessory supports bridging to Bluetooth classic transport.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
static var bluetoothTransportBridging: ASAccessory.SupportOptions { get }
```

```c
ASAccessorySupportBluetoothTransportBridging
```

## Discussion

This option indicates that when connecting with low energy transport, the accessory supports activating Bluetooth classic transport profiles.

## See Also

### Bluetooth options
- [static var bluetoothPairingLE: ASAccessory.SupportOptions](./bluetoothpairingle.md)
  The accessory supports Bluetooth Low Energy pairing.
- [static var bluetoothHID: ASAccessory.SupportOptions](./bluetoothhid.md)
  The accessory supports Bluetooth Low Energy HID service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessory/supportoptions/bluetoothtransportbridging)*