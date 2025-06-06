# CBAdvertisementDataSolicitedServiceUUIDsKey

**Framework**: Core Bluetooth  
**Kind**: var

An array of solicited service UUIDs.

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
let CBAdvertisementDataSolicitedServiceUUIDsKey: String
```

#### Discussion

The value associated with this key is an array of one or more [`CBUUID`](cbuuid.md) objects, representing [`CBService`](cbservice.md) UUIDs.

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
- [let CBAdvertisementDataIsConnectable: String](cbadvertisementdataisconnectable.md)
  A Boolean value that indicates whether the advertising event type is connectable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdatasolicitedserviceuuidskey)*