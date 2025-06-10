# ConnectionProtocol

**Framework**: Network  
**Kind**: protocol

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
protocol ConnectionProtocol : Hashable, Identifiable
```

## Topics

### Associated Types
- [associatedtype ApplicationProtocolType : NetworkProtocolOptions](connectionprotocol/applicationprotocoltype.md)
### Instance Properties
- [var currentPath: NWPath?](connectionprotocol/currentpath.md)
  Current path for the connection, which can be used to extract interface and effective endpoint information
- [var debugDescription: String](connectionprotocol/debugdescription.md)
- [var identifier: UInt64](connectionprotocol/identifier.md)
- [var localEndpoint: NWEndpoint?](connectionprotocol/localendpoint.md)
  The local endpoint of the connection
- [var maximumDatagramSize: Int](connectionprotocol/maximumdatagramsize.md)
  Retrieve the maximum datagram size that can be sent on the connection. Any datagrams sent should be less than or equal to this size.
- [var parameters: NWParameters](connectionprotocol/parameters.md)
  The set of parameters with which the connection was created
- [var remoteEndpoint: NWEndpoint](connectionprotocol/remoteendpoint.md)
  The remote endpoint of the connection
- [var state: NWConnection.State](connectionprotocol/state.md)
  Access the current state of the connection
### Instance Methods
- [func cancelCurrentEndpoint()](connectionprotocol/cancelcurrentendpoint.md)
  Cancel the currently connected endpoint, causing the connection to fall through to the next endpoint if available, or to go to the waiting state if no more endpoints are available.
- [func establishmentReport() async throws -> NWConnection.EstablishmentReport?](connectionprotocol/establishmentreport.md)
  Asynchronously request the establishment report for this connection. If called prior to the connection being in the .ready state, the report will be nil.
- [func metadata(definition: NWProtocolDefinition) -> NWProtocolMetadata?](connectionprotocol/metadata(definition:).md)
  Access connection-wide protocol metadata on the connection. This allows access to state for protocols like TCP and TLS that have long-term state.
- [func startDataTransferReport() -> NWConnection.PendingDataTransferReport](connectionprotocol/startdatatransferreport.md)
  Start a new pending data transfer report on a connection. Multiple reports may be created for a single NWConnection. The report begins capturing data when the connection moves to the .ready state, or when the report is created (whichever occurs last).
### Default Implementations
- [Hashable Implementations](connectionprotocol/hashable-implementations.md)

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
### Inherited By
- [SubConnectionProtocol](subconnectionprotocol.md)
### Conforming Types
- [NetworkConnection](networkconnection.md)
- [NetworkConnection.SubConnection](networkconnection/subconnection.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/connectionprotocol)*