# antecedent

**Framework**: Network  
**Kind**: property

An optional message context that must be sent before the context you are sending.

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
final let antecedent: NWConnection.ContentContext?
```

## See Also

- [init(identifier: String, expiration: UInt64, priority: Double, isFinal: Bool, antecedent: NWConnection.ContentContext?, metadata: [NWProtocolMetadata]?)](nwconnection/contentcontext/init(identifier:expiration:priority:isfinal:antecedent:metadata:).md)
  Initializes a custom message context.
- [let identifier: String](nwconnection/contentcontext/identifier.md)
  The identifier of the message, used for debugging.
- [var protocolMetadata: [NWProtocolMetadata]](nwconnection/contentcontext/protocolmetadata.md)
  An array of protocol metadata used to configure per-message or per-packet properties.
- [class NWProtocolMetadata](nwprotocolmetadata.md)
  The abstract superclass for specifying metadata about a network protocol.
- [let expirationMilliseconds: UInt64](nwconnection/contentcontext/expirationmilliseconds.md)
  A number of milliseconds after which sending the data associated with this context must begin, otherwise the data is discarded.
- [let relativePriority: Double](nwconnection/contentcontext/relativepriority.md)
  A relative value of priority used to reorder contexts when sending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/contentcontext/antecedent)*