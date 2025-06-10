# NWProtocolFramer.Definition

**Framework**: Network  
**Kind**: class

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
- [init(implementation: any NWProtocolFramerImplementation.Type)](nwprotocolframer/definition/init(implementation:).md)
  Initializes a new protocol definition based on your protocol implementation.

## Relationships

### Inherits From
- [NWProtocolDefinition](nwprotocoldefinition.md)
### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NWProtocolFramer.Options](nwprotocolframer/options.md)
  A container you use to add your custom protocol to a connection’s protocol stack.
- [NWProtocolFramer.Message](nwprotocolframer/message.md)
  A message for a custom protocol, in which you can store arbitrary key-value pairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/definition)*