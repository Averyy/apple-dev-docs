# OBEXPutCommandData

**Framework**: IOBluetooth  
**Kind**: struct  
**Role**: Structure

Part of the OBEXSessionEvent structure.

**Availability**:
- macOS

## Declaration

```swift
struct OBEXPutCommandData
```

```c
struct OBEXPutCommandData;
```

#### Overview

Is readable when the event is of type kOBEXSessionEventTypePutCommandReceived (see OBEXSessionEventTypes).

## Topics

### Initializers
- [init()](./obexputcommanddata/init%28%29.md)
- [init(headerDataPtr: UnsafeMutableRawPointer!, headerDataLength: Int, bodyDataLeftToSend: Int)](./obexputcommanddata/init%28headerdataptr,headerdatalength,bodydatalefttosend%29.md)
### Instance Properties
- [var bodyDataLeftToSend: Int](./obexputcommanddata/bodydatalefttosend.md)
- [var headerDataLength: Int](./obexputcommanddata/headerdatalength.md)
- [var headerDataPtr: UnsafeMutableRawPointer!](./obexputcommanddata/headerdataptr.md)

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
- [struct OBEXConnectCommandData](./obexconnectcommanddata.md)
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
- [struct OBEXPutCommandResponseData](./obexputcommandresponsedata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXSetPathCommandData](./obexsetpathcommanddata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXSetPathCommandResponseData](./obexsetpathcommandresponsedata.md)
  Part of the OBEXSessionEvent structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexputcommanddata)*