# IOBluetoothNSStringFromDeviceAddressColon(_:)

**Framework**: IOBluetooth  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS

## Declaration

```swift
func IOBluetoothNSStringFromDeviceAddressColon(_ deviceAddress: UnsafePointer<BluetoothDeviceAddress>!) -> String!
```

```c
extern NSString *IOBluetoothNSStringFromDeviceAddressColon(const BluetoothDeviceAddress *deviceAddress);
```

## See Also

### Functions
- [func IOBluetoothPackDataList(UnsafeMutableRawPointer!, UnsafePointer<CChar>!, CVaListPointer) -> Int](./iobluetoothpackdatalist%28_,_,_%29.md)
- [func IOBluetoothUnpackDataList(Int, UnsafeRawPointer!, UnsafePointer<CChar>!, CVaListPointer) -> Int](./iobluetoothunpackdatalist%28_,_,_,_%29.md)
- [OBEXSessionGetAvailableCommandPayloadLength](./obexsessiongetavailablecommandpayloadlength.md)
  Gets space available for your data for a particular command response you are trying to send.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothnsstringfromdeviceaddresscolon(_:))*