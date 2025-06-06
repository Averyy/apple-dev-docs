# Advertisement Data Retrieval Keys

**Framework**: Core Bluetooth

Keys used to specify items in a dictionary of peripheral advertisement data.

## Topics

### Advertisement Keys
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
- [let CBAdvertisementDataSolicitedServiceUUIDsKey: String](cbadvertisementdatasolicitedserviceuuidskey.md)
  An array of solicited service UUIDs.

## See Also

- [func centralManager(CBCentralManager, didDiscover: CBPeripheral, advertisementData: [String : Any], rssi: NSNumber)](cbcentralmanagerdelegate/centralmanager(_:diddiscover:advertisementdata:rssi:).md)
  Tells the delegate the central manager discovered a peripheral while scanning for devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/advertisement-data-retrieval-keys)*