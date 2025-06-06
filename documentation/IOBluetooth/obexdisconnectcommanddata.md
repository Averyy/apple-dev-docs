# OBEXDisconnectCommandData

**Framework**: IOBluetooth  
**Kind**: struct

Part of the OBEXSessionEvent structure.

**Availability**:
- macOS ?+

## Declaration

```swift
struct OBEXDisconnectCommandData
```

#### Overview

Is readable when the event is of type kOBEXSessionEventTypeDisconnectCommandReceived (see OBEXSessionEventTypes).

## Topics

### Initializers
- [init()](obexdisconnectcommanddata/init.md)
- [init(headerDataPtr: UnsafeMutableRawPointer!, headerDataLength: Int)](obexdisconnectcommanddata/init(headerdataptr:headerdatalength:).md)
### Instance Properties
- [var headerDataLength: Int](obexdisconnectcommanddata/headerdatalength.md)
- [var headerDataPtr: UnsafeMutableRawPointer!](obexdisconnectcommanddata/headerdataptr.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct OBEXSessionEvent](obexsessionevent.md)
- [struct OBEXAbortCommandData](obexabortcommanddata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXAbortCommandResponseData](obexabortcommandresponsedata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXConnectCommandData](obexconnectcommanddata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXConnectCommandResponseData](obexconnectcommandresponsedata.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexdisconnectcommanddata)*