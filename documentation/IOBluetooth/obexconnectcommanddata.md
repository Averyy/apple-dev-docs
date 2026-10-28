# OBEXConnectCommandData

**Framework**: IOBluetooth  
**Kind**: struct  
**Role**: Structure

Part of the OBEXSessionEvent structure.

**Availability**:
- macOS

## Declaration

```swift
struct OBEXConnectCommandData
```

```c
struct OBEXConnectCommandData;
```

## Overview

Is readable when the event is of type kOBEXSessionEventTypeConnectCommandReceived (see OBEXSessionEventTypes).

## Topics

### Initializers
- [init()](./obexconnectcommanddata/init%28%29.md)
- [init(headerDataPtr: UnsafeMutableRawPointer!, headerDataLength: Int, maxPacketSize: OBEXMaxPacketLength, version: OBEXVersion, flags: OBEXFlags)](./obexconnectcommanddata/init%28headerdataptr,headerdatalength,maxpacketsize,version,flags%29.md)
### Instance Properties
- [var flags: OBEXFlags](./obexconnectcommanddata/flags.md)
- [var headerDataLength: Int](./obexconnectcommanddata/headerdatalength.md)
- [var headerDataPtr: UnsafeMutableRawPointer!](./obexconnectcommanddata/headerdataptr.md)
- [var maxPacketSize: OBEXMaxPacketLength](./obexconnectcommanddata/maxpacketsize.md)
- [var version: OBEXVersion](./obexconnectcommanddata/version.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Data Types
- [struct OBEXSessionEvent](./obexsessionevent.md)
- [struct OBEXAbortCommandData](./obexabortcommanddata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXAbortCommandResponseData](./obexabortcommandresponsedata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXConnectCommandResponseData](./obexconnectcommandresponsedata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXDisconnectCommandData](./obexdisconnectcommanddata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXDisconnectCommandResponseData](./obexdisconnectcommandresponsedata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXErrorData](./obexerrordata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXGetCommandData](./obexgetcommanddata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXGetCommandResponseData](./obexgetcommandresponsedata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXPutCommandData](./obexputcommanddata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXPutCommandResponseData](./obexputcommandresponsedata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXSetPathCommandData](./obexsetpathcommanddata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXSetPathCommandResponseData](./obexsetpathcommandresponsedata.md)
  Part of the OBEXSessionEvent structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexconnectcommanddata)*