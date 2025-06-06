# obexGet(_:headers:headersLength:eventSelector:selectorTarget:refCon:)

**Framework**: IOBluetooth  
**Kind**: method

Send an OBEX Get command to the session’s target.

**Availability**:
- macOS ?+

## Declaration

```swift
func obexGet(_ isFinalChunk: Bool, headers inHeaders: UnsafeMutableRawPointer!, headersLength inHeadersLength: Int, eventSelector inSelector: Selector!, selectorTarget inTarget: Any!, refCon inUserRefCon: UnsafeMutableRawPointer!) -> OBEXError
```

#### Discussion

A NULL selector or target will result in an error. After return, the data passed in will have been sent over the transport. You will receive a response to your command on your selector.

## Parameters

- `isFinalChunk`: Specify if this request is complete in one shot - that all the headers you are supplying will fit in the negotiated max packet length.
- `inHeaders`: Can be NULL. Ptr to some data you want to send as your headers, such as Length, Name, etc. Use the provided header contruction kit in OBEX.h and OBEXHeadersToBytes() for your convenience.
- `inHeadersLength`: Length of data in ptr passed in above.
- `inSelector`: A VALID selector to be called when something interesting happens due to this call. Selector in your target object MUST have the following signature, or it will not be called properly (look for error messages in Console.app):
- `inTarget`: A VALID target object for the selector.
- `inUserRefCon`: Whatever you want to pass here. It will be passed back to you in the refCon portion of the OBEXSessionEvent struct. nil is, of course, OK here.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsession/obexget(_:headers:headerslength:eventselector:selectortarget:refcon:))*