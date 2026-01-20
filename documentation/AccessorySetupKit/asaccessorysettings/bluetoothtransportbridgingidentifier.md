# bluetoothTransportBridgingIdentifier

**Framework**: AccessorySetupKit  
**Kind**: property

A 6-byte identifier for bridging classic transport profiles.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var bluetoothTransportBridgingIdentifier: Data? { get set }
```

#### Discussion

AccessorySetupKit ignores this property if another app already authorized and bridged the accessory.

## See Also

- [var ssid: String?](asaccessorysettings/ssid.md)
  A hotspot identifier that clients can use to connect to an accessory’s hotspot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessorysettings/bluetoothtransportbridgingidentifier)*