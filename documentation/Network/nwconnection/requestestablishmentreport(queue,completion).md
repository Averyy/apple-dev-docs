# requestEstablishmentReport(queue:completion:)

**Framework**: Network  
**Kind**: method  
**Role**: Instance Method

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
final func requestEstablishmentReport(queue: DispatchQueue, completion: @escaping @Sendable (NWConnection.EstablishmentReport?) -> Void)
```

## See Also

### Collecting Connection Metrics
- [Collecting Network Connection Metrics](../collecting-network-connection-metrics.md)
  Use reports to understand how DNS and protocol handshakes impact connection establishment.
- [NWConnection.EstablishmentReport](./establishmentreport.md)
  A report that provides metrics about the establishment of a connection.
- [func startDataTransferReport() -> NWConnection.PendingDataTransferReport](./startdatatransferreport%28%29.md)
  Begins a new data transfer report, which can later be collected.
- [NWConnection.PendingDataTransferReport](./pendingdatatransferreport.md)
  An outstanding data transfer report that has yet to be collected.
- [NWConnection.DataTransferReport](./datatransferreport.md)
  A report that provides metrics about data being sent and received on a connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/requestestablishmentreport(queue:completion:))*