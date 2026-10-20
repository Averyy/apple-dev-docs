# Collecting Network Connection Metrics

**Framework**: Network  
**Role**: Sample Code  
**Download**: [CollectingNetworkConnectionMetrics.zip](https://docs-assets.developer.apple.com/published/017625187506/CollectingNetworkConnectionMetrics.zip)

Use reports to understand how DNS and protocol handshakes impact connection establishment.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- Xcode 13.0+

#### Overview

> **Note**: This sample code project is associated with WWDC 2019 session [713: Advances in Networking, Part 2](https://developer.apple.com/videos/play/wwdc19/713/).

## See Also

### Collecting Connection Metrics
- [func requestEstablishmentReport(queue: DispatchQueue, completion: (NWConnection.EstablishmentReport?) -> Void)](./nwconnection/requestestablishmentreport%28queue,completion%29.md)
  Requests a copy of the connection’s establishment report once the connection is in the ready state.
- [NWConnection.EstablishmentReport](./nwconnection/establishmentreport.md)
  A report that provides metrics about the establishment of a connection.
- [func startDataTransferReport() -> NWConnection.PendingDataTransferReport](./nwconnection/startdatatransferreport%28%29.md)
  Begins a new data transfer report, which can later be collected.
- [NWConnection.PendingDataTransferReport](./nwconnection/pendingdatatransferreport.md)
  An outstanding data transfer report that has yet to be collected.
- [NWConnection.DataTransferReport](./nwconnection/datatransferreport.md)
  A report that provides metrics about data being sent and received on a connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/collecting-network-connection-metrics)*