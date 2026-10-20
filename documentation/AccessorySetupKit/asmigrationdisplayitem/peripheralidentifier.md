# peripheralIdentifier

**Framework**: AccessorySetupKit  
**Kind**: property  
**Role**: Instance Property

The Bluetooth identifier of the accessory to migrate.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var peripheralIdentifier: UUID? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSUUID * peripheralIdentifier;
```

## Mentions

- [Discovering and configuring accessories](../discovering-and-configuring-accessories.md)

## See Also

### Accessory identifiers
- [var hotspotSSID: String?](./hotspotssid.md)
  The Wi-Fi hotspot SSID of the accessory to migrate.
- [var wifiAwarePairedDeviceID: ASAccessory.WiFiAwarePairedDeviceID](./wifiawarepaireddeviceid.md)
  The Wi-Fi Aware paired device identififer of the accessory to migrate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asmigrationdisplayitem/peripheralidentifier)*