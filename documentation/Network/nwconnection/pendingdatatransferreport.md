# NWConnection.PendingDataTransferReport

**Framework**: Network  
**Kind**: class  
**Role**: Class

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
- [func collect(queue: DispatchQueue, completion: (NWConnection.DataTransferReport) -> Void)](./pendingdatatransferreport/collect%28queue,completion%29.md)
  Stops an outstanding data transfer report and delivers the result.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Collecting Connection Metrics
- [Collecting Network Connection Metrics](../collecting-network-connection-metrics.md)
  Use reports to understand how DNS and protocol handshakes impact connection establishment.
- [func requestEstablishmentReport(queue: DispatchQueue, completion: (NWConnection.EstablishmentReport?) -> Void)](./requestestablishmentreport%28queue,completion%29.md)
  Requests a copy of the connection’s establishment report once the connection is in the ready state.
- [NWConnection.EstablishmentReport](./establishmentreport.md)
  A report that provides metrics about the establishment of a connection.
- [func startDataTransferReport() -> NWConnection.PendingDataTransferReport](./startdatatransferreport%28%29.md)
  Begins a new data transfer report, which can later be collected.
- [NWConnection.DataTransferReport](./datatransferreport.md)
  A report that provides metrics about data being sent and received on a connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/pendingdatatransferreport)*