# OBEXSetPathCommandData

**Framework**: IOBluetooth  
**Kind**: struct

Part of the OBEXSessionEvent structure.

**Availability**:
- macOS ?+

## Declaration

```swift
struct OBEXSetPathCommandData
```

#### Overview

Is readable when the event is of type kOBEXSessionEventTypeSetPathCommandReceived (see OBEXSessionEventTypes).

## Topics

### Initializers
- [init()](obexsetpathcommanddata/init.md)
- [init(headerDataPtr: UnsafeMutableRawPointer!, headerDataLength: Int, flags: OBEXFlags, constants: OBEXConstants)](obexsetpathcommanddata/init(headerdataptr:headerdatalength:flags:constants:).md)
### Instance Properties
- [var constants: OBEXConstants](obexsetpathcommanddata/constants.md)
- [var flags: OBEXFlags](obexsetpathcommanddata/flags.md)
- [var headerDataLength: Int](obexsetpathcommanddata/headerdatalength.md)
- [var headerDataPtr: UnsafeMutableRawPointer!](obexsetpathcommanddata/headerdataptr.md)

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
- [struct OBEXSetPathCommandResponseData](obexsetpathcommandresponsedata.md)
  Part of the OBEXSessionEvent structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsetpathcommanddata)*