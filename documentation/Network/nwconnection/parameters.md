# parameters

**Framework**: Network  
**Kind**: property

The parameters with which the connection was initialized.

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
final let parameters: NWParameters
```

## See Also

- [func metadata(definition: NWProtocolDefinition) -> NWProtocolMetadata?](nwconnection/metadata(definition:).md)
  Retrieves the connection-wide metadata for a specific protocol.
- [class NWProtocolMetadata](nwprotocolmetadata.md)
  The abstract superclass for specifying metadata about a network protocol.
- [let endpoint: NWEndpoint](nwconnection/endpoint.md)
  The remote endpoint with which the connection was initialized.
- [var queue: DispatchQueue?](nwconnection/queue.md)
  The queue on which connection events are delivered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/parameters)*