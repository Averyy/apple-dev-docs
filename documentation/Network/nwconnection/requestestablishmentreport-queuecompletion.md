# requestEstablishmentReport(queue:completion:)

**Framework**: Network  
**Kind**: method

Requests a copy of the connection’s establishment report once the connection is in the ready state.

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
@preconcurrency
final func requestEstablishmentReport(queue: DispatchQueue, completion: @escaping (NWConnection.EstablishmentReport?) -> Void)
```

## See Also

- [Collecting Network Connection Metrics](collecting-network-connection-metrics.md)
  Use reports to understand how DNS and protocol handshakes impact connection establishment.
- [NWConnection.EstablishmentReport](nwconnection/establishmentreport.md)
  A report that provides metrics about the establishment of a connection.
- [func startDataTransferReport() -> NWConnection.PendingDataTransferReport](nwconnection/startdatatransferreport.md)
  Begins a new data transfer report, which can later be collected.
- [NWConnection.PendingDataTransferReport](nwconnection/pendingdatatransferreport.md)
  An outstanding data transfer report that has yet to be collected.
- [NWConnection.DataTransferReport](nwconnection/datatransferreport.md)
  A report that provides metrics about data being sent and received on a connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/requestestablishmentreport(queue:completion:))*