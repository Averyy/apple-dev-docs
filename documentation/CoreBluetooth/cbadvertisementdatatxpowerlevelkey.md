# CBAdvertisementDataTxPowerLevelKey

**Framework**: Core Bluetooth  
**Kind**: var

The transmit power of a peripheral.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
let CBAdvertisementDataTxPowerLevelKey: String
```

#### Discussion

The value associated with this key is an instance of [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber).

This key and value are available if the peripheral provides its transmitting power level in its advertising packet. You can calculate the path loss by comparing the RSSI value with the transmitting power level.

## See Also

- [let CBAdvertisementDataLocalNameKey: String](cbadvertisementdatalocalnamekey.md)
  The local name of a peripheral.
- [let CBAdvertisementDataManufacturerDataKey: String](cbadvertisementdatamanufacturerdatakey.md)
  The manufacturer data of a peripheral.
- [let CBAdvertisementDataServiceDataKey: String](cbadvertisementdataservicedatakey.md)
  A dictionary that contains service-specific advertisement data.
- [let CBAdvertisementDataServiceUUIDsKey: String](cbadvertisementdataserviceuuidskey.md)
  An array of service UUIDs.
- [let CBAdvertisementDataOverflowServiceUUIDsKey: String](cbadvertisementdataoverflowserviceuuidskey.md)
  An array of UUIDs found in the overflow area of the advertisement data.
- [let CBAdvertisementDataIsConnectable: String](cbadvertisementdataisconnectable.md)
  A Boolean value that indicates whether the advertising event type is connectable.
- [let CBAdvertisementDataSolicitedServiceUUIDsKey: String](cbadvertisementdatasolicitedserviceuuidskey.md)
  An array of solicited service UUIDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdatatxpowerlevelkey)*