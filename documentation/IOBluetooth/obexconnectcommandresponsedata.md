# OBEXConnectCommandResponseData

**Framework**: IOBluetooth  
**Kind**: struct

Part of the OBEXSessionEvent structure.

**Availability**:
- macOS ?+

## Declaration

```swift
struct OBEXConnectCommandResponseData
```

#### Overview

Is readable when the event is of type kOBEXSessionEventTypeConnectCommandResponseReceived (see OBEXSessionEventTypes).

## Topics

### Initializers
- [init()](obexconnectcommandresponsedata/init.md)
- [init(serverResponseOpCode: OBEXOpCode, headerDataPtr: UnsafeMutableRawPointer!, headerDataLength: Int, maxPacketSize: OBEXMaxPacketLength, version: OBEXVersion, flags: OBEXFlags)](obexconnectcommandresponsedata/init(serverresponseopcode:headerdataptr:headerdatalength:maxpacketsize:version:flags:).md)
### Instance Properties
- [var flags: OBEXFlags](obexconnectcommandresponsedata/flags.md)
- [var headerDataLength: Int](obexconnectcommandresponsedata/headerdatalength.md)
- [var headerDataPtr: UnsafeMutableRawPointer!](obexconnectcommandresponsedata/headerdataptr.md)
- [var maxPacketSize: OBEXMaxPacketLength](obexconnectcommandresponsedata/maxpacketsize.md)
- [var serverResponseOpCode: OBEXOpCode](obexconnectcommandresponsedata/serverresponseopcode.md)
- [var version: OBEXVersion](obexconnectcommandresponsedata/version.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexconnectcommandresponsedata)*