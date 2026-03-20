# AccessoryMessage.Payload

**Framework**: Accessory Transport Extension  
**Kind**: struct

A structure that represents a single data payload within an accessory message.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
struct Payload
```

#### Overview

The [`AccessoryMessage`](accessorymessage.md) structure’s [`payloads`](accessorymessage/payloads.md) property contains an array of this type.

## Topics

### Creating a payload
- [init(transport: AccessoryMessage.Transport, data: Data)](accessorymessage/payload/init(transport:data:).md)
  Initializes a payload with a transport method and data.
### Accessing payload content
- [let data: Data](accessorymessage/payload/data.md)
  A data object that contains the payload content.
- [let transport: AccessoryMessage.Transport](accessorymessage/payload/transport.md)
  A transport method for delivering the payload.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let payloads: [AccessoryMessage.Payload]](accessorymessage/payloads.md)
  An array of payload objects that comprise the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage/payload)*