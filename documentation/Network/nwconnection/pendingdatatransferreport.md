# NWConnection.PendingDataTransferReport

**Framework**: Network  
**Kind**: class

An outstanding data transfer report that has yet to be collected.

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
class PendingDataTransferReport
```

## Topics

### Collecting Reports
- [func collect(queue: DispatchQueue, completion: (NWConnection.DataTransferReport) -> Void)](nwconnection/pendingdatatransferreport/collect(queue:completion:).md)
  Stops an outstanding data transfer report and delivers the result.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [Collecting Network Connection Metrics](collecting-network-connection-metrics.md)
  Use reports to understand how DNS and protocol handshakes impact connection establishment.
- [func requestEstablishmentReport(queue: DispatchQueue, completion: (NWConnection.EstablishmentReport?) -> Void)](nwconnection/requestestablishmentreport(queue:completion:).md)
  Requests a copy of the connection’s establishment report once the connection is in the ready state.
- [NWConnection.EstablishmentReport](nwconnection/establishmentreport.md)
  A report that provides metrics about the establishment of a connection.
- [func startDataTransferReport() -> NWConnection.PendingDataTransferReport](nwconnection/startdatatransferreport.md)
  Begins a new data transfer report, which can later be collected.
- [NWConnection.DataTransferReport](nwconnection/datatransferreport.md)
  A report that provides metrics about data being sent and received on a connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/pendingdatatransferreport)*