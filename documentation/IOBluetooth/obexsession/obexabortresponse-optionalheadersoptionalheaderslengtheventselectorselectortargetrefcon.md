# obexAbortResponse(_:optionalHeaders:optionalHeadersLength:eventSelector:selectorTarget:refCon:)

**Framework**: IOBluetooth  
**Kind**: method

Send an abort response to a session’s target.

**Availability**:
- macOS ?+

## Declaration

```swift
func obexAbortResponse(_ inResponseOpCode: OBEXOpCode, optionalHeaders inOptionalHeaders: UnsafeMutableRawPointer!, optionalHeadersLength inOptionalHeadersLength: Int, eventSelector inSelector: Selector!, selectorTarget inTarget: Any!, refCon inUserRefCon: UnsafeMutableRawPointer!) -> OBEXError
```

#### Discussion

A NULL selector or target will result in an error. After return, the data passed in will have been sent over the underlying OBEX transport. You will receive any responses to your command response on your selector.

## Parameters

- `inOptionalHeaders`: Can be NULL. Ptr to some data you want to send as your optional headers. Use the provided header contruction kit in OBEX.h and OBEXHeadersToBytes() for convenience.
- `inOptionalHeadersLength`: Length of data in ptr passed in above.
- `inSelector`: 
- `inTarget`: A VALID target object for the selector.
- `inUserRefCon`: Whatever you want to pass here. It will be passed back to you in the refCon portion of the OBEXSessionEvent struct. nil is, of course, OK here.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsession/obexabortresponse(_:optionalheaders:optionalheaderslength:eventselector:selectortarget:refcon:))*