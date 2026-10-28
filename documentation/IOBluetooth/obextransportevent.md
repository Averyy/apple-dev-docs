# OBEXTransportEvent

**Framework**: IOBluetooth  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS

## Declaration

```swift
struct OBEXTransportEvent
```

```c
struct OBEXTransportEvent;
```

## Overview

You will need to construcy these when data is received, and then pass a pointer to it to one of the incoming data methods defined below. Pass 0 as your status if data was received OK. Otherwise, you can put your own error code in there. For the transport type, be sure to use one of the defined types above.

## Topics

### Initializers
- [init()](./obextransportevent/init%28%29.md)
- [init(type: OBEXTransportEventType, status: OBEXError, dataPtr: UnsafeMutableRawPointer!, dataLength: Int)](./obextransportevent/init%28type,status,dataptr,datalength%29.md)
### Instance Properties
- [var dataLength: Int](./obextransportevent/datalength.md)
- [var dataPtr: UnsafeMutableRawPointer!](./obextransportevent/dataptr.md)
- [var status: OBEXError](./obextransportevent/status.md)
- [var type: OBEXTransportEventType](./obextransportevent/type.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### DataTypes
- [typealias OBEXTransportEventType](./obextransporteventtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obextransportevent)*