# getHandle(_:)

**Framework**: IOBluetooth  
**Kind**: method

Allows the discovery of the service record handle assigned to the service.

**Availability**:
- macOS ?+

## Declaration

```swift
func getHandle(_ outServiceRecordHandle: UnsafeMutablePointer<BluetoothSDPServiceRecordHandle>!) -> IOReturn
```

#### Return Value

Returns kIOReturnSuccess if the service record handle is found.

#### Discussion

This method will search through the attributes to find the one representing the service record handle. If one is found the outServiceRecordHandle param is set with the value. The outServiceRecordHandle value only gets set when kIOReturnSuccess is returned.

## Parameters

- `outServiceRecordHandle`: A pointer to the location that will get the found service record handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord/gethandle(_:))*