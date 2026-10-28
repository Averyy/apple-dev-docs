# AccessoryMessage.Payload

**Framework**: Accessory Transport Extension  
**Kind**: struct  
**Role**: Structure

A structure that represents a single data payload within an accessory message.

**Availability**:
- iOS 26.5+

## Declaration

```swift
struct Payload
```

## Overview

The [`AccessoryMessage`](../accessorymessage.md) structure’s [`payloads`](./payloads.md) property contains an array of this type.

## Topics

### Creating a payload
- [init(transport: AccessoryTransport, data: Data)](./payload/init%28transport,data%29.md)
  Initializes a payload with data and a transport preference.
### Accessing payload content
- [let data: Data](./payload/data.md)
  A data object that contains the payload content.
- [let transport: AccessoryTransport](./payload/transport.md)
  A transport method for delivering the payload.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing message content
- [let payloads: [AccessoryMessage.Payload]](./payloads.md)
  An array of payload objects that comprise the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage/payload)*