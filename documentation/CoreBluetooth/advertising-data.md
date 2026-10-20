# Advertising Data

**Framework**: Core Bluetooth  
**Role**: API Collection

## Topics

### Advertising Keys
- [let CBAdvertisementDataIsConnectable: String](./cbadvertisementdataisconnectable.md)
  A Boolean value that indicates whether the advertising event type is connectable.
- [let CBAdvertisementDataLocalNameKey: String](./cbadvertisementdatalocalnamekey.md)
  The local name of a peripheral.
- [let CBAdvertisementDataManufacturerDataKey: String](./cbadvertisementdatamanufacturerdatakey.md)
  The manufacturer data of a peripheral.
- [let CBAdvertisementDataOverflowServiceUUIDsKey: String](./cbadvertisementdataoverflowserviceuuidskey.md)
  An array of UUIDs found in the overflow area of the advertisement data.
- [let CBAdvertisementDataServiceDataKey: String](./cbadvertisementdataservicedatakey.md)
  A dictionary that contains service-specific advertisement data.
- [let CBAdvertisementDataServiceUUIDsKey: String](./cbadvertisementdataserviceuuidskey.md)
  An array of service UUIDs.
- [let CBAdvertisementDataSolicitedServiceUUIDsKey: String](./cbadvertisementdatasolicitedserviceuuidskey.md)
  An array of solicited service UUIDs.
- [let CBAdvertisementDataTxPowerLevelKey: String](./cbadvertisementdatatxpowerlevelkey.md)
  The transmit power of a peripheral.

## See Also

### Managing Advertising
- [func startAdvertising([String : Any]?)](./cbperipheralmanager/startadvertising%28_%29.md)
  Advertises peripheral manager data.
- [func stopAdvertising()](./cbperipheralmanager/stopadvertising%28%29.md)
  Stops advertising peripheral manager data.
- [var isAdvertising: Bool](./cbperipheralmanager/isadvertising.md)
  A Boolean value that indicates whether the peripheral is advertising data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/advertising-data)*