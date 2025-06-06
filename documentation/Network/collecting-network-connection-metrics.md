# Collecting Network Connection Metrics

**Framework**: Network

Use reports to understand how DNS and protocol handshakes impact connection establishment.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Xcode 13.0+

#### Overview

> **Note**: This sample code project is associated with WWDC 2019 session [`713: Advances in Networking, Part 2`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc19/713/).

## See Also

- [func requestEstablishmentReport(queue: DispatchQueue, completion: (NWConnection.EstablishmentReport?) -> Void)](nwconnection/requestestablishmentreport(queue:completion:).md)
  Requests a copy of the connection’s establishment report once the connection is in the ready state.
- [NWConnection.EstablishmentReport](nwconnection/establishmentreport.md)
  A report that provides metrics about the establishment of a connection.
- [func startDataTransferReport() -> NWConnection.PendingDataTransferReport](nwconnection/startdatatransferreport.md)
  Begins a new data transfer report, which can later be collected.
- [NWConnection.PendingDataTransferReport](nwconnection/pendingdatatransferreport.md)
  An outstanding data transfer report that has yet to be collected.
- [NWConnection.DataTransferReport](nwconnection/datatransferreport.md)
  A report that provides metrics about data being sent and received on a connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Network/collecting-network-connection-metrics)*