# ssid

**Framework**: AccessorySetupKit  
**Kind**: property  
**Role**: Instance Property

The accessory’s Wi-Fi SSID, if any.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var ssid: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * SSID;
```

## Mentions

- [Discovering and configuring accessories](../discovering-and-configuring-accessories.md)

## Discussion

Use this identifier to establish a connection to the accessory.

## See Also

### Accessing identifiers
- [var bluetoothIdentifier: UUID?](./bluetoothidentifier.md)
  The accessory’s unique Bluetooth identifier, if any.
- [var bluetoothTransportBridgingIdentifier: Data?](./bluetoothtransportbridgingidentifier.md)
  The accessory’s Bluetooth identifier, if any, for use when bridging classic transport profiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessory/ssid)*