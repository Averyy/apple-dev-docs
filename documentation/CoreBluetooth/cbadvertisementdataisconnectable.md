# CBAdvertisementDataIsConnectable

**Framework**: Core Bluetooth  
**Kind**: var

A Boolean value that indicates whether the advertising event type is connectable.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let CBAdvertisementDataIsConnectable: String
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object. You can use this value to determine whether your app can currently connect to a peripheral.

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
- [let CBAdvertisementDataTxPowerLevelKey: String](cbadvertisementdatatxpowerlevelkey.md)
  The transmit power of a peripheral.
- [let CBAdvertisementDataSolicitedServiceUUIDsKey: String](cbadvertisementdatasolicitedserviceuuidskey.md)
  An array of solicited service UUIDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdataisconnectable)*