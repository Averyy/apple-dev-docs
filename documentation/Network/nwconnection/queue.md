# queue

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

The queue on which connection events are delivered.

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
final var queue: DispatchQueue? { get }
```

## See Also

### Inspecting Connections
- [func metadata(definition: NWProtocolDefinition) -> NWProtocolMetadata?](./metadata%28definition%29.md)
  Retrieves the connection-wide metadata for a specific protocol.
- [class NWProtocolMetadata](../nwprotocolmetadata.md)
  The abstract superclass for specifying metadata about a network protocol.
- [let endpoint: NWEndpoint](./endpoint.md)
  The remote endpoint with which the connection was initialized.
- [let parameters: NWParameters](./parameters.md)
  The parameters with which the connection was initialized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/queue)*