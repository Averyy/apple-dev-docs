# relativePriority

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

A relative value of priority used to reorder contexts when sending.

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
final let relativePriority: Double
```

## Discussion

Relative priority of contexts only affects ordering when there is a queue of messages to be sent. The priority is a double ranging from 0.0 to 1.0, where default messages are set to 0.5.

## See Also

### Creating Custom Send Contexts
- [init(identifier: String, expiration: UInt64, priority: Double, isFinal: Bool, antecedent: NWConnection.ContentContext?, metadata: [NWProtocolMetadata]?)](./init%28identifier,expiration,priority,isfinal,antecedent,metadata%29.md)
  Initializes a custom message context.
- [let identifier: String](./identifier.md)
  The identifier of the message, used for debugging.
- [var protocolMetadata: [NWProtocolMetadata]](./protocolmetadata.md)
  An array of protocol metadata used to configure per-message or per-packet properties.
- [class NWProtocolMetadata](../../nwprotocolmetadata.md)
  The abstract superclass for specifying metadata about a network protocol.
- [let antecedent: NWConnection.ContentContext?](./antecedent.md)
  An optional message context that must be sent before the context you are sending.
- [let expirationMilliseconds: UInt64](./expirationmilliseconds.md)
  A number of milliseconds after which sending the data associated with this context must begin, otherwise the data is discarded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/contentcontext/relativepriority)*