# obexConnectResponse(_:flags:maxPacketLength:optionalHeaders:optionalHeadersLength:eventSelector:selectorTarget:refCon:)

**Framework**: IOBluetooth  
**Kind**: method

Send a connect response to a session’s target.

**Availability**:
- macOS ?+

## Declaration

```swift
func obexConnectResponse(_ inResponseOpCode: OBEXOpCode, flags inFlags: OBEXFlags, maxPacketLength inMaxPacketLength: OBEXMaxPacketLength, optionalHeaders inOptionalHeaders: UnsafeMutableRawPointer!, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector!, selectorTarget inTarget: Any!, refCon inUserRefCon: UnsafeMutableRawPointer!) -> OBEXError
```

#### Discussion

A NULL selector or target will result in an error. After return, the data passed in will have been sent over the underlying OBEX transport. You will receive any responses to your command response on your selector.

## Parameters

- `inResponseOpCode`: OBEX response constant. See OBEX.h for possibilities.
- `inFlags`: OBEX connect flags. See OBEX.h for possibilities.
- `inMaxPacketLength`: Maximum packet size you want your OBEX session to communicate with. This MUST be lower than the max packet size the client has reported to you in the connect command you received from it.
- `inOptionalHeaders`: Can be NULL. Ptr to some data you want to send as your optional headers. Use the provided header contruction kit in OBEX.h and OBEXHeadersToBytes() for convenience.
- `inOptionalHeadersLength`: Length of data in ptr passed in above.
- `inSelector`: A VALID selector to be called when something interesting happens due to this call. Selector in your target object MUST have the following signature, or it will not be called properly (look for error messages in Console.app):
- `inTarget`: A VALID target object for the selector.
- `inUserRefCon`: Whatever you want to pass here. It will be passed back to you in the refCon portion of the OBEXSessionEvent struct. nil is, of course, OK here.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsession/obexconnectresponse(_:flags:maxpacketlength:optionalheaders:optionalheaderslength:eventselector:selectortarget:refcon:))*