# NWParameters.ProtocolStack

**Framework**: Network  
**Kind**: class

An ordered set of protocol options that define the protocols that connections and listeners use.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class ProtocolStack
```

## Topics

### Adding Application Protocols
- [var applicationProtocols: [NWProtocolOptions]](nwparameters/protocolstack/applicationprotocols.md)
  The array of application protocol options used by connections and listeners.
### Configuring Lower Protocols
- [var transportProtocol: NWProtocolOptions?](nwparameters/protocolstack/transportprotocol.md)
  The transport protocol options used by connections and listeners.
- [var internetProtocol: NWProtocolOptions?](nwparameters/protocolstack/internetprotocol.md)
  The Internet Protocol options used by connections and listeners.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [var defaultProtocolStack: NWParameters.ProtocolStack](nwparameters/defaultprotocolstack.md)
  The protocol stack used by connections and listeners.
- [class NWProtocol](nwprotocol.md)
  The abstract superclass used by Network framework protocols and by custom network protocols that you define.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/protocolstack)*