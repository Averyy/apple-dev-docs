# OBEXSessionEvent

**Framework**: IOBluetooth  
**Kind**: struct

**Availability**:
- macOS ?+

## Declaration

```swift
struct OBEXSessionEvent
```

#### Overview

When a new session event occurs, your selector (or C callback) will be given an OBEXSessionEvent pointer, and in it will be information you might find interesting so that you can then reply back appropriately. For example, of you receive a kOBEXSessionEventTypeConnectCommandResponseReceived event, you can then parse out the information related to that event, and if all looks well to you, you could them send a “Get” command to get a file off of the OBEX server you just connected to.

## Topics

### Initializers
- [init()](obexsessionevent/init.md)
- [init(type: OBEXSessionEventType, session: OBEXSessionRef!, refCon: UnsafeMutableRawPointer!, isEndOfEventData: DarwinBoolean, reserved1: UnsafeMutableRawPointer!, reserved2: UnsafeMutableRawPointer!, u: OBEXSessionEvent.__Unnamed_union_u)](obexsessionevent/init(type:session:refcon:isendofeventdata:reserved1:reserved2:u:).md)
### Instance Properties
- [var isEndOfEventData: DarwinBoolean](obexsessionevent/isendofeventdata.md)
- [var refCon: UnsafeMutableRawPointer!](obexsessionevent/refcon.md)
- [var reserved1: UnsafeMutableRawPointer!](obexsessionevent/reserved1.md)
- [var reserved2: UnsafeMutableRawPointer!](obexsessionevent/reserved2.md)
- [var session: OBEXSessionRef!](obexsessionevent/session.md)
- [var type: OBEXSessionEventType](obexsessionevent/type.md)
- [var u: OBEXSessionEvent.__Unnamed_union_u](obexsessionevent/u.md)

## See Also

- [struct OBEXAbortCommandData](obexabortcommanddata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXAbortCommandResponseData](obexabortcommandresponsedata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXConnectCommandData](obexconnectcommanddata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXConnectCommandResponseData](obexconnectcommandresponsedata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXDisconnectCommandData](obexdisconnectcommanddata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXDisconnectCommandResponseData](obexdisconnectcommandresponsedata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXErrorData](obexerrordata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXGetCommandData](obexgetcommanddata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXGetCommandResponseData](obexgetcommandresponsedata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXPutCommandData](obexputcommanddata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXPutCommandResponseData](obexputcommandresponsedata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXSetPathCommandData](obexsetpathcommanddata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXSetPathCommandResponseData](obexsetpathcommandresponsedata.md)
  Part of the OBEXSessionEvent structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsessionevent)*