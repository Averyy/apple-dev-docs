# services

**Framework**: IOBluetooth  
**Kind**: property

Gets an array of service records for the device.

**Availability**:
- macOS ?+

## Declaration

```swift
var services: [Any]! { get }
```

#### Return Value

Returns an array of service records for the device if an SDP query has been performed. If no SDP query has been performed, nil is returned.

#### Discussion

The resulting array contains IOBluetoothSDPServiceRecord objects. The service records are only present if an SDP query has been done on the target object. This can be determined by calling -getLastServicesUpdate. It will return the last date/time of the SDP query. To initiate an SDP query on a device, use -performSDPQuery: as defined above.

Instead of allowing individual clients to query for different services and service attributes, the system request all of the device’s services and service attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/services)*