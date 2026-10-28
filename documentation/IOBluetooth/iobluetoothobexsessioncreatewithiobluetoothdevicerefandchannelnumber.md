# IOBluetoothOBEXSessionCreateWithIOBluetoothDeviceRefAndChannelNumber

**Framework**: IOBluetooth  
**Kind**: func  
**Role**: Function

Create an OBEX session with a device ref and an RFCOMM channel ID. This allows you to bypass the browser if you already know the SDP information.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
OBEXError IOBluetoothOBEXSessionCreateWithIOBluetoothDeviceRefAndChannelNumber(IOBluetoothDeviceRef inDeviceRef, BluetoothRFCOMMChannelID inChannelID, OBEXSessionRef*outSessionRef);
```

## Return Value

An error code value. 0 if successful.

## Discussion

You will use a session reference to do all OBEX interaction to a specific device. This method DOES NOT create a connection to the device of any kind.

*** DEPRECATED IN BLUETOOTH 2.2 (OS X 10.6) *** You should transition your code to Objective-C equivalents. *** This API may be removed any time in the future.

## Parameters

- `inDeviceRef`: A valid IOBluetoothDeviceRef reference.
- `inChannelID`: A valid RFCOMM channel ID on the target device.
- `outSessionRef`: A valid ptr to an IOBluetoothOBEXSessionRef; will contain the newly created session if return value is kOBEXSuccess.

## See Also

### Miscellaneous
- [IOBluetoothOBEXSessionCreateWithIncomingIOBluetoothRFCOMMChannel](./iobluetoothobexsessioncreatewithincomingiobluetoothrfcommchannel.md)
  Create an OBEX session with an IOBluetoothRFCOMMchannel. This implies you are creating a OBEX SERVER session that will dole out info to remote Bluetooth clients.
- [IOBluetoothOBEXSessionCreateWithIOBluetoothSDPServiceRecordRef](./iobluetoothobexsessioncreatewithiobluetoothsdpservicerecordref.md)
  Create an OBEX session with a service ref, usually obtained from the device browser.
- [IOBluetoothOBEXSessionOpenTransportConnection](./iobluetoothobexsessionopentransportconnection.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsessioncreatewithiobluetoothdevicerefandchannelnumber)*