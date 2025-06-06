# init(identifier:expiration:priority:isFinal:antecedent:metadata:)

**Framework**: Network  
**Kind**: init

Initializes a custom message context.

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
init(identifier: String, expiration: UInt64 = 0, priority: Double = 0.5, isFinal: Bool = false, antecedent: NWConnection.ContentContext? = nil, metadata: [NWProtocolMetadata]? = [])
```

## See Also

- [let identifier: String](nwconnection/contentcontext/identifier.md)
  The identifier of the message, used for debugging.
- [var protocolMetadata: [NWProtocolMetadata]](nwconnection/contentcontext/protocolmetadata.md)
  An array of protocol metadata used to configure per-message or per-packet properties.
- [class NWProtocolMetadata](nwprotocolmetadata.md)
  The abstract superclass for specifying metadata about a network protocol.
- [let antecedent: NWConnection.ContentContext?](nwconnection/contentcontext/antecedent.md)
  An optional message context that must be sent before the context you are sending.
- [let expirationMilliseconds: UInt64](nwconnection/contentcontext/expirationmilliseconds.md)
  A number of milliseconds after which sending the data associated with this context must begin, otherwise the data is discarded.
- [let relativePriority: Double](nwconnection/contentcontext/relativepriority.md)
  A relative value of priority used to reorder contexts when sending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/contentcontext/init(identifier:expiration:priority:isfinal:antecedent:metadata:))*