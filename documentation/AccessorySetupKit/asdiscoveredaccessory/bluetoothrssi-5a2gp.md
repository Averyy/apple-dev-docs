# bluetoothRSSI

**Framework**: AccessorySetupKit  
**Kind**: property  
**Role**: Instance Property

The Bluetooth RSSI (Received Signal Strength Indicator) value from the discovered accessory.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+

## Declaration

```swift
var bluetoothRSSI: Int? { get }
```

## Discussion

This value represents the signal strength in dBm when the session discovered the accessory.

## See Also

### Working with accessory properties
- [var bluetoothAdvertisementData: [AnyHashable : Any]?](./bluetoothadvertisementdata.md)
  The Bluetooth advertisement data from the discovered accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asdiscoveredaccessory/bluetoothrssi-5a2gp)*