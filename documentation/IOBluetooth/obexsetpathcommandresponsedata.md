# OBEXSetPathCommandResponseData

**Framework**: IOBluetooth  
**Kind**: struct

Part of the OBEXSessionEvent structure.

**Availability**:
- macOS ?+

## Declaration

```swift
struct OBEXSetPathCommandResponseData
```

#### Overview

Is readable when the event is of type kOBEXSessionEventTypeSetPathCommandResponseReceived (see OBEXSessionEventTypes).

## Topics

### Initializers
- [init()](obexsetpathcommandresponsedata/init.md)
- [init(serverResponseOpCode: OBEXOpCode, headerDataPtr: UnsafeMutableRawPointer!, headerDataLength: Int, flags: OBEXFlags, constants: OBEXConstants)](obexsetpathcommandresponsedata/init(serverresponseopcode:headerdataptr:headerdatalength:flags:constants:).md)
### Instance Properties
- [var constants: OBEXConstants](obexsetpathcommandresponsedata/constants.md)
- [var flags: OBEXFlags](obexsetpathcommandresponsedata/flags.md)
- [var headerDataLength: Int](obexsetpathcommandresponsedata/headerdatalength.md)
- [var headerDataPtr: UnsafeMutableRawPointer!](obexsetpathcommandresponsedata/headerdataptr.md)
- [var serverResponseOpCode: OBEXOpCode](obexsetpathcommandresponsedata/serverresponseopcode.md)

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
- [struct OBEXPutCommandResponseData](obexputcommandresponsedata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXSetPathCommandData](obexsetpathcommanddata.md)
  Part of the OBEXSessionEvent structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsetpathcommandresponsedata)*