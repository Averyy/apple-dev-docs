# NWProtocolFramer.Options

**Framework**: Network  
**Kind**: class  
**Role**: Class

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
- [init(definition: NWProtocolFramer.Definition)](./options/init%28definition%29.md)
  Initializes a set of protocol options with a custom framer definition.
### Subscripts
- [subscript(String) -> Any?](./options/subscript%28_%29.md)

## Relationships

### Inherits From
- [NWProtocolOptions](../nwprotocoloptions.md)
### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Using Framers with Connections
- [NWProtocolFramer.Definition](./definition.md)
  A custom protocol definition you use to associate messages with protocol options.
- [NWProtocolFramer.Message](./message.md)
  A message for a custom protocol, in which you can store arbitrary key-value pairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/options)*