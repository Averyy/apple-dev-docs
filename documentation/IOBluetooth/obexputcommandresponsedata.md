# OBEXPutCommandResponseData

**Framework**: IOBluetooth  
**Kind**: struct

Part of the OBEXSessionEvent structure.

**Availability**:
- macOS ?+

## Declaration

```swift
struct OBEXPutCommandResponseData
```

#### Overview

Is readable when the event is of type kOBEXSessionEventTypePutCommandResponseReceived (see OBEXSessionEventTypes).

## Topics

### Initializers
- [init()](obexputcommandresponsedata/init.md)
- [init(serverResponseOpCode: OBEXOpCode, headerDataPtr: UnsafeMutableRawPointer!, headerDataLength: Int)](obexputcommandresponsedata/init(serverresponseopcode:headerdataptr:headerdatalength:).md)
### Instance Properties
- [var headerDataLength: Int](obexputcommandresponsedata/headerdatalength.md)
- [var headerDataPtr: UnsafeMutableRawPointer!](obexputcommandresponsedata/headerdataptr.md)
- [var serverResponseOpCode: OBEXOpCode](obexputcommandresponsedata/serverresponseopcode.md)

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
- [struct OBEXSetPathCommandData](obexsetpathcommanddata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXSetPathCommandResponseData](obexsetpathcommandresponsedata.md)
  Part of the OBEXSessionEvent structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexputcommandresponsedata)*