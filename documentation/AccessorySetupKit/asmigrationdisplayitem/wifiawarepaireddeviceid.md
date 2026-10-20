# wifiAwarePairedDeviceID

**Framework**: AccessorySetupKit  
**Kind**: property  
**Role**: Instance Property

The Wi-Fi Aware paired device identififer of the accessory to migrate.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+

## Declaration

```swift
var wifiAwarePairedDeviceID: ASAccessory.WiFiAwarePairedDeviceID { get set }
```

```objc
@property (nonatomic, assign, readwrite) ASAccessoryWiFiAwarePairedDeviceID wifiAwarePairedDeviceID;
```

## See Also

### Accessory identifiers
- [var peripheralIdentifier: UUID?](./peripheralidentifier.md)
  The Bluetooth identifier of the accessory to migrate.
- [var hotspotSSID: String?](./hotspotssid.md)
  The Wi-Fi hotspot SSID of the accessory to migrate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asmigrationdisplayitem/wifiawarepaireddeviceid)*