# IOBluetoothOBEXSessionCreateWithIncomingIOBluetoothRFCOMMChannel

**Framework**: IOBluetooth  
**Kind**: func  
**Role**: Function

Create an OBEX session with an IOBluetoothRFCOMMchannel. This implies you are creating a OBEX SERVER session that will dole out info to remote Bluetooth clients.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
OBEXError IOBluetoothOBEXSessionCreateWithIncomingIOBluetoothRFCOMMChannel(IOBluetoothRFCOMMChannelRef inRFCOMMChannelRef, OBEXSessionEventCallback inCallback, void *inUserRefCon, OBEXSessionRef*outSessionRef);
```

#### Return Value

An error code value. 0 if successful.

#### Discussion

This assumes that the RFCOMM channel you have passed it is already open and ready to transmit data to the session.

*** DEPRECATED IN BLUETOOTH 2.2 (OS X 10.6) *** You should transition your code to Objective-C equivalents. *** This API may be removed any time in the future.

## Parameters

- `inRFCOMMChannelRef`: A valid IOBluetoothRFCOMMChannel reference.
- `inCallback`: A callback for Get requests sent to your session by a remote device. Must be a valid function ptr, otherwise why even call this?
- `outSessionRef`: A valid ptr to an IOBluetoothOBEXSessionRef; will contain the newly created session if return value is kOBEXSuccess.

## See Also

### Miscellaneous
- [IOBluetoothOBEXSessionCreateWithIOBluetoothDeviceRefAndChannelNumber](./iobluetoothobexsessioncreatewithiobluetoothdevicerefandchannelnumber.md)
  Create an OBEX session with a device ref and an RFCOMM channel ID. This allows you to bypass the browser if you already know the SDP information.
- [IOBluetoothOBEXSessionCreateWithIOBluetoothSDPServiceRecordRef](./iobluetoothobexsessioncreatewithiobluetoothsdpservicerecordref.md)
  Create an OBEX session with a service ref, usually obtained from the device browser.
- [IOBluetoothOBEXSessionOpenTransportConnection](./iobluetoothobexsessionopentransportconnection.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsessioncreatewithincomingiobluetoothrfcommchannel)*