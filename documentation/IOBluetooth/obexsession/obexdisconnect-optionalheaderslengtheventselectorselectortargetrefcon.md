# obexDisconnect(_:optionalHeadersLength:eventSelector:selectorTarget:refCon:)

**Framework**: IOBluetooth  
**Kind**: method

Send an OBEX Disconnect command to the session’s target. THIS DOES NOT necessarily close the underlying transport connection. Deleting the session will ensure that closure.

**Availability**:
- macOS ?+

## Declaration

```swift
func obexDisconnect(_ inOptionalHeaders: UnsafeMutableRawPointer!, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector!, selectorTarget inTarget: Any!, refCon inUserRefCon: UnsafeMutableRawPointer!) -> OBEXError
```

#### Discussion

A NULL selector or target will result in an error. After return, the data passed in will have been sent over the transport. You will receive a response to your command on your selector. Be careful not to exceed the max packet length in your optional headers, or your command will be rejected. It is recommended that you call getMaxPacketLength on your session before issuing this command so you know how much data the session’s target will accept in a single transaction.

## Parameters

- `inOptionalHeaders`: Can be NULL. Ptr to some data you want to send as your optional headers. Use the provided header contruction kit in OBEX.h and OBEXHeadersToBytes() for convenience.
- `inOptionalHeadersLength`: Length of data in ptr passed in above.
- `inSelector`: A VALID selector to be called when something interesting happens due to this call. Selector in your target object MUST have the following signature, or it will not be called properly (look for error messages in Console.app):
- `inTarget`: A VALID target object for the selector.
- `inUserRefCon`: Whatever you want to pass here. It will be passed back to you in the refCon portion of the OBEXSessionEvent struct. nil is, of course, OK here.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsession/obexdisconnect(_:optionalheaderslength:eventselector:selectortarget:refcon:))*