# bluetoothTransportBridgingIdentifier

**Framework**: AccessorySetupKit  
**Kind**: property  
**Role**: Instance Property

The accessory’s Bluetooth identifier, if any, for use when bridging classic transport profiles.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var bluetoothTransportBridgingIdentifier: Data? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSData * bluetoothTransportBridgingIdentifier;
```

## See Also

### Accessing identifiers
- [var bluetoothIdentifier: UUID?](./bluetoothidentifier.md)
  The accessory’s unique Bluetooth identifier, if any.
- [var ssid: String?](./ssid.md)
  The accessory’s Wi-Fi SSID, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessory/bluetoothtransportbridgingidentifier)*