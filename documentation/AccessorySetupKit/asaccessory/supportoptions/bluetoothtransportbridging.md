# bluetoothTransportBridging

**Framework**: AccessorySetupKit  
**Kind**: property

The accessory supports bridging to Bluetooth classic transport.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
static var bluetoothTransportBridging: ASAccessory.SupportOptions { get }
```

#### Discussion

This option indicates that when connecting with low energy transport, the accessory supports activating Bluetooth classic transport profiles.

## See Also

- [static var bluetoothPairingLE: ASAccessory.SupportOptions](asaccessory/supportoptions/bluetoothpairingle.md)
  The accessory supports Bluetooth Low Energy pairing.
- [static var bluetoothHID: ASAccessory.SupportOptions](asaccessory/supportoptions/bluetoothhid.md)
  The accessory supports Bluetooth Low Energy HID service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessory/supportoptions/bluetoothtransportbridging)*