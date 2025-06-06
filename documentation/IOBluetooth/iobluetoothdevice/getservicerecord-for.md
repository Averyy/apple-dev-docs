# getServiceRecord(for:)

**Framework**: IOBluetooth  
**Kind**: method

Search for a service record containing the given UUID.

**Availability**:
- macOS ?+

## Declaration

```swift
func getServiceRecord(for sdpUUID: IOBluetoothSDPUUID!) -> IOBluetoothSDPServiceRecord!
```

#### Return Value

Returns the first service record that contains the given uuid. If no service record is found, nil is returned.

#### Discussion

This method searches through the device’s services to find a service that contains the given UUID. Only the first service record will be returned. This method only operates on services that have already been queried. It will not initiate a new query. This method should probably be updated to return an array of service records if more than one contains the UUID.

## Parameters

- `sdpUUID`: UUID value to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/getservicerecord(for:))*