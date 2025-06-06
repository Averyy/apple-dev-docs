# NWConnection.DataTransferReport

**Framework**: Network  
**Kind**: struct

A report that provides metrics about data being sent and received on a connection.

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
struct DataTransferReport
```

## Topics

### Examining Data Transfer
- [let aggregatePathReport: NWConnection.DataTransferReport.PathReport](nwconnection/datatransferreport/aggregatepathreport.md)
  A report that sums counts across all network paths.
- [let pathReports: [NWConnection.DataTransferReport.PathReport]](nwconnection/datatransferreport/pathreports.md)
  An array of reports for each network path the connection used.
- [NWConnection.DataTransferReport.PathReport](nwconnection/datatransferreport/pathreport.md)
  A report that contains details about data transfer over a single network path.
### Summarizing Reports
- [let duration: TimeInterval](nwconnection/datatransferreport/duration.md)
  The duration of the data transfer report, from when it was started to when it was collected.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
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
- [NWConnection.PendingDataTransferReport](nwconnection/pendingdatatransferreport.md)
  An outstanding data transfer report that has yet to be collected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/datatransferreport)*