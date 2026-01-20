# ssid

**Framework**: AccessorySetupKit  
**Kind**: property

The accessory’s Wi-Fi SSID, if any.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var ssid: String? { get }
```

## Mentions

- [Discovering and configuring accessories](discovering-and-configuring-accessories.md)

#### Discussion

Use this identifier to establish a connection to the accessory.

## See Also

- [var bluetoothIdentifier: UUID?](asaccessory/bluetoothidentifier.md)
  The accessory’s unique Bluetooth identifier, if any.
- [var bluetoothTransportBridgingIdentifier: Data?](asaccessory/bluetoothtransportbridgingidentifier.md)
  The accessory’s Bluetooth identifier, if any, for use when bridging classic transport profiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessory/ssid)*