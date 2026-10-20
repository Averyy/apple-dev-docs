# NWProtocolFramer.Definition

**Framework**: Network  
**Kind**: class  
**Role**: Class

A custom protocol definition you use to associate messages with protocol options.

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
class Definition
```

## Topics

### Defining Framer Protocols
- [init(implementation: any NWProtocolFramerImplementation.Type)](./definition/init%28implementation%29.md)
  Initializes a new protocol definition based on your protocol implementation.

## Relationships

### Inherits From
- [NWProtocolDefinition](../nwprotocoldefinition.md)
### Conforms To
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Using Framers with Connections
- [NWProtocolFramer.Options](./options.md)
  A container you use to add your custom protocol to a connection’s protocol stack.
- [NWProtocolFramer.Message](./message.md)
  A message for a custom protocol, in which you can store arbitrary key-value pairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/definition)*