# NWProtocolFramer.Message

**Framework**: Network  
**Kind**: class  
**Role**: Class

A message for a custom protocol, in which you can store arbitrary key-value pairs.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class Message
```

## Topics

### Creating Framer Messages
- [init(definition: NWProtocolFramer.Definition)](./message/init%28definition%29.md)
  Initializes an empty message for a custom framer definition.
- [init(instance: NWProtocolFramer.Instance)](./message/init%28instance%29.md)
  Initializes an empty message from within a framer implementation.
### Accessing Message Metadata
- [subscript(String) -> Any?](./message/subscript%28_%29.md)
  Get and set object values in a custom framer message.

## Relationships

### Inherits From
- [NWProtocolMetadata](../nwprotocolmetadata.md)
### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Using Framers with Connections
- [NWProtocolFramer.Definition](./definition.md)
  A custom protocol definition you use to associate messages with protocol options.
- [NWProtocolFramer.Options](./options.md)
  A container you use to add your custom protocol to a connection’s protocol stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/message)*