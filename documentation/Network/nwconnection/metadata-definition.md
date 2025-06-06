# metadata(definition:)

**Framework**: Network  
**Kind**: method

Retrieves the connection-wide metadata for a specific protocol.

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
final func metadata(definition: NWProtocolDefinition) -> NWProtocolMetadata?
```

## See Also

- [class NWProtocolMetadata](nwprotocolmetadata.md)
  The abstract superclass for specifying metadata about a network protocol.
- [let endpoint: NWEndpoint](nwconnection/endpoint.md)
  The remote endpoint with which the connection was initialized.
- [let parameters: NWParameters](nwconnection/parameters.md)
  The parameters with which the connection was initialized.
- [var queue: DispatchQueue?](nwconnection/queue.md)
  The queue on which connection events are delivered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/metadata(definition:))*