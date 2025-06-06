# CBAdvertisementDataServiceDataKey

**Framework**: Core Bluetooth  
**Kind**: var

A dictionary that contains service-specific advertisement data.

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
let CBAdvertisementDataServiceDataKey: String
```

#### Discussion

The keys ([`CBUUID`](cbuuid.md) objects) represent CBService UUIDs, and the values ([`NSData`](https://developer.apple.com/documentation/Foundation/NSData) objects) represent service-specific data.

## See Also

- [let CBAdvertisementDataLocalNameKey: String](cbadvertisementdatalocalnamekey.md)
  The local name of a peripheral.
- [let CBAdvertisementDataManufacturerDataKey: String](cbadvertisementdatamanufacturerdatakey.md)
  The manufacturer data of a peripheral.
- [let CBAdvertisementDataServiceUUIDsKey: String](cbadvertisementdataserviceuuidskey.md)
  An array of service UUIDs.
- [let CBAdvertisementDataOverflowServiceUUIDsKey: String](cbadvertisementdataoverflowserviceuuidskey.md)
  An array of UUIDs found in the overflow area of the advertisement data.
- [let CBAdvertisementDataTxPowerLevelKey: String](cbadvertisementdatatxpowerlevelkey.md)
  The transmit power of a peripheral.
- [let CBAdvertisementDataIsConnectable: String](cbadvertisementdataisconnectable.md)
  A Boolean value that indicates whether the advertising event type is connectable.
- [let CBAdvertisementDataSolicitedServiceUUIDsKey: String](cbadvertisementdatasolicitedserviceuuidskey.md)
  An array of solicited service UUIDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdataservicedatakey)*