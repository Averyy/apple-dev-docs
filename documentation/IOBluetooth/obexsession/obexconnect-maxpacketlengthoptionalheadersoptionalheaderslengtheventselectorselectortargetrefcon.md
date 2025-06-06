# obexConnect(_:maxPacketLength:optionalHeaders:optionalHeadersLength:eventSelector:selectorTarget:refCon:)

**Framework**: IOBluetooth  
**Kind**: method

Initiate an OBEX connection to a device. Causes underlying transport (Bluetooth, et al) to attempt to connect to a remote device. After success, an OBEX connect packet is sent to establish the OBEX Connection.

**Availability**:
- macOS ?+

## Declaration

```swift
func obexConnect(_ inFlags: OBEXFlags, maxPacketLength inMaxPacketLength: OBEXMaxPacketLength, optionalHeaders inOptionalHeaders: UnsafeMutableRawPointer!, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector!, selectorTarget inTarget: Any!, refCon inUserRefCon: UnsafeMutableRawPointer!) -> OBEXError
```

#### Discussion

A NULL selector or target will result in an error. After return, the data passed in will have been sent over the transport. You will receive a response to your command on your selector. If you have already established an OBEX connection and you call this again you will get an ‘kOBEXSessionAlreadyConnectedError’ as a result.

## Parameters

- `inFlags`: OBEX connect flags. See OBEX.h for possibilities.
- `inMaxPacketLength`: Maximum packet size you want to support. May be negotiated down, depending on target device.
- `inOptionalHeaders`: Can be NULL. Ptr to some data you want to send as your optional headers. Use the provided header contruction kit in OBEX.h and OBEXHeadersToBytes() for convenience.
- `inOptionalHeadersLength`: Length of data in ptr passed in above.
- `inSelector`: A VALID selector to be called when something interesting happens due to this call. Selector in your target object MUST have the following signature, or it will not be called properly (look for error messages in Console.app):
- `inTarget`: A VALID target object for the selector.
- `inUserRefCon`: Whatever you want to pass here. It will be passed back to you in the refCon portion of the OBEXSessionEvent struct. nil is, of course, OK here.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsession/obexconnect(_:maxpacketlength:optionalheaders:optionalheaderslength:eventselector:selectortarget:refcon:))*