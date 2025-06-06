# NWProtocolFramer.Options

**Framework**: Network  
**Kind**: class

A container you use to add your custom protocol to a connection’s protocol stack.

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
class Options
```

## Topics

### Creating Framer Options
- [init(definition: NWProtocolFramer.Definition)](nwprotocolframer/options/init(definition:).md)
  Initializes a set of protocol options with a custom framer definition.
### Subscripts
- [subscript(String) -> Any?](nwprotocolframer/options/subscript(_:).md)

## Relationships

### Inherits From
- [NWProtocolOptions](nwprotocoloptions.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [NWProtocolFramer.Definition](nwprotocolframer/definition.md)
  A custom protocol definition you use to associate messages with protocol options.
- [NWProtocolFramer.Message](nwprotocolframer/message.md)
  A message for a custom protocol, in which you can store arbitrary key-value pairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/options)*