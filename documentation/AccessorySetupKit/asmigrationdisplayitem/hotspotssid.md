# hotspotSSID

**Framework**: AccessorySetupKit  
**Kind**: property  
**Role**: Instance Property

The Wi-Fi hotspot SSID of the accessory to migrate.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var hotspotSSID: String? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSString * hotspotSSID;
```

## Mentions

- [Discovering and configuring accessories](../discovering-and-configuring-accessories.md)

## See Also

### Accessory identifiers
- [var peripheralIdentifier: UUID?](./peripheralidentifier.md)
  The Bluetooth identifier of the accessory to migrate.
- [var wifiAwarePairedDeviceID: ASAccessory.WiFiAwarePairedDeviceID](./wifiawarepaireddeviceid.md)
  The Wi-Fi Aware paired device identififer of the accessory to migrate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asmigrationdisplayitem/hotspotssid)*