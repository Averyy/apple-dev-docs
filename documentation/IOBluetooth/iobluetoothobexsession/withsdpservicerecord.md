# withSDPServiceRecord(_:)

**Framework**: IOBluetooth  
**Kind**: method

Creates a Bluetooth-based OBEX Session using an SDP service record, typically obtained from a device/service browser window controller.

**Availability**:
- macOS ?+

## Declaration

```swift
class func withSDPServiceRecord(_ inSDPServiceRecord: IOBluetoothSDPServiceRecord!) -> Self!
```

#### Return Value

An OBEX session representing the device/rfcomm channel found in the service record. nil if we failed.

#### Discussion

Note that this does NOT mean the transport connection was open. It will be opened when OBEXConnect is invoked on the session object.

 In Bluetooth framework version 1.0.0, the session returned will NOT be autoreleased as it should be according to objc convention. This has been changed starting in Bluetooth version 1.0.1 and later, so it WILL be autoreleased upon return, so you will need to retain it if you want to reference it later.

## Parameters

- `inSDPServiceRecord`: A valid SDP service record describing the service (and RFCOMM channel) you want to connect to with Bluetooth/OBEX.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsession/withsdpservicerecord(_:))*