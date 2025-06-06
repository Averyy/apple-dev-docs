# CBAdvertisementDataOverflowServiceUUIDsKey

**Framework**: Core Bluetooth  
**Kind**: var

An array of UUIDs found in the overflow area of the advertisement data.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let CBAdvertisementDataOverflowServiceUUIDsKey: String
```

#### Discussion

The value associated with this key is an array of one or more [`CBUUID`](cbuuid.md) objects, representing [`CBService`](cbservice.md) UUIDs.

Because data stored in this area results from not fitting in the main advertisement, UUIDs listed here are “best effort” and may not always be accurate. For details about the overflow area of advertisement data, see the [`startAdvertising(_:)`](cbperipheralmanager/startadvertising(_:).md) method in [`CBPeripheralManager`](cbperipheralmanager.md).

## See Also

- [let CBAdvertisementDataLocalNameKey: String](cbadvertisementdatalocalnamekey.md)
  The local name of a peripheral.
- [let CBAdvertisementDataManufacturerDataKey: String](cbadvertisementdatamanufacturerdatakey.md)
  The manufacturer data of a peripheral.
- [let CBAdvertisementDataServiceDataKey: String](cbadvertisementdataservicedatakey.md)
  A dictionary that contains service-specific advertisement data.
- [let CBAdvertisementDataServiceUUIDsKey: String](cbadvertisementdataserviceuuidskey.md)
  An array of service UUIDs.
- [let CBAdvertisementDataTxPowerLevelKey: String](cbadvertisementdatatxpowerlevelkey.md)
  The transmit power of a peripheral.
- [let CBAdvertisementDataIsConnectable: String](cbadvertisementdataisconnectable.md)
  A Boolean value that indicates whether the advertising event type is connectable.
- [let CBAdvertisementDataSolicitedServiceUUIDsKey: String](cbadvertisementdatasolicitedserviceuuidskey.md)
  An array of solicited service UUIDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdataoverflowserviceuuidskey)*