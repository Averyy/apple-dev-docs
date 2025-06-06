# OBEXAbortCommandData

**Framework**: IOBluetooth  
**Kind**: struct

Part of the OBEXSessionEvent structure.

**Availability**:
- macOS ?+

## Declaration

```swift
struct OBEXAbortCommandData
```

#### Overview

Is readable when the event is of type kOBEXSessionEventTypeAbortCommandReceived (see OBEXSessionEventTypes).

## Topics

### Initializers
- [init()](obexabortcommanddata/init.md)
- [init(headerDataPtr: UnsafeMutableRawPointer!, headerDataLength: Int)](obexabortcommanddata/init(headerdataptr:headerdatalength:).md)
### Instance Properties
- [var headerDataLength: Int](obexabortcommanddata/headerdatalength.md)
- [var headerDataPtr: UnsafeMutableRawPointer!](obexabortcommanddata/headerdataptr.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct OBEXSessionEvent](obexsessionevent.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexabortcommanddata)*